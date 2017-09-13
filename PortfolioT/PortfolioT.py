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

    def __init__(self, file_raw, riskfree):
        '''
        Attributes:
        -----------
        file_raw: pandas DataFrame with Date (1st column) and Closing Price
        
        '''
        
        self.file_raw = file_raw
        if not isinstance(file_raw, pd.DataFrame):
            raise ValueError("file_raw is not a pandas Dataframe)
        self.riskfree = 0
        self.securities = []
        self.data = pd.DataFrame()
        self.name = []
        
    def get_name(self):
        return self.name
        
    def get_avgret(self):
        return data.pct_change().dropna().mean()
    
    
        