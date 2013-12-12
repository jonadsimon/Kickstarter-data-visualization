'''
Created on Dec 11, 2013

Given that you earned at least *% of your goal, what's the probability your campaign succeeded?
In other words: P(Success | >=*% earned) = P(Success AND >=*% earned) / P(>=*% earned) 
  
P(Success | >=50% earned) = 94.01%
P(Success | >=75% earned) = 97.66%
P(Success | >=90% earned) = 98.79%

CLEARLY BY THE TIME YOU GET TO 50%, THINGS HAVE ALREADY GOTTEN CRAZILY PROBABLY
INSTEAD, LET'S REVERSE OUR PROBLEM, AND LOOK FOR VALUES OF p RESULTING IN "SUPRISINGLY" HIGH PROBABILITIES
e.g. what value of p do we need to ensure > 50% success likelihood? (I know there are more failures than successes, so the answer must be >0%)

At least 14% of goal earned --> >75% probability of success
At least 38% of goal earned --> >90% probability of success 
 
@author: Jonathan Simon
'''

import numpy as np
import pylab

if __name__ == '__main__':
    data_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Input/kickstarter-etter-cosn2013"
    statuses = np.load(data_folder + "/statuses.npy")
    
    total_pledges = statuses[:,-1,1]
    #total_campaigns = len(total_pledges) # = 16042
    
    ####################################################################
    ############ IMPORTANT VALUES OF PERCENT OF GOAL EARNED ############
    ####################################################################
    
    over_50p_indices = np.where(total_pledges >= .5)[0] # len = 8081
    over_75p_indices = np.where(total_pledges >= .75)[0] # len = 7779
    over_90p_indices = np.where(total_pledges >= .9)[0] # len = 7690
    
    #NOTE: THESE THREE VALUES ARE NECESSARILY IDENTICAL 
    num_over_50_successes = len(np.where(total_pledges[over_50p_indices] >= 1)[0])
    num_over_75_successes = len(np.where(total_pledges[over_75p_indices] >= 1)[0])
    num_over_90_successes = len(np.where(total_pledges[over_90p_indices] >= 1)[0])
    
    print "Probability of success given >=50% of goal earned:", 1.0*num_over_50_successes/len(over_50p_indices)
    print "Probability of success given >=75% of goal earned:", 1.0*num_over_75_successes/len(over_75p_indices)
    print "Probability of success given >=90% of goal earned:", 1.0*num_over_90_successes/len(over_90p_indices)
    
    ########################################################################################
    ############ PROBABILITY OF SUCCESS AS A FUNCTION OF PERCENT OF GOAL EARNED ############
    ########################################################################################
    
    num_successful_campaigns = len(np.where(total_pledges >= 1)[0]) # = 7739
    get_prob = lambda p: 1.0*num_successful_campaigns/len(np.where(total_pledges >= p)[0])
    fig = pylab.figure()
    pylab.plot(np.linspace(0, 1, 201), map(get_prob,np.linspace(0, 1, 201)))
    ax = pylab.subplot(111)
    pylab.title("Probability of Success vs Percent of Goal Earned")
    pylab.xlabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,1,11))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,110,10)])
    pylab.ylabel("Probability of Success")
    ax.set_yticks(np.linspace(.4,1,13))
    ax.set_yticklabels([str(percent)+'%' for percent in range(40,105,5)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/success_probability_vs_percent_goal_earned.png")
    
    ################################################################################################################
    ############ PROBABILITY OF SUCCESS AS A FUNCTION OF PERCENT OF GOAL EARNED, WITH Y=X REGRESSED OUT ############
    ################################################################################################################
    
    #NOTE: In retrospect, I should have regressed out "y = .5*x + .5", but it doesn't really matter now anyway 
    num_successful_campaigns = len(np.where(total_pledges >= 1)[0]) # = 7739
    get_regressed_prob = lambda p: 1.0*num_successful_campaigns/len(np.where(total_pledges >= p)[0]) - p #this '-p' gives us the distance from the function y=x
    fig = pylab.figure()
    x_values = np.linspace(0, 1, 101)
    y_values = map(get_regressed_prob,x_values)
    pylab.plot(x_values, y_values)
    ax = pylab.subplot(111)
    pylab.title("Probability of Success vs Percent of Goal Earned (Regressed)")
    pylab.xlabel("Percent of Goal Earned")
    ax.set_xticks(np.linspace(0,1,11))
    ax.set_xticklabels([str(percent)+'%' for percent in range(0,110,10)])
    pylab.ylabel("Probability of Success (Regressed)")
    ax.set_yticks(np.linspace(0,.7,8))
    ax.set_yticklabels([str(percent)+'%' for percent in range(0,80,10)])
    
    output_folder = "/Users/Macbook/Desktop/Data Analysis Projects/Kickstart Monetary Flow Visualization/Output"
    fig.savefig(output_folder + "/success_probability_vs_percent_goal_earned_(regressed).png")
    
    #####################################################################
    ############ SURPRISING VALUES OF PERCENT OF GOAL EARNED ############
    #####################################################################
    
    max_deviation_idx = np.argmax(y_values)
    #"Most surprising value" (i.e. highest deviation from our expectation of y=x)
    print "Percent earned:", x_values[max_deviation_idx] # = 13%
    print "Probability of success:", x_values[max_deviation_idx] + y_values[max_deviation_idx] # = 74.60%
    
    num_successful_campaigns = len(np.where(total_pledges >= 1)[0]) # = 7739
    get_prob = lambda p: 1.0*num_successful_campaigns/len(np.where(total_pledges >= p)[0])
    for p in [.13,.14,.35,.36,.37,.38,.39,.40,.41,.42,.43,.44,.45]:
        print "Percent of goal earned:", p
        print "Probability of success:", get_prob(p)
        print
    