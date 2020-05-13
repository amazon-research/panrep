import pickle
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from cycler import cycler

fontP = FontProperties()
fontP.set_size('small')
def panrep():
    def split_acc(acc):
        acc = float(acc.split(" ")[1].split("~")[0])
        return acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif, num_cluster, single_layer, num_motif_cluster) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [2, 15]

        for conf in sets[confs[0]]:
            for conf2 in sets[confs[1]]:
                legend += [paramlist[confs[0]] + ' : ' + str(conf) +
                           paramlist[confs[1]] + ' : ' + str(conf2)]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)]]
                plt.plot(x, y)
        plt.legend(legend, loc='center left', bbox_to_anchor=(0.1, 1.4))
        plt.show()

    paramlist = "n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,use_infomax_loss, mask_links, use_self_loop,use_node_motif, num_cluster, single_layer, num_motif_cluster"
    paramlist = paramlist.split(',')
    file = "2020-04-15-22:46:17.306660.pickle"

    results = pickle.load(open("results/" + file, 'rb'))
    plot_results(results, paramlist)
def panrep1rw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "2020-04-21-05:16:23.867440.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrep2rw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "2020-04-21-09:17:43.540173.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrep20samplesrw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "2020-04-22-04:45:26.040514.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrep1hoprw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "2020-04-23-04:12:44.109313.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrep10hoprw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "2020-04-23-08:34:55.969640.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrepimdbns10hoprw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-24-04:11:08.357247.pickle"

    results = pickle.load(open("results/panrep_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def panrepimdbns5hoprw():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-24-00:03:24.312803.pickle"

    results = pickle.load(open("results/panrep_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def panrepimdbns5hoprw5():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-24-01:03:59.187589.pickle"

    results = pickle.load(open("results/panrep_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def panrepimdbns5hoprw10():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-24-04:11:08.357247.pickle"

    results = pickle.load(open("results/panrep_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def panrepdblrw2ng1():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-23-12:40:42.006046.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)

def panrepdblrw1ng1():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-27-10:48:50.916881.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrepdblrw1ng5():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-28-08:03:11.512166.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrepdblrw2ng5():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-28-08:37:11.809010.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)
def panrepdblrw8ng5():
    def split_acc(acc):
        tacc = float(acc.split(" ")[1].split("t")[2])
        macro=float(acc.split(" ")[3].split("~")[0])
        return tacc,macro

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer,num_motif_cluster,
              use_meta_rw_loss) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            plots[key] = split_acc(results[key])

        count_confs = [len(conf) for conf in sets]
        plot_over = 0
        key = list(key)
        legend = []
        confs = [1, 15,2]
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]


    paramlist = "n_epochs, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot,MPRW"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-28-13:39:13.267177.pickle"

    results = pickle.load(open("results/panrep_node_classification//" + file, 'rb'))
    plot_results(results, paramlist)


def endtoend():
    def split_acc(acc):
        tes_acc = float(acc.split(" ")[2])
        endend_acc = float(acc.split(" ")[5].split("~")[0])
        return tes_acc,endend_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr,
             dropout, use_self_loop, K)= key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)
        legend = []
        confs = [8,2]
        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                   cycler('linestyle',
                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

        for conf in sets[confs[0]]:
            title=paramlist[confs[0]] + ' : ' + str(conf)
            legend=[]
            fig = plt.figure(num=i, figsize=(8, 6))
            for conf2 in sorted(sets[confs[1]]):
                legend+=[paramlist[confs[1]] + ' : ' + str(conf2)]
                #legend += [cur_legend]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][1]]
                plt.plot(x, y)

            plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2))
            plt.xlabel('Epochs')
            plt.ylabel('Macro-F1')
            plt.title(title)
            plt.show()
        for conf in sets[confs[0]]:
            title = paramlist[confs[0]] + ' : ' + str(conf)
            legend = []
            fig = plt.figure(num=i, figsize=(8, 6))
            for conf2 in sorted(sets[confs[1]]):
                legend += [paramlist[confs[1]] + ' : ' + str(conf2)]
                # legend += [cur_legend]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][0]]
                plt.plot(x, y)

            plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2))
            plt.xlabel('Epochs')
            plt.ylabel('Test Acc')
            plt.title(title +" direct RGCN classifier")
            plt.show()


    paramlist = "n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout, use_self_loop, K"
    paramlist = paramlist.split(',')
    file = "2020-04-16-01:57:06.865085.pickle"

    results = pickle.load(open("results/end_to_end_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def endtoenddifsplitsimdb():
    def split_acc(acc):
        tes_acc = float(acc.split(" ")[2])
        endend_acc = float(acc.split(" ")[5].split("~")[0])
        return tes_acc,endend_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs, n_layers, n_hidden, n_bases, fanout, lr,
             dropout, use_self_loop, splitpct,K)= key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)
        legend = []
        confs = [1,2,9]
        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                   cycler('linestyle',
                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

        for conf in sets[confs[0]]:
            title=paramlist[confs[0]] + ' : ' + str(conf)
            legend=[]
            fig = plt.figure(num=i, figsize=(8, 6))
            for conf2 in sorted(sets[confs[1]]):
                for conf3 in sorted(sets[confs[2]]):
                    legend+=[paramlist[confs[1]] + ' : ' + str(conf2)+paramlist[confs[2]] + ' : ' + str(conf3)]
                    #legend += [cur_legend]
                    y = []
                    key[confs[0]] = conf
                    key[confs[1]] = conf2
                    key[confs[2]] = conf3
                    x = sorted(sets[plot_over])
                    for el in x:
                        key[plot_over] = el
                        y += [plots[tuple(key)][1]]
                    plt.plot(x, y)

            plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3)
            plt.xlabel('Epochs')
            plt.ylabel('Macro-F1')
            plt.title(title)
            plt.show()
        for conf in sets[confs[0]]:
            title = paramlist[confs[0]] + ' : ' + str(conf)
            legend = []
            fig = plt.figure(num=i, figsize=(8, 6))
            for conf2 in sorted(sets[confs[1]]):
                for conf3 in sorted(sets[confs[2]]):
                    legend += [paramlist[confs[1]] + ' : ' + str(conf2) + paramlist[confs[2]] + ' : ' + str(conf3)]
                    # legend += [cur_legend]
                    y = []
                    key[confs[0]] = conf
                    key[confs[1]] = conf2
                    key[confs[2]] = conf3
                    x = sorted(sets[plot_over])
                    for el in x:
                        key[plot_over] = el
                        y += [plots[tuple(key)][0]]
                    plt.plot(x, y)
            plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3)
            plt.xlabel('Epochs')
            plt.ylabel('Test Acc')
            plt.title(title +" direct RGCN classifier")
            plt.show()


    paramlist = "n_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout, use_self_loop, splitpct, K"
    paramlist = paramlist.split(',')
    files=["2020-05-08-22:27:10.737286.pickle","2020-05-08-21:51:46.700476.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/end_to_end_node_classification/" + f, 'rb'))
        plot_results(results, paramlist)
