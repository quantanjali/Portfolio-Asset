# -*- coding: utf-8 -*-
"""
Copyright 2017 Nguyen Minh, Thanh

Python for Financial Analysis

Project Name:
Draft Number:

@author:Nguyen Minh Thanh
"""

'''
import numpy as np
import pandas as pd
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("REE.csv", parse_dates=['Date/Time'], index_col = 1 )
del data['Ticker']
data.resample("W", how = 'last')

class data_stock(object):
    
    def __init__(self, filename):
        self.ticker = filename.replace(".csv","")
        self.data = self.csvread(filename)
        self.wdata = self.week_resample()
        self.mdata = self.month_resample()
        self.index_ = self.data.index
        
    def csvread(self,filename):
        temp = pd.read_csv(filename, parse_dates=['Date/Time'], index_col=1)
        del temp['Ticker']
        return temp

    def month_resample(self):
        temp = self.data.resample("BM").last()
        return temp
    
    def week_resample(self):
        temp = self.data.resample("W").last()
        return temp
        
    def return_calculation(self, choice): 
        if choice == "month":
            temp = self.wdata['Close'].pct_change().dropna()
            return temp
        elif choice == "week":
            temp = self.wdata['Close'].pct_change().dropna()
            return temp
        else:
            temp = self.data['Close'].pct_change().dropna()
            return temp
        
    
class statistical_description():
    def __init__(self, data_stock, type_):
        self.data_stock = data_stock
        self.type_ = type_
        self.statistics = self.descriptive_statistics()
        
    def descriptive_statistics(self):
        temp = self.data_stock.return_calculation(self.type_)
        if self.type_ == "month":
            temp_mean = temp.mean()*12
            temp_std = temp.std()*np.sqrt(12)
        elif self.type_ == "week":
            temp_mean = temp.mean()*52
            temp_std = temp.std()*np.sqrt(52)
        else:
            temp_mean = temp.mean()*252
            temp_std = temp.std()*np.sqrt(252)
        return {"mean":temp_mean, "std":temp_std}
        
class regression_calculation(data_stock1, data_stock2):
    
    

#testcode
dat = data_stock("REE.csv")
dat2 = data_stock("FPT.csv")

a = dat.data['Close']

dat.data['Close'].head()
abc = statistical_description(dat, "month")
abc.statistics

