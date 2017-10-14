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


class sorted_list(object):
    def __init__(self, elements):
        self.elements = sorted(elements)
    def __iter__(self):
        self.position= -1
        return self
    def next(self):
        if self.position == len(self.elements) -1 :
            raise StopIteration
        self.position += 1
        return self.elements[self.position]
    
    
    
name_list = ['Sandra', 'Lilli', 'Guido', 'Zorro', 'Henry']
sorted_name_list = sorted_list(name_list)

sorted(name_list)


class short_rate(object):
    
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        
    def get_discount_factors(self, time_list):
        time_list = np.array(time_list)
        return np.exp(-self.rate * time_list)

sr = short_rate('r', 0.05)
sr.name, sr.rate

time_list = [0.0, 0.5, 1.0, 1.25, 1.75, 2.0]
sr.get_discount_factors(time_list)

t = np.linspace(0,5)

for r in [0.025, 0.05, 0.1, 0.15]:
    sr.rate = r
    plt.plot(t, sr.get_discount_factors(t), 
             label = 'r = %4.2f' %sr.rate, lw = 1.5)
    plt.xlabel('years')
    plt.ylabel('discount factor')
    plt.grid(True)
    plt.legend(loc=0)
    

sr.rate = 0.05
cash_flows = np.array([-100, 50, 75])
time_list = [0.0, 1.0, 2.0]

disc_facts = sr.get_discount_factors(time_list)
disc_facts*cash_flows
np.sum(disc_facts * cash_flows)


class cash_flow_series(object):
    def __init__(self, name, time_list, cash_flows, short_rate):
        self.name = name
        self.time_list = time_list
        self.cash_flows = cash_flows
        self.short_rate = short_rate
        
    def present_value_list(self):
        df = self.short_rate.get_discount_factors(self.time_list)
        return np.array(self.cash_flows) * df
    
    def net_present_value(self):
        return np.sum(self.present_value_list())
    
sr.rate = 0.05
cfs = cash_flow_series('cfs', time_list, cash_flows, sr)
cfs.cash_flows
cfs.time_list

cfs.present_value_list()
cfs.net_present_value()


class cfs_sensitivity(cash_flow_series):
    def npv_sensitivity(self, short_rates):
        npvs = []
        for rate in short_rates:
            self.short_rate.rate = rate
            npvs.append(self.net_present_value())
        return np.array(npvs)
    
cfs_sens = cfs_sensitivity('cfs' , time_list, cash_flows, sr)         
            
short_rates = [0.01, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2]
npvs = cfs_sens.npv_sensitivity(short_rates)            
            
    
plt. plot(short_rates, npvs, 'b' )
plt. plot(short_rates, npvs, 'ro' )
plt. plot((0, max(short_rates)), (0, 0), 'r' , lw=2)
plt. grid(True)
plt. xlabel('short rate' )
plt. ylabel('net present value' )


import numpy as np
improt pandas as pd

class simulation_class(object):
    def __init__(self, name, mar_env, corr):
        try:
            self.name = name
            self.pricing_date = mar_env.pricing

            
            
            
            