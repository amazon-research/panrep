import torch
import numpy as np

def create_edge_mask(old_g,use_cude):
    g=old_g.local_var()
    for etype in g.etypes:
        if use_cude:
            g.edges[etype].data['mask']=torch.tensor(np.ones((g.number_of_edges(etype))),dtype=torch.float32).cuda()
        else:
            g.edges[etype].data['mask'] = torch.tensor(np.ones((g.number_of_edges(etype))),dtype=torch.float32)
    return g

def negative_sampling(pos_samples_d, num_entity_s_d,num_entity_o_d, negative_rate):
    labels_d={}
    samples_d={}
    for e in pos_samples_d.keys():
        pos_samples=pos_samples_d[e].transpose()
        num_entity_o=num_entity_o_d[e]
        num_entity_s=num_entity_s_d[e]
        size_of_batch = len(pos_samples)
        num_to_generate = size_of_batch * negative_rate
        neg_samples = np.tile(pos_samples, (negative_rate, 1))
        labels = np.zeros(size_of_batch * (negative_rate + 1), dtype=np.float32)
        labels[: size_of_batch] = 1
        values_s = np.random.randint(num_entity_s, size=num_to_generate)
        values_o = np.random.randint(num_entity_o, size=num_to_generate)
        choices = np.random.uniform(size=num_to_generate)
        subj = choices > 0.5
        obj = choices <= 0.5
        neg_samples[subj, 0] = values_s[subj]
        neg_samples[obj, 1] = values_o[obj]
        samples_d[e] = np.concatenate((pos_samples, neg_samples))
        labels_d[e] = labels

    return samples_d, labels_d




def hetero_edge_masker_sampler(old_g, num_sampled_edges, negative_rate,edge_masking):
    '''
    This function masks some edges at random by setting the mask attribute to 0
    :param old_g: The original graph
    :param num_sampled_edges: The nbr of edges to sample
    :param negative_rate: The nbr of negative samples per edge
    :param edge_masking: Whether to mask the sampled edges or not
    :return: The altered graph, the positive and the negative samples.
    '''
    pos_samples = {}
    neg_samples = {}
    num_entity_s = {}
    num_entity_o = {}
    g = old_g.local_var()
    for etype in g.etypes:
        pos_samples[etype]=[]
        u,v,eid=g.all_edges(form='all', etype=etype)
        if len(eid)//3 <= num_sampled_edges:
            lnum_sampled_edges = len(eid)//3
        else:
            lnum_sampled_edges = num_sampled_edges
        sampl_ids=np.random.choice(g.number_of_edges(etype),size=lnum_sampled_edges,replace=False)
        pos_samples[etype]=np.stack((u[sampl_ids],v[sampl_ids]))
        sampled_edges=eid[sampl_ids]
        num_entity_s[etype]=max(u)
        num_entity_o[etype]=max(v)
        # mask edges
        if edge_masking:
            g.edges[etype].data['mask'][sampled_edges] = 0
    # TODO negative samples
    samples_d,labels_d=negative_sampling(pos_samples, num_entity_s, num_entity_o, negative_rate)


    # create function consuming pos
    return g,samples_d,labels_d