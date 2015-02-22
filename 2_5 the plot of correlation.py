# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:36:05 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt
import time
import datetime

##Extract the rate
rate1=[]
tmstmp1=[]
f=open('first_second_correlation.txt','r')
for line in f:
    data=line.split()
    rate1.append(data[6])
    tmstmp1.append(data[0])

rate=map(float,rate1)
tmstmp=map(int,tmstmp1)

##文本里的第一栏是时间戳，要提取出来转换成时间然后再写进坐标轴
tm=[]
for i in tmstmp:
    tm.append(datetime.datetime.fromtimestamp(i).strftime('%H:%M:%S')

##Draw the line 
plt.xlabel('Time')
plt.ylabel('The rate')
plt.title('The Correlation in Linear Scale')
plt.plot(tm,rate)
plt.show()








