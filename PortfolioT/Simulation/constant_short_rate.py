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

class constant_short_rate(object):
    def __init__(self, name, short_rate):
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError('Short rate negative')
            
    def get_discount_factors(self, date_list, dtobjects=True):
        if dtobjects is True:
            dlist = get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp((self.short_rate*np.sort*-dlist))
        return np.array((date_list, dflist)).T
    
    
    
    
