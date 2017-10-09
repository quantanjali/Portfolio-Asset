# -*- coding: utf-8 -*-
"""
Copyright 2017 Nguyen Minh, Thanh

Python for Financial Analysis

Project Name:
Draft Number:

@author:Nguyen Minh Thanh
"""


import numpy as np
import pandas as pd



data = pd.read_csv("Monthdata.csv")

data.head()

print("\n Brief Information of DataFrame loaded ")
print 40*"-"
print "Number of Assets: %.2f" %(len(data.columns)-1)
print "Length of period: %.2f" %len(data)
print 40*"-"
print "Most recent value of dataframe:"
print data.iloc[-2:,:]

data[1]
data.iloc[:,0]
data.iloc[:,1:]