def endtoenddifLPsplitsimdb():
    def split_acc(acc):
        #tes_acc = float(acc.split(" ")[2])
        endend_acc = float(acc.split(" ")[7].split("\n")[0])
        return endend_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_self_loop,k_fold, ng_rate,test_edge_split)= key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)
        legend = []
        confs = [10,2,1]
        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                   cycler('linestyle',
                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

        for conf in sets[confs[0]]:
            title = paramlist[confs[0]] + ' : ' + str(conf)
            legend = []
            fig = plt.figure(num=i, figsize=(8, 6))
            for conf2 in sorted(sets[confs[1]]):
                for conf3 in sorted(sets[confs[2]]):
                    legend += [paramlist[confs[1]] + ' : ' + str(conf2) + paramlist[confs[2]] + ' : ' + str(conf3)]
                    # legend += [cur_legend]
                    y = []
                    key[confs[0]] = conf
                    key[confs[1]] = conf2
                    key[confs[2]] = conf3
                    x = sorted(sets[plot_over])
                    for el in x:
                        key[plot_over] = el
                        y += [plots[tuple(key)]]
                    plt.plot(x, y)
            plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3)
            plt.xlabel('Epochs')
            plt.ylabel('Test Acc')
            plt.title(title +" direct RGCN classifier")
            plt.show()


    paramlist = "n_epochs,n_layers, n_hidden, n_bases, fanout, lr, dropout," \
                "use_self_loop,k_fold, ng_rate,test_edge_split"
    paramlist = paramlist.split(',')
    files=["imdb_preprocessed-2020-05-09-08:26:26.236531.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/end_to_end_link_prediction/" + f, 'rb'))
        plot_results(results, paramlist)





