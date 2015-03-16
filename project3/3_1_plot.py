# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:07:53 2015

@author: duanhaiman
"""

"""
Plot "number of tweets in hour" over time for #SuperBowl and #NFL (a histogram with 1-hour bins).
"""

import matplotlib.pylab as plt
import json
import numpy as np
import datetime

def getTweets(filename):
    tweets = []
    firstpo_date = []
    tmlb=[]
    
    f=open(filename)
    for line in f:
        try: 
            tweets.append(json.loads(line))
        except:
            print "error when reading tweets.txt"
                    
                    
    #extract all the first post date into the list
    for i in range(len(tweets)):
        firstpo_date.append(tweets[i]['firstpost_date'])
        #transfer the time stamp into actual time
        timefrom=datetime.datetime.fromtimestamp(float(tweets[i]['firstpost_date'])).strftime('%H:%M:%S')
        #store the actual time into tmlb        
        tmlb.append(timefrom)

    hashtag=filename[7:-4]
    intvl=tmlb[::100]
    mintime = min(firstpo_date)
    maxtime = max(firstpo_date)
    num = len(firstpo_date)
    delta = maxtime - mintime

    print 'Mintime: ', mintime
    print 'Maxtime: ', maxtime

    period = delta / 3600
    if (maxtime - mintime) % 3600 != 0:
        period += 1
    
    tweetphour = np.zeros(period) #create a list to count the number   
    
    for j in range(num):
        for i in range(period):
            if firstpo_date[j]>=(mintime+i*3600) and firstpo_date[j]<=(mintime+(i+1)*3600):
                tweetphour[i] += 1 

    
    index = np.arange(len(tweetphour))
    
    ax=plt.subplot(111)    
    plt.bar(index,tweetphour)
    plt.xlabel('Time')
    plt.ylabel('Number of Tweets')
    plt.title('Number of Tweets Per Hour')
    ax.set_xticklabels(intvl,rotation=20, rotation_mode="anchor", ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()   
    
    return tweetphour
    f.close()

getTweets('tweets_#superbowl.txt')
getTweets('tweets_#nfl.txt')















