import abc
from math import exp
import math
import numbers
import time

import numpy as np
import scipy.optimize
import scipy.stats


def enum(**enums):
    return type('Enum', (), enums)

OptionType = enum(CALL='call', PUT='put')
OptionExerciseType = enum(EUROPEAN='european', AMERICAN='american')
OptionModel = enum(BLACK_SCHOLES='black_scholes', BINOMIAL_TREE='binomial_tree',
                   MONTE_CARLO='monte_carlo')
OptionMeasure = enum(VALUE='value', DELTA='delta', THETA='theta', RHO='rho',
                     VEGA='vega', GAMMA='gamma')

a = type('Enum', ())



class Instrument(object):
    @abc.abstractmethod
    def run_model(self):
        """calculate measures (i.e. theoretical value & greaks) for this 
        this instrument
        """



class Option(Instrument):
    def __init__(self, opt_type, spot0, strike, mat, vol=None, riskless_rate=None,
                 yield_=None, exer_type=None):
        self.opt_type = opt_type #1
        self.spot0 = spot0 #2
        self.strike = strike #3
        self.vol = vol #4
        self.mat = mat #5
        self.riskless_rate = riskless_rate or 0 #6
        self.yield_ = yield_ or 0 #7
        self.exer_type = exer_type or OptionExerciseType.AMERICAN #8
        self.model_cache = {} #9
        self.model_cache_param_hashes = {} #10
        
    def copy(self):
        return Option(self.opt_type, self.spot0, self.strike, self.mat,
                      vol=self.vol, riskless_rate=self.riskless_rate,
                      yield_=self.yield_, exer_type=self.exer_type)
    
    def param_hash(self):
        return hash((self.opt_type, self.spot0, self.strike, self.mat,
                     self.vol, self.riskless_rate, self.yield_, self.exer_type))
        
    @staticmethod
    def imply_volatility(premium, max_vol=0.99, *args, **kwargs):
        def obj_fn(vol_guess):
            kwargs['vol'] = vol_guess
            val = Option(*args, **kwargs).run_model()[OptionMeasure.VALUE]
            return val-premium
        try:
            return scipy.optimize.bisect(obj_fn, 0.01, max_vol, xtol=0.0025)
        except ValueError:
            return None
        
    def run_model(self, model=OptionModel.BINOMIAL_TREE, **kwargs):
        curr_param_hash = self.param_hash()
        
        if model in self.model_cache:
            prev_param_hash = self.model_cache_param_hashes[model]
            if self.param_hash() == prev_param_hash:
                return self.model_cache[model]
            
        if model == OptionModel.BLACK_SCHOLES:
            result = self.black_scholes(**kwargs)
            
        elif model == OptionModel.BINOMIAL_TREE:
            result = self.binomial_tree(**kwargs)
            
        else:
            result = self.monte_carlo(**kwargs)
        
        self.model_cache[model] = result
        self.model_cache_param_hashes = curr_param_hash
        return result
    
    
    def black_scholes(self):
        assert self.exer_type == OptionExerciseType.EUROPEAN, "Black-Scholes\
        does not support early exercise"
        assert (self.yield_ is None) or is_number(self.yield_), \
        "Black-Scholes does not support discrete dividends"
        sqrt_mat = self.mat ** 0.5
        d1 = (math.log(float(self.spot0)/self.strike) + 
              (self.riskless_rate-self.yield_+0.5*self.vol*self.vol)*self.mat)/ \
              (self.vol*sqrt_mat)
        d2 = d1 - self.vol*(self.mat**0.5)
        d1_pdf = scipy.stats.norm.pdf(d1)
        riskless_disc = exp(-self.riskless_rate*self.mat)
        yield_disc = exp(-self.yield_*self.mat)
        if self.opt_type == OptionType.CALL:
            d1_cdf = scipy.stats.norm.cdf(d1)
            d1_cdf = scipy.stats.norm.cdf(d2)
            delta = yield_disc * d1_cdf
            val = self.spot0*delta - riskless_disc*self.strike*d2_cdf
            theta = -yield_disc*(self.spot0*)
            
              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        