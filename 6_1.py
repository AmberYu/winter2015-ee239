# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:13:02 2015

@author: duanhaiman
"""

"""
Calculate for each hashtag:
average number of tweets per hour,
average number of followers of users posting the tweets, 
average number of retweets. 

Plot "number of tweets in hour" over time for #SuperBowl and #NFL (a histogram with 1-hour bins).
"""

import json

def part1(filename):
    tweets = []
    firstpo_date = []
    retweets = []
    followers = []
    
    for line in open(filename):
        try: 
            tweets.append(json.loads(line))
        except:
            print "error when reading tweets.txt"
            
            
    for i in range(len(tweets)):
        firstpo_date.append(tweets[i]['firstpost_date'])
        retweets.append(tweets[i]['tweet']['retweet_count'])
        followers.append(tweets[i]['tweet']['user']['followers_count'])
    
    
    tweetnum = len(tweets)
    mintime = min(firstpo_date)
    maxtime = max(firstpo_date)
    retweetlen = len(retweets)
    delta = maxtime - mintime
    avgtweets = float(tweetnum)*3600/float(delta)
    avgfollowers = sum(followers)/float(len(followers))
    avgretweets = float(sum(retweets))/float(retweetlen)
    
    
    print 'mintime: ', mintime
    print 'maxtime:', maxtime
    print 'The average number of tweets per hour: ', ('%.2f' % avgtweets)
    print 'The average number of followers of users posting the tweets: ', ('%.2f' % avgfollowers)
    print 'The average number of average number of retweets: ', ('%.2f' % avgretweets)

part1('tweets_#gopatriots.txt')











