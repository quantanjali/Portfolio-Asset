
'''
This module used to implement Black_Scholes formula for European Option without 
dividend only
'''


import abc
import math
import numbers
import time

import numpy as np
import scipy.optimize
import scipy.stats


class FinInstrument(object):
    @abc.abstractmethod
    def run(self):
        '''
        inherited class must implement this method 
        '''
        
class Option(FinInstrument):
    
    def __init__(self, type_, S0, Strike, T, vol=None, rfr = None):
        self.type_ = type
        self.S0 = S0
        self.Strike = Strike
        self.T = T
        self.vol = vol
        self.mat = mat
        self.rfr = rfr
        
    def run(self, **kwargs):
        result = self.BS(**kwargs)
        return result
    
    
    def bs(self):
        d1 = (math.log(self.S0/self.Strike) + (self.rfr + 0.5*self.vol*self.vol)*self.T)/\
        self.vol*math.sqrt(self.T)
        d2 = d1 - self.vol*math.sqrt(self.T)
        disc_f = np.exp(-self.rfr*self.T)
        
        if self.type_ == "Call":
            NC_d1 = scipy.stats.norm.cdf(d1)
            NC_d2 = scipy.stats.norm.cdf(d2)
            DC_d1 = scipy.stats.pdf(d1) 
            
            price = self.S0*NC_d1 - self.Strike*disc_f*NC_d2
            
            delta = NC_d1
            theta = (self.S0*DC_d1*self.vol)/(2*math.sqrt(self.T)) - \
            self.rfr*self.Strike*disc_f*NC_d2
    
        