'''
Created on Dec 15, 2013

Updates the 250% histogram from "linear_total_money_histograms.py" to make it more visually appealing.
Recall that this histogram encompasses 95.0% (94.98%) of the data.
 
@author: Jonathan Simon
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy")
    
    total_pledges = statuses[:,-1,1] 
    total_campaigns = len(total_pledges) # = 16042
    
    #####################################################
    ############ LINEAR HISTOGRAM UP TO 250% ############
    #####################################################
    
    total_pledges_under_250 = total_pledges[np.where(total_pledges <= 2.5)[0]]
    
    fig = plt.figure(figsize=(10, 6))
    ax = plt.subplot(111)
    plt.hist(total_pledges_under_250, bins=np.linspace(0,2.5,51), alpha=0.75)
    plt.grid(True)
    plt.title("Relative Frequencies of Percent of Goal Earned (250% cutoff)")
    plt.xlabel("Percent of Goal Earned")
    plt.ylabel("Percent of Campaigns")
    ax.set_xticks(np.linspace(0,2.5,11))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,275,25)])
    ax.set_yticks(np.linspace(0,.28,8)*total_campaigns)
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,32,4)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/Linear_Histogram_250_new_2.png")