def finetune():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [1, 3,9,10,13,17]
        sets[3] = set([300])
        sets[1] = set([20])
        experiment=[n_layers]
        i=0
        for conf6 in sets[confs[5]]:

            for conf in sets[confs[0]]:


                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[5]] + \
                                 ' : ' + str(conf6) + paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:

                        for conf4 in sets[confs[3]]:

                            for conf5 in sets[confs[4]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    cur_legend += paramlist[confs[3]] + ':' + str(conf4)
                                    cur_legend += paramlist[confs[4]] + ':' + str(conf5)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    key[confs[4]] = conf5
                                    key[confs[5]] = conf6

                                    x = sorted(sets[plot_over])

                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][0]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]
                                    legend+=["PR-FT" +cur_legend]
                                    y=[]
                                    for el in x:
                                        key[plot_over] = el
                                        y += [plots[tuple(key)][2]]
                                    plt.plot(x, y)

                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]
        for conf6 in sets[confs[5]]:

            for conf in sets[confs[0]]:

                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[5]] + \
                                 ' : ' + str(conf6) + paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i += 1
                    fig = plt.figure(num=i, figsize=(8, 6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':',
                                                       '-.'])))

                    # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:

                        for conf4 in sets[confs[3]]:

                            for conf5 in sets[confs[4]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ':' + str(conf3)
                                cur_legend += paramlist[confs[3]] + ':' + str(conf4)
                                cur_legend += paramlist[confs[4]] + ':' + str(conf5)
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                key[confs[4]] = conf5
                                key[confs[5]] = conf6

                                x = sorted(sets[plot_over])

                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += ["MLP" + cur_legend]
                                #legend += ["PR-FT" + cur_legend]
                                y = []

                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3, prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Test acc')

                    plt.title(experiment)
                    plt.show()
                    legend = []

        '''
        for conf in sets[confs[0]]:
            cur_legend=paramlist[confs[0]] + ' : ' + str(conf)
            for conf2 in sets[confs[1]]:
                cur_legend+=paramlist[confs[1]] + ' : ' + str(conf2)
                #legend += [cur_legend]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                legend+=["MLP classifier"]
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][1]]
                plt.plot(x, y)

        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.1))
        plt.xlabel('Epochs')
        plt.ylabel('Macro-F1')
        plt.title(experiment)
        plt.show()
        '''

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot"
    paramlist = paramlist.split(',')
    file = "2020-04-18-15:45:02.991956.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetune1():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [10,13,14]
        #sets[3] = set([300])
        #sets[1] = set([20])
        experiment=[n_layers]
        i=0
        for conf in sets[confs[0]]:
                for conf2 in sets[confs[1]]:
                    experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                                     confs[1]] + ' : ' + str(conf2)

                    legend = []
                    i+=1
                    fig=plt.figure(num=i,figsize=(8,6))
                    plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                            cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                    #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                    for conf3 in sets[confs[2]]:
                                    skip_this=False
                                    cur_legend =  paramlist[confs[2]] + ':' + str(conf3)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3

                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this=True
                                            break
                                        y += [plots[tuple(key)][0]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR" + cur_legend]


                    plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3,prop=fontP)
                    plt.xlabel('Epochs')
                    plt.ylabel('Macro-F1')

                    plt.title(experiment)
                    plt.show()
                    legend=[]

        for conf in sets[confs[0]]:
            for conf2 in sets[confs[1]]:
                experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                    confs[1]] + ' : ' + str(conf2)

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf3 in sets[confs[2]]:
                    skip_this = False
                    cur_legend = paramlist[confs[2]] + ':' + str(conf3)
                    y = []
                    key[confs[0]] = conf
                    key[confs[1]] = conf2
                    key[confs[2]] = conf3

                    x = sorted(sets[plot_over])
                    for el in x:
                        key[plot_over] = el
                        if tuple(key) not in plots:
                            skip_this = True
                            break
                        y += [plots[tuple(key)][2]]
                    if skip_this:
                        break
                    plt.plot(x, y)
                    legend += ["PR-FT" + cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')

                plt.title(experiment)
                plt.show()
                legend = []

        for conf in sets[confs[0]]:
            for conf2 in sets[confs[1]]:
                experiment = paramlist[confs[0]] + ' : ' + str(conf) + paramlist[
                    confs[1]] + ' : ' + str(conf2)

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf3 in sets[confs[2]]:
                    skip_this = False
                    cur_legend = paramlist[confs[2]] + ':' + str(conf3)
                    y = []
                    key[confs[0]] = conf
                    key[confs[1]] = conf2
                    key[confs[2]] = conf3

                    x = sorted(sets[plot_over])
                    for el in x:
                        key[plot_over] = el
                        if tuple(key) not in plots:
                            skip_this = True
                            break
                        y += [plots[tuple(key)][1]]
                    if skip_this:
                        break
                    plt.plot(x, y)
                    legend += ["MLP" + cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title(experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, num_motif_clus,k_shot"
    paramlist = paramlist.split(',')
    file = "2020-04-21-12:30:56.276397.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetunemotif_basednowarmstart():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [9,10,16,17]
        #sets[1] = set([20])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-28-08:25:01.108195.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetunemotif_basedwarmstart10():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [9,10,16,17]
        #sets[1] = set([20])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-28-08:25:06.196346.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetunewrw():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [9,10,13,3]
        #sets[1] = set([20])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)

                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf3 in sets[confs[2]]:
                            for conf in sets[confs[0]]:
                                for conf2 in sets[confs[1]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot,rw"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-29-19:42:13.437127.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetunedblp():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [9,10,13,3,2]
        sets[2] = set([3])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
            for conf5 in sets[confs[4]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)+\
                                     paramlist[confs[4]] + ' : ' + str(conf5)
                        key[confs[4]] = conf5

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]


                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        key[confs[4]] = conf5
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot"
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-04-29-20:02:31.180729.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetuneimdblp15nr():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [3,9,10,13,2]
        #sets[2] = set([3])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
            for conf5 in sets[confs[4]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)+\
                                     paramlist[confs[4]] + ' : ' + str(conf5)
                        key[confs[4]] = conf5

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]


                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        key[confs[4]] = conf5
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot,rw"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-30-06:06:01.491382.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def finetuneimdblp5nr():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [3,9,10,13,2]
        #sets[2] = set([3])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
            for conf5 in sets[confs[4]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)+\
                                     paramlist[confs[4]] + ' : ' + str(conf5)
                        key[confs[4]] = conf5

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]


                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        key[confs[4]] = conf5
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot,rw"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-30-06:05:08.050278.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetuneimdblp2nr():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [3,9,10,13,2]
        #sets[2] = set([3])
        experiment=[n_layers]
        i=0
        for conf4 in sets[confs[3]]:
            for conf5 in sets[confs[4]]:
                        experiment = paramlist[confs[3]] + ' : ' + str(conf4)+\
                                     paramlist[confs[4]] + ' : ' + str(conf5)
                        key[confs[4]] = conf5

                        legend = []
                        i+=1
                        fig=plt.figure(num=i,figsize=(8,6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                cycler('linestyle', ['-', '--', ':', '-.','-', '--', ':', '-.','-', '--', ':', '-.'])))

                        #fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                        skip_this=False
                                        cur_legend =  paramlist[confs[2]] + ':' + str(conf3)+ paramlist[confs[0]]+' : ' + str(conf) +  paramlist[
                                         confs[1]] + ' : ' + str(conf2)
                                        y = []
                                        key[confs[0]] = conf
                                        key[confs[1]] = conf2
                                        key[confs[2]] = conf3
                                        key[confs[3]] = conf4
                                        x = sorted(sets[plot_over])
                                        for el in x:
                                            key[plot_over] = el
                                            if tuple(key) not in plots:
                                                skip_this=True
                                                break
                                            y += [plots[tuple(key)][0]]
                                        if skip_this:
                                            break
                                        plt.plot(x, y)
                                        legend += ["PR" + cur_legend]


                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3,prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend=[]


                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                               cycler('linestyle',
                                                      ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) + paramlist[confs[0]]+' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)
                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][2]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["PR-FT" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Macro-F1')

                        plt.title(experiment)
                        plt.show()
                        legend = []

                        key[confs[4]] = conf5
                        legend = []
                        i += 1
                        fig = plt.figure(num=i, figsize=(8, 6))
                        plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                                   cycler('linestyle',
                                                          ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                        # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                        for conf in sets[confs[0]]:
                            for conf2 in sets[confs[1]]:
                                for conf3 in sets[confs[2]]:
                                    skip_this = False
                                    cur_legend = paramlist[confs[2]] + ':' + str(conf3) +paramlist[confs[0]]+ ' : ' + str(conf) + paramlist[
                                        confs[1]] + ' : ' + str(conf2)

                                    y = []
                                    key[confs[0]] = conf
                                    key[confs[1]] = conf2
                                    key[confs[2]] = conf3
                                    key[confs[3]] = conf4
                                    x = sorted(sets[plot_over])
                                    for el in x:
                                        key[plot_over] = el
                                        if tuple(key) not in plots:
                                            skip_this = True
                                            break
                                        y += [plots[tuple(key)][1]]
                                    if skip_this:
                                        break
                                    plt.plot(x, y)
                                    legend += ["MLP" + cur_legend]
                        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                        plt.xlabel('Epochs')
                        plt.ylabel('Test Acc')

                        plt.title(experiment)
                        plt.show()
                        legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links, use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot,rw"
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-04-30-17:48:55.040204.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def finetune2():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)
        legend = []
        confs = [2, 15]
        experiment=[n_fine_tune_epochs, n_layers, n_hidden]
        experiment=str(experiment)

        for conf in sets[confs[0]]:
            cur_legend=paramlist[confs[0]] + ' : ' + str(conf)
            for conf2 in sets[confs[1]]:
                cur_legend+=paramlist[confs[1]] + ' : ' + str(conf2)
                #legend += [cur_legend]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                legend+=["PanRepMI"]
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][0]]
                plt.plot(x, y)
                legend+=["PanRepMI+ Finetune"]
                y=[]
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][2]]
                plt.plot(x, y)

        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.1))
        plt.xlabel('Epochs')
        plt.ylabel('Macro-F1')
        plt.title(experiment)
        plt.show()
        legend=[]
        for conf in sets[confs[0]]:
            cur_legend=paramlist[confs[0]] + ' : ' + str(conf)
            for conf2 in sets[confs[1]]:
                cur_legend+=paramlist[confs[1]] + ' : ' + str(conf2)
                #legend += [cur_legend]
                y = []
                key[confs[0]] = conf
                key[confs[1]] = conf2
                x = sorted(sets[plot_over])
                legend+=["MLP classifier"]
                for el in x:
                    key[plot_over] = el
                    y += [plots[tuple(key)][1]]
                plt.plot(x, y)

        plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.1))
        plt.xlabel('Epochs')
        plt.ylabel('Macro-F1')
        plt.title(experiment)
        plt.show()


    paramlist = "n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout, use_link_prediction, use_reconstruction_loss, use_infomax_loss, mask_links, use_self_loop, use_node_motif,num_cluster,single_layer, motif_cluster,k_shot"
    paramlist = paramlist.split(',')
    file = "2020-04-15-23:20:15.052926.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)

