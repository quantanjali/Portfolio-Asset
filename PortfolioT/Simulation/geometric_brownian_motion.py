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


class geometric_brownian_motion(simulation_class):
    def __init__(self, name, mar_env, corr=False):
        super(geometric_brownian_motion, self).__init__(name, mar_env, corr)
        
    def update(self, initial_value=None, volatility=None, final_date=None):
        if initial_value is not None:
            self.initial_value = initial_value
        if volatility is not None:
            self.volatility = volatility
        if final_date is not None:
            self.final_date = final_date
        self.instrument_values = None
    
    def generate_paths(self, fixed_seed=False, day_count=365.):
        if self.time_grid is None:
            self.generate_time_grid()
        M = len(self.time_grid)
        I = self.paths
        paths = np.zeros((M,I))
        paths[0] = self.initial_value
        if not self.correlated:
            rand = sn_random_numbers((1, M, I), fixed_seed=fixed_seed)
        else:
            rand = self.random_numbers
        short_rate = self.discount_curve.short_rate
        for t in range(1, len(self.time_grid)):
            if not self.correlated:
                ran = rand[t]
            else:
                ran = np.dot(self.cholesky_matrix, rand[:,t,:])
                ran = ran[self.rn_set]
            dt = (self.time_grid[t] - self.time_grid[t-1]).days/day_count
            paths[t] = paths[t-1] * np.exp((short_rate - 0.5*self.volatility**2)*dt + \
                 self.volatility*np.sqrt(dt)*ran)
        self.instrument_values = paths
        


me_gbm = market_environment('me_gbm', dt.datetime(2015,1,1))
me_gbm       
me_gbm.add_constant('initial_value', 36.)    
me_gbm.add_constant('volatility', 0.2)    
me_gbm.add_constant('final_date', dt.datetime(2015,12,31))    
me_gbm.add_constant('currency', 'EUR')    
me_gbm.add_constant('frequency', 'M')    
me_gbm.add_constant('paths', 1000)    

csr = constant_short_rate('csr', 0.05)    
me_gbm.add_curve('discount_curve', csr)    

gbm = geometric_brownian_motion('gbm', me_gbm)
    
    
    
    
    
    
    
    
    
    
    
    