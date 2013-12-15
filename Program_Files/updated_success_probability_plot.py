'''
Created on Dec 15, 2013

Updates the success probability vs percent of goal earned plot from "success_probability_given_total_money.py" to make it more visually appealing.
Recall the two notable statistics:
At least 14% of goal earned --> >75% probability of success
At least 38% of goal earned --> >90% probability of success

@author: Macbook
'''

import numpy as np
import matplotlib.pyplot as plt
#from scipy import interpolate

if __name__ == '__main__':
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy")
    
    total_pledges = statuses[:,-1,1]
    
    ########################################################################################
    ############ PROBABILITY OF SUCCESS AS A FUNCTION OF PERCENT OF GOAL EARNED ############
    ########################################################################################
    
    num_successful_campaigns = len(np.where(total_pledges >= 1)[0]) # = 7739
    get_prob = lambda p: 1.0*num_successful_campaigns/len(np.where(total_pledges >= p)[0])
    
    fig = plt.figure()
    ax = plt.subplot(111)
    
    ## Smoothing with cubic splines:
    #x = np.linspace(0, 1, 51)
    #y = map(get_prob,x)
    #tck = interpolate.splrep(x,y)
    #x_new = np.linspace(0, 1, 201)
    #y_new = interpolate.splev(x_new,tck)
    #plt.fill_between(x_new, 0, y_new, alpha=0.5)
    
    ## Concentrate points near zero, where the slope is high:
    x1 = np.arange(0,.021,.001) #density on [0,2] = 10x
    x2 = np.arange(.0225,.04,.0025) #density on [2,4] = 4x
    x3 = np.arange(.04,1.02,.02) #density on [4,100] = .5x
    x = np.concatenate((x1,x2,x3))
    y = map(get_prob,x)
    plt.fill_between(x, 0, y, alpha=0.5)
    plt.grid(True)
    plt.title("Probability of Success vs Percent of Goal Earned")
    plt.xlabel("Percent of Goal Earned")
    plt.ylabel("Probability of Success")
    ax.set_xticks(np.linspace(0,1,11))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,110,10)])
    ax.set_ylim([.45,1])
    ax.set_yticks(np.linspace(.45,1,12))
    ax.set_yticklabels([str(percent)+'%' for percent in range(45,105,5)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/success_probability_vs_percent_goal_earned_new.png")