def finetunedblpsmallrw():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [18,9, 10, 13,3, 2]
        sets[6] = set([0.001])
        sets[2] = set([2])
        sets[3] = set([150])
        key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('rbgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw  "
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-05-01-10:27:33.202339.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetunedblplargerw():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        return panrep_acc,tes_acc,finpanrep_acc

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [18,9, 10, 13,3, 2]
        #sets[6] = set([0.001])
        sets[2] = set([2])
        #sets[3] = set([150])
        key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('gbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-',':', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('gbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', ':', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':',
                                                   '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('gbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['-', ':', '--', ':', '-.', '-', '--', ':', '-.', '-', '--', ':',
                                                   '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw  "
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-05-02-23:04:46.626591.pickle"

    results = pickle.load(open("results/finetune_node_classification/" + file, 'rb'))
    plot_results(results, paramlist)
def finetuneimdb_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        if acc.split(" ")[50].split('\n')[0]=='Logits:':
            mrr=0
        else:
            mrr=float(acc.split(" ")[50].split('\n')[0])
        return panrep_acc,tes_acc,finpanrep_acc,mrr

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw,ng_rate) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [18,9, 10, 13,3, 8]
        #sets[6] = set([0.001])
        #sets[2] = set([2])
        #sets[3] = set([150])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate  "
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-05-02-23:04:56.799430.pickle"

    results = pickle.load(open("results/universal_task/" + file, 'rb'))
    plot_results(results, paramlist)

def finetuneimdb_morefintepochs_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        if acc.split(" ")[50].split('\n')[0]=='Logits:':
            mrr=0
        else:
            mrr=float(acc.split(" ")[50].split('\n')[0])
        return panrep_acc,tes_acc,finpanrep_acc,mrr

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw,ng_rate) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [18,9, 10, 13,3, 1]
        #sets[6] = set([0.001])
        #sets[2] = set([2])
        #sets[3] = set([150])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate  "
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-05-04-08:37:06.795527.pickle"

    results = pickle.load(open("results/universal_task/" + file, 'rb'))
    plot_results(results, paramlist)

def finetuneimdb_tunefin_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])
        lp_mrr = float(acc.split(" ")[58].split('\n')[0])
        return panrep_acc,tes_acc,finpanrep_acc,mrr,lp_mrr

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw,ng_rate) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [15,7, 10, 13,3, 2]
        #sets[6] = set([0.001])
        #sets[2] = set([2])
        #sets[3] = set([150])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, n_layers, n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate  "
    paramlist = paramlist.split(',')
    file = "imdb_preprocessed-2020-05-06-03:54:37.400400.pickle"

    results = pickle.load(open("results/universal_task/" + file, 'rb'))
    plot_results(results, paramlist)

