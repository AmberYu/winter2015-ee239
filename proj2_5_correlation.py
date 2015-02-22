# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:36:05 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt

##Extract the rate
trate1=[]
trate2=[]
trate=[]
f=open('first_second_correlation.txt','r')
for line in f:
    data=line.split()
    trate1.append(data[2])
    trate2.append(data[4])
    trate.append(data[6])

rate1=map(float,trate1)
rate2=map(float,trate2)
rate=map(float,trate)

    
##The first pic
plt.figure(1) # 创建图表1
plt.xlabel('Tweeting rate of #Patriots')
plt.ylabel('Tweeting rate of #SuperBowlXLIX')
plt.title('The Correlation Between The Tags')
plt.plot(rate2,rate1,'o')

##The second one
plt.figure(2)  # 创建图表2
plt.xlabel('Time')
plt.ylabel('The Tweeting Rate of Tag1/Tag2')
plt.title('The Correlation Between The Tags Over Time')
plt.plot(rate)

plt.show()









