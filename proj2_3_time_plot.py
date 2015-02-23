# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 12:50:31 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt
import datetime


f=open('numbers_persecond_SuperBowlXLIX.txt','r')
tm=[]
rate=[]

for line in f:
    data=line.split()
    rate.append(float(data[2])
    timefrom=time.strftime("%H:%M:%S",time.localtime(float(data[0])))
    tm.append(timefrom)
    


##Draw the plot
ax=plt.subplot(111)
plt.xlabel('Time')
plt.ylabel('Number of Tweets')
plt.title('Number of Tweets Per Second')
plt.plot(rate)
ax.set_xticklabels(elapse,rotation=20, rotation_mode="anchor", ha="right")
plt.show()

f.close()