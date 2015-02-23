# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:36:05 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt
import datetime,time

##Extract the rate
f=open('first_second_correlation.txt','r')
rate1=[]
rate2=[]
rate=[]
elapse=[]

for line in f:
    data=line.split()
    rate1.append(float(data[2]))
    rate2.append(float(data[4]))
    rate.append(float(data[6]))
    timefrom=time.strftime("%H:%M:%S",time.localtime(float(data[0])))
    elapse.append(timefrom)

    
##The first pic
plt.figure(1)
plt.xlabel('Tweeting rate of #Patriots')
plt.ylabel('Tweeting rate of #SuperBowlXLIX')
plt.title('The Correlation Between The Tags')
plt.plot(rate2,rate1,'o')

##The second one
plt.figure(2)
ax=plt.subplot(111)
plt.xlabel('Time')
plt.ylabel('The Tweeting Rate of Tag1/Tag2')
plt.title('The Correlation Between The Tags Over Time')
ax.set_xticklabels(elapse,rotation=20, rotation_mode="anchor", ha="right")
plt.plot(rate)

plt.show()









