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



def PortfolioOpt(object):
    '''
    Base class to handle csv data and calculate descriptive
    '''

    def __init__(self, data, riskfree, datatype):
        '''
        Attributes:
        -----------
        data: pandas.DataFrame
            Dataframe with Date at 1st column and the rest is Daily Closing 
            Price or Return
            
        riskfree: float
            Annual Risk Free Rate
            
        datatype: boolean
            Closing Price or Return in DataFrame, true if Closing Price,
            false if Return
            
        
        
        
        '''
        
        self.file_raw = file_raw
        
        if not isinstance(file_raw, pd.DataFrame):
            raise ValueError("file_raw is not a pandas Dataframe)
        
        self.riskfree = riskfree
        
        if not isinstance(riskfree, float) or riskfree < 0:
            raise ValueError("riskfree type is not possible)
            
        self.datatype = datatype
        
        if not isinstance(datatype, boolean):
            raise ValueError("datatype is not a boolean type")
            
            
        
        self.average_return = 0
        self.data = pd.DataFrame()
        self.name = []
        
    def get_name(self):
        return self.name
        
    def get_avgret(self):
        return data.pct_change().dropna().mean()
    
    def print_info(self):
        print "\n Brief Information of DataFrame loaded "
        print 40*"-"
        print "Number of Assets: %.2f" %(len(file_raw.columns) - 1) 
        print "Length of period: %.2f" %len(file_raw)
        print 40*"-"
        print "Most recent value of data:"
        print file_raw.iloc[-2:]
        
    def clean_data(self):
        temp = self.file_raw
        temp.index = temp.iloc[:,0]
        temp = temp.iloc[:,1:]
        self.data = temp
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        