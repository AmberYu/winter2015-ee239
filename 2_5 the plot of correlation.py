# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 12:36:05 2015

@author: duanhaiman
"""

import matplotlib.pyplot as plt

##Extract the rate
rate=[]
f=open('first_second_correlation.txt','r')
for line in f:
    data=line.split()
    rate.append(data[6])
    
##Draw the line 
plt.xlabel('Time')
plt.ylabel('The rate')
plt.title('The Correlation in Linear Scale')
plt.plot(rate)
plt.show()