def finetuneimdb_tune_ssl_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])
        lp_mrr = float(acc.split(" ")[58].split('\n')[0])
        lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
        entropy =float(acc.split(" ")[90])
        mlp_acc_pr=float(acc.split(" ")[95])
        mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [2, 12,7, 20,3, 5]
        sets[7] = set([0.1])
        #sets[2] = set([1])
        #sets[1] = set([100])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, use_link_prediction, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-07-09:30:14.936903.pickle","imdb_preprocessed-2020-05-07-09:48:19.609264.pickle",
    "imdb_preprocessed-2020-05-07-10:07:46.243617.pickle","imdb_preprocessed-2020-05-07-10:42:25.997116.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_tune_sslsmal_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])
        lp_mrr = float(acc.split(" ")[58].split('\n')[0])
        lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
        entropy =float(acc.split(" ")[90])
        mlp_acc_pr=float(acc.split(" ")[95])
        mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 3
        key = list(key)

        confs = [0,2,1, 12,7, 20]
        #sets[2] = set([1])
        #sets[1] = set([100])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, use_link_prediction, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-07-22:15:34.465754.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_tune_small_across_panrep_configurations():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0,3,2, 8,10, 20]
        #sets[2] = set([1])
        #sets[1] = set([100])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-08-01:01:00.833871.pickle",
           "imdb_preprocessed-2020-05-08-01:29:22.172781.pickle",
           "imdb_preprocessed-2020-05-08-01:36:02.945222.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
