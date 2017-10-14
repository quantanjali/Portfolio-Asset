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


# create instance of market_environment class
me_gbm = market_environment('me_gbm', dt.datetime(2015,1,1))
me_gbm       

me_gbm.add_constant('initial_value', 36.)    
me_gbm.add_constant('volatility', 0.2)    
me_gbm.add_constant('final_date', dt.datetime(2015,12,31))    
me_gbm.add_constant('currency', 'EUR')    
me_gbm.add_constant('frequency', 'M')    
me_gbm.add_constant('paths', 1000)    

# create instance of constant_short_rate class
csr = constant_short_rate('csr', 0.05)    
me_gbm.add_curve('discount_curve', csr)    

gbm = geometric_brownian_motion('gbm', me_gbm)
gbm.generate_time_grid()
gbm.time_grid
    