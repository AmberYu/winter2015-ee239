# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:36:05 2015
@author: duanhaiman
"""

import matplotlib.pyplot as plt
import datetime, time

##Extract the rate
rate=[]
elapse=[]
f=open('first_second_correlation.txt','r')
for line in f:
	data=line.split()
	rate.append(data[6])
	timefrom=datetime.datetime.fromtimestamp(float(data[0]).strftime('%H:%M:%S')
	elapse.append(timefrom)

##Draw the line 
ax=plt.subplot(111)
plt.xlabel('Time')
plt.ylabel('The rate')
plt.title('The Correlation Over Time')
plt.plot(rate)
ax.set_xticklabels(elapse,rotation=20, rotation_mode="anchor", ha="right")
plt.show()