# small drop in performance but still relative good even when learning the rel
def finetuneimdb_tune_learning_rel_embedding():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])

        entropy =float(acc.split(" ")[71])
        mlp_acc_pr=float(acc.split(" ")[76])
        mlp_acc_prft=float(acc.split(" ")[81])
        return panrep_acc,prft_tes_acc,finpanrep_acc,entropy,mlp_acc_pr,mlp_acc_prft

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [1,3,2, 8,10, 20]
        #sets[2] = set([1])
        #sets[1] = set([100])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                #plt.ylim(bottom=0.4)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-08-01:53:33.556326.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)


def finetuneimdb_small_no_init():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        sets[0] = set([800,900])
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-08-02:10:59.182465.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)

def finetuneimdb_adjusted_learning_rate_to_base_layers():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-08-02:20:51.728115.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_adjusted_large_scale_learning_rate_to_base_layers():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-08-13:55:13.417213.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_adjlr_diftrain_4split():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-09-03:15:03.913886.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_adjlr_diftrain_2split():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-09-03:50:26.802202.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_adjlr_diftrain_05split():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-09-09:06:40.928088.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_infomax():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 1
        key = list(key)

        confs = [0, 3, 10, 8, 7, 20]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-09-17:46:56.761579.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)

def finetuneimdb_dif_edge_splits_dif_lr():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])

        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
            finlogpanrep_acc = float(acc.split(" ")[65].split("~")[0])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
            finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl,test_edge_split) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [1, 3, 2, 7, 8, 21]
        # sets[1] = set([100])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl,split_pct "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-10-09:32:08.357661.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_dif_edge_splits():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])

        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
            finlogpanrep_acc = float(acc.split(" ")[65].split("~")[0])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
            finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl,test_edge_split) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 21
        key = list(key)

        confs = [1, 3, 2, 7, 8, 4]
        sets[0] = set([800])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl,split_pct "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-10-10:18:08.620973.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)
