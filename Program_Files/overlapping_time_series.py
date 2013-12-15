'''
Created on Dec 15, 2013

Plot the time series of every campaign with a low transparency setting. More opaque regions will indicate higher overlap,
and thus a more common path for campaigns to take.

Load data array: ~5 seconds
Plot all 16000+ lines: ~36 seconds
Render and save the plot: ~15 seconds

Plotting all of the lines in advance would save a huge amount of time.
Try pickling them to make it easier to experiment with formatting.

Optimal plot settings found:
figure size - (8,8)
line width - 2
alpha - 1/100
 
@author: Jonathan Simon
'''

import numpy as np
import matplotlib.pyplot as plt
from time import time
import pickle

if __name__ == '__main__':
    start_time = time()
    
    #######################################################################
    ############ OVERLAPPING CAMPAIGN TRAJECTORY (SINGLE PLOT) ############
    #######################################################################
    
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy") #pledge_mat = statuses[:,:,1]
    print "Loading time:", time()-start_time
    
    #fig = plt.figure(figsize=(6,10))
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111)
    for i in range(statuses.shape[0]):
        plt.plot(statuses[i,:,0], statuses[i,:,1], color='b', alpha=.01, linewidth=2)
    plt.title("Campaign Trajectories Over Time")
    plt.xlabel("Fraction of Campaign Completed")
    plt.ylabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,1,11))
    ax.set_xticklabels(np.linspace(0,1,11))
    ax.set_ylim([0,1.75])
    ax.set_yticks(np.arange(0,2,.25))
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,200,25)])
    #ax.set_ylim([0,2.5])
    #ax.set_yticks(np.linspace(0,2.5,11))
    #ax.set_yticklabels([str(percent)+'%' for percent in range(0,275,25)])
    print "Plotting time:", time()-start_time
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/overlapping_campaign_trajectories_alpha100_2.png")
    print "Total time:", time()-start_time
    
    '''
    ###############################################################################
    ############ OVERLAPPING CAMPAIGN TRAJECTORY (SAVE MULTIPLE PLOTS) ############
    ###############################################################################
    
    ## Based on the example seen here:
    ## http://stackoverflow.com/questions/7290370/store-and-reload-matplotlib-pyplot-object
    
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy") #pledge_mat = statuses[:,:,1]
    print "Loading time:", time()-start_time
    
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot(111)
    
    plt.title("Campaign Trajectories Over Time")
    plt.xlabel("Fraction of Campaign Completed")
    plt.ylabel("Percent of Goal Earned")
    
    ax.set_xticks(np.linspace(0,1,11))
    ax.set_xticklabels(np.linspace(0,1,11))
    ax.set_ylim([0,2.5])
    ax.set_yticks(np.linspace(0,2.5,11))
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,275,25)])
    
    xy_list = []
    for i in range(statuses.shape[0]):
        xy_list.append(statuses[i,:,0]) 
        xy_list.append(statuses[i,:,1])
    plt.plot(*xy_list)
    
    pickle.dump(ax,file(data_folder+"/all_lines_plot.pkl",'w'))
    
    print "Plotting time:", time()-start_time
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/overlapping_campaign_trajectories_alpha100.png")
    print "Total time:", time()-start_time
    '''