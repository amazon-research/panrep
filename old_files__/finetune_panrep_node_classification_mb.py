"""
Modeling Relational Data with Graph Convolutional Networks
Paper: https://arxiv.org/abs/1703.06103
Code: https://github.com/tkipf/relational-gcn

Difference compared to tkipf/relation-gcn
* l2norm applied to all weights
* remove nodes that won't be touched
"""
from node_sampling_masking import  HeteroNeighborSampler,InfomaxNodeRecNeighborSampler
import os
from datetime import datetime
import pickle
import argparse
import numpy as np
import time
import torch
import torch.nn.functional as F
import dgl
from classifiers import ClassifierMLP
from load_data import load_hetero_data,generate_rwalks
from model import PanRepHetero
from sklearn.metrics import roc_auc_score
from torch.utils.data import DataLoader
from node_supervision_tasks import MetapathRWalkerSupervision,LinkPredictor
from encoders import EncoderRelGraphConvHetero,EncoderRelGraphAttentionHetero
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, normalized_mutual_info_score, adjusted_rand_score
from sklearn.cluster import KMeans
from sklearn.svm import LinearSVC


def extract_embed(node_embed, block):
    emb = {}
    for ntype in block.srctypes:
        nid = block.srcnodes[ntype].data[dgl.NID]
        emb[ntype] = node_embed[ntype][nid]
    return emb
def evaluate(model, seeds, blocks, device, labels, category, use_cuda):
    model.eval()
    #emb = extract_embed(node_embed, blocks[0])
    lbl = labels[seeds]
    if use_cuda:
        lbl = lbl.cuda()
        for i in range(len(blocks)):
            blocks[i] = blocks[i].to(device)
    logits = model.classifier_forward_mb(blocks)[category]
    loss = F.binary_cross_entropy_with_logits(logits, lbl)

    acc = torch.sum(logits.argmax(dim=1) == lbl.argmax(dim=1) ).item() / len(seeds)
    pred = torch.sigmoid(logits).detach().cpu().numpy()
    try:
        acc_auc = roc_auc_score(lbl.cpu().numpy(), pred)
    except ValueError:
        acc_auc = -1
        pass
    return loss, acc,acc_auc

def eval_panrep(model,dataloader):
    model.eval()

    print("==========Start evaluating===============")
    for i, (seeds, blocks) in enumerate(dataloader):

        loss, embeddings = model.forward_mb(p_blocks=blocks)
    print("=============Evaluation finished=============")
    return