def finetuneimdb_dif_supervisions():

    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        prft_tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])

        mrr = float(acc.split(" ")[51].split('\n')[0])

        if acc.split(" ")[56]=='LPFT':
            lp_mrr = 0
            lpft_mrr = float(acc.split(" ")[58].split('\n')[0])
            entropy =float(acc.split(" ")[83])
            mlp_acc_pr=float(acc.split(" ")[88])
            mlp_acc_prft=float(acc.split(" ")[93])
            finlogpanrep_acc = float(acc.split(" ")[65].split("~")[0])
        else:
            lp_mrr = float(acc.split(" ")[58].split('\n')[0])
            lpft_mrr = float(acc.split(" ")[65].split('\n')[0])
            entropy =float(acc.split(" ")[90])
            mlp_acc_pr=float(acc.split(" ")[95])
            mlp_acc_prft=float(acc.split(" ")[100])
            finlogpanrep_acc = float(acc.split(" ")[72].split("~")[0])
        return panrep_acc,prft_tes_acc,finpanrep_acc,mrr,lp_mrr,lpft_mrr,entropy,mlp_acc_pr,mlp_acc_prft,finlogpanrep_acc
    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw, ng_rate,only_ssl,test_edge_split) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])
            if len(results[key])>0:
                plots[key] = split_acc(results[key])

        plot_over = 21
        key = list(key)

        confs = [8,9,10, 13, 18, 4]
        sets[0] = set([800])
        # key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR " + experiment)
                plt.show()
                legend = []
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][9]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT Log" + experiment)
                plt.show()

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Macro-F1')
                # plt.ylim(bottom=0.4)
                plt.title("PR-FT " + experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Test Acc')

                plt.title("MLP " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][4]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep-LP module" + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][5]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('MRR')

                plt.title("PanRep LP-FT " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][7]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr " + experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][8]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel(paramlist[plot_over])
                plt.ylabel('Acc')

                plt.title("MLP acc of pr-ft" + experiment)
                plt.show()

    paramlist = "n_epochs,n_ft_ep, L, n_h, n_b, fanout, lr, dr, LP, R, I, mask_links," \
                " self_loop , M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate, ssl,split_pct "
    paramlist = paramlist.split(',')

    files=["imdb_preprocessed-2020-05-10-07:42:54.021860.pickle"]
    for f in files:
    #file = "imdb_preprocessed-2020-05-07-09:30:14.936903.pickle"

        results = pickle.load(open("results/universal_task/" + f, 'rb'))
        plot_results(results, paramlist)

def finetunedblp_univ():
    def split_acc(acc):
        panrep_acc = float(acc.split(" ")[4].split("~")[0])
        tes_acc = float(acc.split(" ")[24])
        finpanrep_acc = float(acc.split(" ")[30].split("~")[0])
        if acc.split(" ")[50].split('\n')[0]=='Logits:':
            mrr=0
        else:
            mrr=float(acc.split(" ")[50].split('\n')[0])
        return panrep_acc,tes_acc,finpanrep_acc,mrr

    def plot_results(results, paramlist):
        plots = {}
        elems = list(results.keys())[0]
        sets = []
        for el in list(elems):
            sets += [set()]
        keys = list(results.keys())
        experiment = keys[-1]
        keys = keys[:-1]
        for key in keys:
            (n_epochs,n_fine_tune_epochs, n_layers, n_hidden, n_bases, fanout, lr, dropout,
             use_link_prediction, use_reconstruction_loss,
             use_infomax_loss, mask_links, use_self_loop,
             use_node_motif,num_cluster,single_layer,motif_cluster,k_fold,rw,ng_rate) = key
            for i in range(len(list(key))):
                sets[i].add(key[i])

            plots[key] = split_acc(results[key])

        plot_over = 0
        key = list(key)

        confs = [18,9, 10, 13,3, 8]
        #sets[6] = set([0.001])
        #sets[2] = set([2])
        #sets[3] = set([150])
        #key[6]=0.001
        experiment = [n_layers]
        i = 0
        for conf6 in sets[confs[5]]:
            for conf5 in sets[confs[4]]:
                experiment = paramlist[confs[5]] + ' : ' + str(conf6) + \
                             paramlist[confs[4]] + ' : ' + str(conf5)
                key[confs[4]] = conf5
                key[confs[5]] = conf6
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][0]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]

                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))
                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][2]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Macro-F1')
                plt.ylim(bottom=0.6)
                plt.title("PR-FT " +experiment)
                plt.show()
                legend = []

                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.','-',':',  '-','--', '-',':', ':', '-.', '-', '--', ':', '-.', '-', '--', ':', '-.'])))

                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2))+ paramlist[confs[3]] +\
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][1]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [ cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('Test Acc')

                plt.title("MLP " +experiment)
                plt.show()
                legend = []
                i += 1
                fig = plt.figure(num=i, figsize=(8, 6))
                plt.rc('axes', prop_cycle=(cycler('color', list('kcbgyrgbrgykcmygbcg')) +
                                           cycler('linestyle',
                                                  ['--', ':', '-.', '-', ':', '-', '--', '-', ':', ':', '-.', '-', '--',
                                                   ':', '-.', '-', '--', ':', '-.'])))
                # fig.set_prop_cycle('color', plt.cm.Spectral(np.linspace(0, 1, 30)))

                for conf in sets[confs[0]]:
                    for conf2 in sets[confs[1]]:
                        for conf3 in sets[confs[2]]:
                            for conf4 in sets[confs[3]]:
                                skip_this = False
                                cur_legend = paramlist[confs[2]] + ' : ' + str(float(conf3)) + paramlist[
                                    confs[0]] + ' : ' + str(
                                    int(conf)) + paramlist[confs[1]] + ' : ' + str(float(conf2)) + paramlist[confs[3]] + \
                                             ' : ' + str(float(conf4))
                                y = []
                                key[confs[0]] = conf
                                key[confs[1]] = conf2
                                key[confs[2]] = conf3
                                key[confs[3]] = conf4
                                x = sorted(sets[plot_over])
                                for el in x:
                                    key[plot_over] = el
                                    if tuple(key) not in plots:
                                        skip_this = True
                                        break
                                    y += [plots[tuple(key)][3]]
                                if skip_this:
                                    break
                                plt.plot(x, y)
                                legend += [cur_legend]
                plt.legend(legend, loc='center left', bbox_to_anchor=(-0.1, 1.2), ncol=3, prop=fontP)
                plt.xlabel('Epochs')
                plt.ylabel('MRR')

                plt.title("PanRep " + experiment)
                plt.show()
                legend = []

    paramlist = "n_epochs,n_ft_ep, L , n_h, n_b, fanout, lr, dropout, use_link_prediction, R, I, mask_links," \
                " use_self_loop, M,num_cluster,single_layer, n_mt_cls,k_shot, rw, ng_rate  "
    paramlist = paramlist.split(',')
    file = "dblp_preprocessed-2020-05-04-13:29:39.020451.pickle"

    results = pickle.load(open("results/universal_task/" + file, 'rb'))
    plot_results(results, paramlist)

if __name__ == '__main__':
    #finetunedblpsmallrw()
    #finetunedblplargerw()
    #finetuneimdb_univ()#_morefintepochs_univ()
    #finetunedblp_univ()
    #finetuneimdb_adjusted_large_scale_learning_rate_to_base_layers()
    #finetuneimdb_dif_edge_splits_dif_lr()
    finetuneimdb_dif_supervisions()