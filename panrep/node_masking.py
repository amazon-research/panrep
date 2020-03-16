import random
import copy
import torch
import numpy as np
import time
def node_masker(old_g, num_nodes, masked_node_types):
    masked_nodes={}
    g=old_g.local_var()
    for ntype in g.ntypes:
        mnnodes=num_nodes
        if ntype not in masked_node_types:
            if mnnodes>g.nodes[ntype].data['features'].shape[0]:
                mnnodes=g.nodes[ntype].data['features'].shape[0]//3
            masked_ids = np.random.choice(g.number_of_nodes(ntype), size=mnnodes, replace=False)

            masked_nodes[ntype]=masked_ids
            g.nodes[ntype].data['masked_values'] = copy.deepcopy(g.nodes[ntype].data['features'])
            new_val=torch.zeros((mnnodes,g.nodes[ntype].data['features'].shape[1]))
            if g.nodes[ntype].data['features'].is_cuda:
                new_val=new_val.cuda()
            g.nodes[ntype].data['features'][masked_ids,:] = new_val

    return masked_nodes,g


def unmask_nodes(g,masked_node_types):
    for ntype in g.ntypes:
        if ntype not in masked_node_types:
                g.nodes[ntype].data['features']=g.nodes[ntype].data['masked_values']
    return g