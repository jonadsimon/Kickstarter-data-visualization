'''
Created on Dec 10, 2013

Save statuses as a npy instead of a pkl. The pkl takes up 3 times as much space, and takes ~50 times longer to load. 

@author: Jonathan Simon
'''

import cPickle
import numpy as np
from time import time

if __name__ == '__main__':
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    pkl_load_start = time()
    with open(data_folder + "/statuses.pkl", 'rb') as f:
        statuses = cPickle.load(f)
    print "cPickle load time:", time()-pkl_load_start
    statuses = np.array(statuses)
    
    np.save(data_folder+"/statuses.npy",statuses)
    
    del statuses #clear 'statuses' from memory, so it's not loaded in twice
    
    npy_load_start = time()
    statuses = np.load(data_folder+"/statuses.npy")
    print "Numpy load time:", time()-npy_load_start