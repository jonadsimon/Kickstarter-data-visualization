'''
Created on Dec 11, 2013

Note: Try using something like color to indicate the goal amounts.
I expect these will be correlated with the normalized total pledge amounts.

Total number of campaigns: 16042

Percent of campaigns exceeding 200% of goal: 7.05%
Percent of campaigns exceeding 250% of goal: 5.02%
Percent of campaigns exceeding 300% of goal: 4.10%

@author: Jonathan Simon
'''

import numpy as np
import pylab as P

if __name__ == '__main__':
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy")
    
    total_pledges = statuses[:,-1,1] 
    total_campaigns = len(total_pledges) # = 16042
    #log_total_pledges = np.log10(total_pledges+1)
    
    print "Relative number of campaigns exceeding 200% goal:", 1.0*len(np.where(total_pledges > 2)[0])/len(total_pledges)
    print "Relative number of campaigns exceeding 250% goal:", 1.0*len(np.where(total_pledges > 2.5)[0])/len(total_pledges)
    print "Relative number of campaigns exceeding 300% goal:", 1.0*len(np.where(total_pledges > 3)[0])/len(total_pledges)
    
    #####################################################
    ############ LINEAR HISTOGRAM UP TO 200% ############
    #####################################################
    
    total_pledges_under_2 = total_pledges[np.where(total_pledges <= 2)[0]]
    
    fig = P.figure(figsize=(8, 6))
    ax = P.subplot(111)
    P.hist(total_pledges_under_2, bins=np.linspace(0,2,41))
    P.title("Relative Frequencies of Percent of Goal Earned (200% cutoff)")
    P.xlabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,2,9))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,225,25)])
    P.ylabel("Percent of Campaigns")
    ax.set_yticks(np.linspace(0,.28,8)*total_campaigns)
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,32,4)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/Linear_Histogram_200.png")
    
    #####################################################
    ############ LINEAR HISTOGRAM UP TO 250% ############
    #####################################################
    
    total_pledges_under_2 = total_pledges[np.where(total_pledges <= 2.5)[0]]
    
    fig = P.figure(figsize=(10, 6))
    ax = P.subplot(111)
    P.hist(total_pledges_under_2, bins=np.linspace(0,2.5,51))
    P.title("Relative Frequencies of Percent of Goal Earned (250% cutoff)")
    P.xlabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,2.5,11))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,275,25)])
    P.ylabel("Percent of Campaigns")
    ax.set_yticks(np.linspace(0,.28,8)*total_campaigns)
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,32,4)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/Linear_Histogram_250.png")
    
    #####################################################
    ############ LINEAR HISTOGRAM UP TO 300% ############
    #####################################################
    
    total_pledges_under_3 = total_pledges[np.where(total_pledges <= 3)[0]]
    
    fig = P.figure(figsize=(12, 6))
    ax = P.subplot(111)
    P.hist(total_pledges_under_3, bins=np.linspace(0,3,61))
    P.title("Relative Frequencies of Percent of Goal Earned (300% cutoff)")
    P.xlabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,3,13))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,325,25)])
    P.ylabel("Percent of Campaigns")
    ax.set_yticks(np.linspace(0,.28,8)*total_campaigns)
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,32,4)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/Linear_Histogram_300.png")
    