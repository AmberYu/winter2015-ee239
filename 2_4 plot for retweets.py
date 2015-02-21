# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 13:01:42 2015

@author: duanhaiman
"""

##plot the line for the retweeted tweets

import matplotlib.pyplot as plt
f=open('retweet_num.txt','r')

twtnum=[]
k=[]

for line in f:
    data=line.split()
    k.append(data[3])
    twtnum.append(data[0])
   
x=map(int,k)
y=map(int,twtnum)

'''
plt.bar(x,y)
plt.title('The Number of Retweets in Linear Scale')
plt.xlabel('The Retweeted Time')
plt.ylabel('The Number of Retweeted Tweets')
plt.show()
'''

##plot in log-log scale

import math

z=map(float,twtnum)
n=map(float,k)
twtlog=[]
klog=[]
for i in z:
    twtlog.append(math.log10(i))

for i in n:    
    klog.append(math.log10(i))

plt.plot(klog,twtlog)
plt.title('The Number of Retweets in log-log Scale')
plt.xlabel('The Retweeted Time')
plt.ylabel('The Number of Retweeted Tweets')
plt.show()

f.close()






















