# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 12:50:31 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt
import datetime

f=open('numbers_persecond_SuperBowlXLIX.txt','r')
tmstmp1=[]
rate1=[]

for line in f:
    data=line.split()
    tmstmp1.append(data[0])
    rate1.append(data[2])
    
tmstmp=map(int,tmstmp1)
rate=map(float,rate1)


##Transfer the timestamp into standard time
stm=[]
for i in tmstmp:
    stm.append(datetime.datetime.fromtimestamp(i).strftime('%H:%M:%S'))

##Draw the plot
plt.title('Number of Tweets Per Second')
plt.xlabel('Time')
plt.ylabel('Number of Tweets')
plt.plot(stm,rate)
plt.show()

f.close()