def _fit(n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
         use_infomax_loss, mask_links,use_self_loop,use_node_motif, num_cluster,single_layer,motif_cluster,k_fold,rw_supervision,args):
    if num_cluster>0:
        args.use_cluster=True
        args.num_clusters=num_cluster
    else:
        args.use_cluster = False
    args.k_fold=k_fold
    args.rw_supervision = rw_supervision
    args.motif_clusters=motif_cluster
    args.use_node_motifs=use_node_motif
    train_idx, test_idx, val_idx, labels, g, category, num_classes, masked_node_types,metapaths=\
        load_hetero_data(args)


    # sampler parameters
    batch_size = 4*1024
    l2norm=0.0001

    # check cuda
    use_cuda = args.gpu >= 0 and torch.cuda.is_available()
    if use_cuda:
        torch.cuda.set_device(args.gpu)
        labels = labels.cuda()

    device = torch.device("cuda:" + str(args.gpu) if use_cuda else "cpu")
        # create model
    #dgl.contrib.sampling.sampler.EdgeSampler(g['customer_to_transaction'], batch_size=100)
    use_reconstruction_loss = use_reconstruction_loss
    use_infomax_loss = use_infomax_loss

    # not used currently
    num_masked_nodes = -1
    node_masking = False
    loss_over_all_nodes = True
    pct_masked_edges = -1
    negative_rate = -1
    link_prediction = use_link_prediction
    mask_links = mask_links


    # for the embedding layer
    out_size_dict={}
    for name in g.ntypes:
        if name not in masked_node_types:
            if num_cluster>0:
                out_size_dict[name]=g.nodes[name].data['h_clusters'].size(1)
            else:
                out_size_dict[name] = g.nodes[name].data['h_f'].size(1)
        else:
            out_size_dict[name] =0

    # for the motif layer

    out_motif_dict = {}
    if use_node_motif:
        for name in g.ntypes:
            out_motif_dict[name] = g.nodes[name].data['motifs'].size(1)

    ntype2id = {}
    for i, ntype in enumerate(g.ntypes):
            ntype2id[ntype] = i
    if args.encoder=='RGCN':
        encoder=EncoderRelGraphConvHetero(
                                  n_hidden,
                                    g=g,
                                    device=device,
                                  num_bases=n_bases,
                                          etypes=g.etypes,
                                        ntypes=g.ntypes,
                                  num_hidden_layers=n_layers,
                                  dropout=dropout,
                                  use_self_loop=use_self_loop)
    elif args.encoder=='RGAT':
        encoder = EncoderRelGraphAttentionHetero(
                                            n_hidden,
                                            etypes=g.etypes,
                                            ntypes=g.ntypes,
                                            num_hidden_layers=n_layers,
                                            dropout=dropout,
                                            use_self_loop=use_self_loop)

    metapathRWSupervision = None
    if rw_supervision:
        mrw_interact = {}
        for ntype in g.ntypes:
            mrw_interact[ntype]=[]
            for neighbor_ntype in g.ntypes:
                mrw_interact[ntype] +=[neighbor_ntype]

        metapathRWSupervision = MetapathRWalkerSupervision(in_dim=n_hidden, negative_rate=5,
                                                           device=device,mrw_interact=mrw_interact)
    link_predictor = None
    if use_link_prediction:
        link_predictor = LinkPredictor(out_dim=n_hidden, etypes=g.etypes,
                                      ntype2id=ntype2id, use_cuda=use_cuda)

    model = PanRepHetero(
                             n_hidden,
                             n_hidden,
                             etypes=g.etypes,
                             encoder=encoder,
                             ntype2id=ntype2id,
                             num_hidden_layers=n_layers,
                             dropout=dropout,
                             out_size_dict=out_size_dict,
                             masked_node_types=masked_node_types,
                             loss_over_all_nodes=loss_over_all_nodes,
                             use_infomax_task=use_infomax_loss,
                             use_reconstruction_task=use_reconstruction_loss,
                             use_node_motif=use_node_motif,
                             link_predictor=link_predictor,
                             out_motif_dict=out_motif_dict,
                             use_cluster=num_cluster>0,
                             single_layer_clusterandrecover_decoder=single_layer,
                             use_cuda=use_cuda,
                             metapathRWSupervision=metapathRWSupervision)


    if use_cuda:
        model.cuda()
    node_embed={}
    for ntype in g.ntypes:
        if ntype not in masked_node_types:
            node_embed[ntype]=g.nodes[ntype].data['h_f']


    if len(labels.shape)>1:
        zero_rows=np.where(~(labels).cpu().numpy().any(axis=1))[0]

        train_idx=np.array(list(set(train_idx).difference(set(zero_rows))))
        val_idx = np.array(list(set(val_idx).difference(set(zero_rows))))
        test_idx = np.array(list(set(test_idx).difference(set(zero_rows))))
        #TODO val set not used currently


    if use_cuda:
        g=g.to(device)

    val_pct=0.1
    evaluate_every=50
    sampler = InfomaxNodeRecNeighborSampler(g, [fanout] * (n_layers), device=device, full_neighbor=True)
    pr_node_ids=list(sampler.hetero_map.keys())
    pr_val_ind=list(np.random.choice(len(pr_node_ids), int(len(pr_node_ids)*val_pct), replace=False))
    pr_train_ind=list(set(list(np.arange(len(pr_node_ids)))).difference(set(pr_val_ind)))
    loader = DataLoader(dataset=pr_train_ind,
                        batch_size=batch_size,
                        collate_fn=sampler.sample_blocks,
                        shuffle=True,
                        num_workers=0)


    valid_loader = DataLoader(dataset=pr_val_ind,
                        batch_size=batch_size,
                        collate_fn=sampler.sample_blocks,
                        shuffle=True,
                        num_workers=0)
    #TODO LOAD All data in GPU
    #  Use validation set to supervise embeddings using the clustering accuracy loss and the others...

    # optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=l2norm)

    # training loop
    print("start training...")


    for epoch in range(n_epochs):
        model.train()

        optimizer.zero_grad()
        for i, (seeds, blocks) in enumerate(loader):

            if link_prediction:
                raise NotImplementedError
            if rw_supervision:
                rw_neighbors=generate_rwalks(g=g,metapaths=metapaths,samples_per_node=4,device=device)
            else:
                rw_neighbors=None
            loss, embeddings = model.forward_mb(p_blocks=blocks,rw_neighbors=rw_neighbors)
            loss.backward()
            optimizer.step()


            print("Train Loss: {:.4f} Epoch {:05d} | Batch {:03d}".format(loss.item(), epoch, i))
        if epoch % evaluate_every == 0:
            eval_panrep(model=model, dataloader=valid_loader)
    ## Evaluate before finetune
    model.eval()
    if use_cuda:
        model.cpu()
        model.encoder.cpu()
        g=g.to(torch.device("cpu"))
    with torch.no_grad():
        embeddings = model.encoder.forward(g)
    if use_cuda:
        model.cuda()
        model.encoder.cuda()
        g=g.to(device)

    feats = embeddings[category]
    #mlp_classifier(feats,use_cuda,args,num_classes,labels,train_idx,val_idx,test_idx,device)
    labels_i=np.argmax(labels.cpu().numpy(),axis=1)
    svm_macro_f1_list, svm_micro_f1_list, nmi_mean, nmi_std, ari_mean, ari_std,macro_str,micro_str = evaluate_results_nc(
        feats[test_idx].cpu().numpy(), labels_i[test_idx], num_classes=num_classes)
    ## Finetune PanRep
    # add the target category in the sampler
    sampler = InfomaxNodeRecNeighborSampler(g, [fanout] * (n_layers), device=device, full_neighbor=True,category=category)
    fine_tune_loader = DataLoader(dataset=list(train_idx),
                        batch_size=batch_size,
                        collate_fn=sampler.sample_blocks,
                        shuffle=True,
                        num_workers=0)


    # validation sampler
    val_sampler = HeteroNeighborSampler(g, category, [fanout] * n_layers, True)
    _, val_blocks = val_sampler.sample_blocks(val_idx)

    # test sampler
    test_sampler = HeteroNeighborSampler(g, category, [fanout] * n_layers, True)
    _, test_blocks = test_sampler.sample_blocks(test_idx)
    # set up fine_tune epochs
    n_init_fine_epochs=0
    n_fine_tune_epochs=n_fine_tune_epochs-n_init_fine_epochs


    # donwstream classifier
    multilabel = True
    model.classifier=ClassifierMLP(input_size=n_hidden,hidden_size=n_hidden,out_size=num_classes)
    if multilabel is False:
        loss_func = torch.nn.CrossEntropyLoss()
    else:
        loss_func = torch.nn.BCEWithLogitsLoss()
    if use_cuda:
        model.cuda()
        feats=feats.cuda()
    labels=labels.float()
    best_test_acc=0
    best_val_acc=0
    #NodeClassifierRGCN(in_dim= n_hidden,out_dim=num_classes, rel_names=g.etypes,num_bases=n_bases)
    optimizer_init = torch.optim.Adam(model.classifier.parameters(), lr=lr, weight_decay=l2norm)
    for epoch in range(n_init_fine_epochs):
            model.classifier.train()
            optimizer.zero_grad()
            t0 = time.time()
            lbl = labels
            logits = model.classifier.forward(feats)
            loss = F.binary_cross_entropy_with_logits(logits[train_idx].squeeze(1),
                                                      lbl[train_idx].type(torch.FloatTensor).to(device))
            loss.backward()
            optimizer_init.step()
            pred = torch.sigmoid(logits).detach().cpu().numpy()
            train_acc = roc_auc_score(labels.cpu()[train_idx].numpy(),
                                      pred[train_idx], average='macro')
            val_acc = roc_auc_score(labels.cpu()[val_idx].numpy(),
                                    pred[val_idx], average='macro')
            test_acc = roc_auc_score(labels.cpu()[test_idx].numpy()
                                     , pred[test_idx], average='macro')
            test_acc_w = roc_auc_score(labels.cpu()[test_idx].numpy()
                                       , pred[test_idx], average='weighted')
            if best_val_acc < val_acc:
                best_val_acc = val_acc
                best_test_acc = test_acc

            if epoch % 5 == 0:
                print(
                    'Loss %.4f, Train Acc %.4f, Val Acc %.4f (Best %.4f), Test Acc %.4f (Best %.4f), Weighted Test Acc %.4f' % (
                        loss.item(),
                        train_acc.item(),
                        val_acc.item(),
                        best_val_acc.item(),
                        test_acc.item(),
                        best_test_acc.item(), test_acc_w.item()
                    ))
    print()


    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=l2norm)
    # training loop
    print("start training...")
    forward_time = []
    backward_time = []
    model.train()

    dur = []



    for epoch in range(n_fine_tune_epochs):
        model.train()
        optimizer.zero_grad()
        if epoch > 3:
            t0 = time.time()

        for i, (seeds, blocks) in enumerate(fine_tune_loader):
            batch_tic = time.time()
            # need to copy the features
            for i in range(len(blocks)):
                blocks[i] = blocks[i].to(device)
            #emb = extract_embed(node_embed, blocks[0])
            lbl = labels[seeds[category]]
            logits = model.classifier_forward_mb(blocks)[category]
            loss = loss_func(logits, lbl)
            loss.backward()
            optimizer.step()

            train_acc = torch.sum(logits.argmax(dim=1) == lbl.argmax(dim=1)).item() / len(seeds[category])
            pred = torch.sigmoid(logits).detach().cpu().numpy()
            try:
                train_acc_auc = roc_auc_score(lbl.cpu().numpy(), pred)
            except ValueError:
                train_acc_auc=-1
                pass
            print("Epoch {:05d} | Batch {:03d} | Train Acc: {:.4f} |Train Acc AUC: {:.4f}| Train Loss: {:.4f} | Time: {:.4f}".
                  format(epoch, i, train_acc,train_acc_auc, loss.item(), time.time() - batch_tic))

        if epoch > 3:
            dur.append(time.time() - t0)

        val_loss, val_acc,val_acc_auc = evaluate(model, val_idx, val_blocks,device, labels, category,use_cuda)
        print("Epoch {:05d} | Valid Acc: {:.4f} |Valid Acc Auc: {:.4f} | Valid loss: {:.4f} | Time: {:.4f}".
              format(epoch, val_acc, val_acc_auc,val_loss.item(), np.average(dur)))
    print()

    # full graph evaluation here
    model.eval()
    if use_cuda:
        model.cpu()
        model.encoder.cpu()
        g=g.to(torch.device("cpu"))
    with torch.no_grad():
        embeddings = model.encoder.forward(g)
        logits=model.classifier_forward(g)[category]

    acc = torch.sum(logits[test_idx].argmax(dim=1) == labels[test_idx].cpu().argmax(dim=1)).item() / len(test_idx)
    print("Test accuracy: {:4f}".format(acc))
    print("Mean forward time: {:4f}".format(np.mean(forward_time[len(forward_time) // 4:])))
    print("Mean backward time: {:4f}".format(np.mean(backward_time[len(backward_time) // 4:])))

    feats = embeddings[category]
    #mlp_classifier(feats,use_cuda,args,num_classes,labels,train_idx,val_idx,test_idx,device)
    labels_i=np.argmax(labels.cpu().numpy(),axis=1)
    svm_macro_f1_list, svm_micro_f1_list, nmi_mean, nmi_std, ari_mean, ari_std,finmacro_str,finmicro_str = evaluate_results_nc(
        feats[test_idx].cpu().numpy(), labels_i[test_idx], num_classes=num_classes)
    print("With logits")
    svm_macro_f1_list, svm_micro_f1_list, nmi_mean, nmi_std, ari_mean, ari_std, macro_str_log, micro_str_log = evaluate_results_nc(
        logits[test_idx].cpu().numpy(), labels_i[test_idx], num_classes=num_classes)
    return " | PanRep " +macro_str+" "+micro_str+ " | Test accuracy: {:4f} | ".format(acc)+" | Finetune "+finmacro_str+" "+finmicro_str+" Logits: "+macro_str_log+" "+micro_str_log

def fit(args):

        n_epochs_list =[50, 100, 300]  # [250,300]
        n_hidden_list = [50, 100, 150]#[50, 100, 300, 500, 700]  # [40,200,400]
        n_fine_tune_epochs_list= [50]#[20,50]#[30,50,150]
        n_layers_list = [2,3]#[2,3]#[2,3]
        n_bases_list = [30]
        lr_list = [1e-3,1e-4]
        dropout_list = [0.2]
        fanout_list = [None]
        use_link_prediction_list = [False]
        use_reconstruction_loss_list =[True,False]#[False,True]
        use_infomax_loss_list = [True,False]#[False,True]
        use_node_motif_list = [True,False]
        rw_supervision_list=[True,False]
        num_cluster_list=[6]
        K_list=[0]#[2,5,10,15]
        motif_cluster_list=[5]#[2,6,10]
        mask_links_list = [False]
        use_self_loop_list=[False]
        single_layer_list=[False]
        results={}
        for n_epochs in n_epochs_list:
            for n_fine_tune_epochs in n_fine_tune_epochs_list:
                for n_hidden in n_hidden_list:
                    for n_layers in n_layers_list:
                        for n_bases in n_bases_list:
                            for fanout in fanout_list:
                                for lr in lr_list:
                                    for dropout in dropout_list:
                                        for use_infomax_loss in use_infomax_loss_list:
                                            for use_link_prediction in use_link_prediction_list:
                                                for use_reconstruction_loss in use_reconstruction_loss_list:
                                                    for mask_links in mask_links_list:
                                                        for use_self_loop in use_self_loop_list:
                                                            for use_node_motif in use_node_motif_list:
                                                                for num_cluster in num_cluster_list:
                                                                    for single_layer in single_layer_list:
                                                                        for motif_cluster in motif_cluster_list:
                                                                            for rw_supervision in rw_supervision_list:
                                                                                for k_fold in K_list:
                                                                                    if not use_reconstruction_loss and not \
                                                                                            use_infomax_loss and not use_link_prediction\
                                                                                            and not use_node_motif and not rw_supervision:
                                                                                        continue
                                                                                    else:
                                                                                        acc=_fit(n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
                                                                                                 use_link_prediction, use_reconstruction_loss,
                                                                                                 use_infomax_loss, mask_links, use_self_loop,
                                                                                             use_node_motif,num_cluster,single_layer,
                                                                                                 motif_cluster,k_fold,rw_supervision,args)
                                                                                        results[(n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
                                                                                                 use_link_prediction, use_reconstruction_loss,
                                                                                                 use_infomax_loss, mask_links, use_self_loop,
                                                                                             use_node_motif,num_cluster,single_layer,
                                                                                                 motif_cluster,k_fold,rw_supervision)]=acc

                                                                                        result = "PanRep-RGCN Model, n_epochs {}; n_fine_tune_epochs {}; n_hidden {}; n_layers {}; n_bases {}; " \
                                                                                                 "fanout {}; lr {}; dropout {} use_reconstruction_loss {} " \
                                                                                                 "use_link_prediction {} use_infomax_loss {} mask_links {} " \
                                                                                                 "use_self_loop {} use_node_motif {} num_cluster {}" \
                                                                                                 " single_layer {} motif_cluster {} " \
                                                                                                 "k_fold {} rw_supervision{} acc {}".format(
                                                                                            n_epochs,
                                                                                            n_fine_tune_epochs,
                                                                                            n_hidden,
                                                                                            n_layers,
                                                                                            n_bases,
                                                                                            0,
                                                                                            lr,
                                                                                            dropout,
                                                                                            use_reconstruction_loss,
                                                                                            use_link_prediction,
                                                                                            use_infomax_loss,
                                                                                            mask_links,use_self_loop,use_node_motif,
                                                                                            num_cluster,single_layer,motif_cluster,k_fold,
                                                                                            rw_supervision,acc)
                                                                                        print(result)
        results[str(args)]=1
        file=args.dataset+'-'+str(datetime.date(datetime.now()))+"-"+str(datetime.time(datetime.now()))
        pickle.dump(results, open(os.path.join("results/finetune_node_classification/", file + ".pickle"), "wb"),
                    protocol=4)
        return

def kmeans_test(X, y, n_clusters, repeat=10):
    nmi_list = []
    ari_list = []
    for _ in range(repeat):
        kmeans = KMeans(n_clusters=n_clusters)
        y_pred = kmeans.fit_predict(X)
        nmi_score = normalized_mutual_info_score(y, y_pred, average_method='arithmetic')
        ari_score = adjusted_rand_score(y, y_pred)
        nmi_list.append(nmi_score)
        ari_list.append(ari_score)
    return np.mean(nmi_list), np.std(nmi_list), np.mean(ari_list), np.std(ari_list)


def svm_test(X, y, test_sizes=(0.2, 0.4, 0.6, 0.8), repeat=10):
    random_states = [182318 + i for i in range(repeat)]
    result_macro_f1_list = []
    result_micro_f1_list = []
    for test_size in test_sizes:
        macro_f1_list = []
        micro_f1_list = []
        for i in range(repeat):
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, shuffle=True, random_state=random_states[i])
            svm = LinearSVC(dual=False)
            svm.fit(X_train, y_train)
            y_pred = svm.predict(X_test)
            macro_f1 = f1_score(y_test, y_pred, average='macro')
            micro_f1 = f1_score(y_test, y_pred, average='micro')
            macro_f1_list.append(macro_f1)
            micro_f1_list.append(micro_f1)
        result_macro_f1_list.append((np.mean(macro_f1_list), np.std(macro_f1_list)))
        result_micro_f1_list.append((np.mean(micro_f1_list), np.std(micro_f1_list)))
    return result_macro_f1_list, result_micro_f1_list


def evaluate_results_nc(embeddings, labels, num_classes):
    print('SVM test')
    svm_macro_f1_list, svm_micro_f1_list = svm_test(embeddings, labels)
    macro_str='Macro-F1: ' + ', '.join(['{:.6f}~{:.6f} ({:.1f})'.format(macro_f1_mean, macro_f1_std, train_size) for
                                    (macro_f1_mean, macro_f1_std), train_size in
                                    zip(svm_macro_f1_list, [0.8, 0.6, 0.4, 0.2])])

    micro_str='Micro-F1: ' + ', '.join(['{:.6f}~{:.6f} ({:.1f})'.format(micro_f1_mean, micro_f1_std, train_size) for
                                    (micro_f1_mean, micro_f1_std), train_size in
                                    zip(svm_micro_f1_list, [0.8, 0.6, 0.4, 0.2])])
    print(macro_str)
    print(micro_str)
    print('K-means test')
    nmi_mean, nmi_std, ari_mean, ari_std = kmeans_test(embeddings, labels, num_classes)
    print('NMI: {:.6f}~{:.6f}'.format(nmi_mean, nmi_std))
    print('ARI: {:.6f}~{:.6f}'.format(ari_mean, ari_std))

    return svm_macro_f1_list, svm_micro_f1_list, nmi_mean, nmi_std, ari_mean, ari_std,macro_str,micro_str


def mlp_classifier(feats,use_cuda,n_hidden,lr_d,n_cepochs,args,num_classes,labels,train_idx,val_idx,test_idx,device):
    ###
    # Use the encoded features for classification
    # Here we initialize the features using the reconstructed ones

    # feats = g.nodes[category].data['features']
    l2norm = 0.0001
    inp_dim = feats.shape[1]
    model = ClassifierMLP(input_size=inp_dim, hidden_size=n_hidden,out_size=num_classes)

    if use_cuda:
        model.cuda()
        feats=feats.cuda()

    # optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=lr_d, weight_decay=l2norm)

    # training loop
    print("start training...")
    forward_time = []
    backward_time = []
    model.train()

    # TODO find all zero indices rows and remove.
    if len(labels.shape)>1:
        zero_rows=np.where(~(labels).cpu().numpy().any(axis=1))[0]

        train_idx=np.array(list(set(train_idx).difference(set(zero_rows))))
        val_idx = np.array(list(set(val_idx).difference(set(zero_rows))))
        test_idx = np.array(list(set(test_idx).difference(set(zero_rows))))

    train_indices = torch.tensor(train_idx).to(device);
    valid_indices = torch.tensor(val_idx).to(device);
    test_indices = torch.tensor(test_idx).to(device);




    best_val_acc = 0
    best_test_acc = 0
    labels_n=labels

    for epoch in range(n_cepochs):
        optimizer.zero_grad()
        logits = model(feats)
        loss = F.binary_cross_entropy_with_logits(logits[train_idx].squeeze(1), labels_n[train_idx].type(torch.FloatTensor).to(device))
        loss.backward()
        optimizer.step()
        pred = torch.sigmoid(logits).detach().cpu().numpy()

        train_acc = roc_auc_score(labels_n.cpu()[train_indices.cpu()].numpy(),
                                  pred[train_indices.cpu()],average='macro')
        val_acc = roc_auc_score(labels_n.cpu()[valid_indices.cpu()].numpy(),
                                pred[valid_indices.cpu()],average='macro')
        test_acc = roc_auc_score(labels_n.cpu()[test_indices.cpu()].numpy()
                                 , pred[test_indices.cpu()],average='macro')
        test_acc_w = roc_auc_score(labels_n.cpu()[test_indices.cpu()].numpy()
                                 , pred[test_indices.cpu()], average='weighted')
        if best_val_acc < val_acc:
            best_val_acc = val_acc
            best_test_acc = test_acc

        if epoch % 5 == 0:
            print('Loss %.4f, Train Acc %.4f, Val Acc %.4f (Best %.4f), Test Acc %.4f (Best %.4f), Weighted Test Acc %.4f' % (
                loss.item(),
                train_acc.item(),
                val_acc.item(),
                best_val_acc.item(),
                test_acc.item(),
                best_test_acc.item(),test_acc_w.item()
            ))
    print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PanRep-FineTune')
    parser.add_argument("--dropout", type=float, default=0.2,
            help="dropout probability")
    parser.add_argument("--n-hidden", type=int, default=60,
            help="number of hidden units") # use 16, 2 for debug
    parser.add_argument("--gpu", type=int, default=2,
            help="gpu")
    parser.add_argument("--lr", type=float, default=1e-3,
            help="learning rate")
    parser.add_argument("--lr-d", type=float, default=1e-2,
            help="learning rate")
    parser.add_argument("--n-bases", type=int, default=20,
            help="number of filter weight matrices, default: -1 [use all]")
    parser.add_argument("--n-layers", type=int, default=3,
            help="number of propagation rounds")
    parser.add_argument("-e", "--n-epochs", type=int, default=200,
            help="number of training epochs for decoder")
    parser.add_argument("-ec", "--n-cepochs", type=int, default=2,
                        help="number of training epochs for classification")
    parser.add_argument("-num_masked", "--n-masked-nodes", type=int, default=100,
                        help="number of masked nodes")
    parser.add_argument("-pct_masked_links", "--pct-masked-links", type=int, default=0.5,
                        help="number of masked links")
    parser.add_argument("-negative_rate", "--negative-rate", type=int, default=4,
                        help="number of negative examples per masked link")


    parser.add_argument("-d", "--dataset", type=str, required=True,
            help="dataset to use")
    parser.add_argument("-en", "--encoder", type=str, required=True,
                        help="Encoder to use")
    parser.add_argument("--l2norm", type=float, default=0.0001,
            help="l2 norm coef")
    parser.add_argument("--relabel", default=False, action='store_true',
            help="remove untouched nodes and relabel")
    parser.add_argument("--use-self-loop", default=False, action='store_true',
            help="include self feature as a special relation")
    parser.add_argument("--use-infomax-loss", default=True, action='store_true',
                        help="use infomax task supervision")
    parser.add_argument("--use-reconstruction-loss", default=False, action='store_true',
                        help="use feature reconstruction task supervision")
    parser.add_argument("--node-masking", default=False, action='store_true',
                        help="mask a subset of node features")
    parser.add_argument("--loss-over-all-nodes", default=True, action='store_true',
                        help="compute the feature reconstruction loss over all nods or just the masked")
    parser.add_argument("--link-prediction", default=False, action='store_true',
                       help="use link prediction as supervision task")
    parser.add_argument("--mask-links", default=True, action='store_true',
                       help="mask the links to be predicted")
    parser.add_argument("--use-node-motifs", default=True, action='store_true',
                       help="use the node motifs")
    parser.add_argument("--batch-size", type=int, default=5000,
            help="Mini-batch size. If -1, use full graph training.")
    parser.add_argument("--model_path", type=str, default=None,
            help='path for save the model')
    parser.add_argument("--fanout", type=int, default=10,
            help="Fan-out of neighbor sampling.")
    parser.add_argument("--split", type=int, default=0,
                        help="split type.")
    fp = parser.add_mutually_exclusive_group(required=False)
    fp.add_argument('--validation', dest='validation', action='store_true')
    fp.add_argument('--testing', dest='validation', action='store_false')
    parser.set_defaults(validation=True)

    args = parser.parse_args(['--dataset', 'dblp_preprocessed','--encoder', 'RGCN'])
    print(args)
    args.bfs_level = args.n_layers + 1 # pruning used nodes for memory
    fit(args)

    '''
    # perform edge neighborhood sampling to generate training graph and data
    g, node_id, edge_type, node_norm, data, labels = \
        utils.generate_sampled_graph_and_labels(
            train_data, args.graph_batch_size, args.graph_split_size,
            num_rels, adj_list, degrees, args.negative_sample,
            args.edge_sampler)
    print("Done edge sampling")

    # set node/edge feature
    node_id = torch.from_numpy(node_id).view(-1, 1).long()
    edge_type = torch.from_numpy(edge_type)
    edge_norm = node_norm_to_edge_norm(g, torch.from_numpy(node_norm).view(-1, 1))
    data, labels = torch.from_numpy(data), torch.from_numpy(labels)
    deg = g.in_degrees(range(g.number_of_nodes())).float().view(-1, 1)
    if use_cuda:
        node_id, deg = node_id.cuda(), deg.cuda()
        edge_type, edge_norm = edge_type.cuda(), edge_norm.cuda()
        data, labels = data.cuda(), labels.cuda()
    '''