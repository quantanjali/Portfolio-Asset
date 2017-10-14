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

class market_environment(object):
    
    def __init__(self, name, pricing_date):
        self.name = name
        self.pricing_date = pricing_date
        self.constants = {}
        self.lists = {}
        self.curves = {}
        
    def add_constant(self, key, constant):
        self.constants[key] = constant
        
    def get_constant(self, key):
        return self.constants[key]
    
    def add_list(self, key, list_object):
        self.lists[key] = list_object
        
    def get_list(self, key):
        return self.lists[key]
    
    def add_curve(self, key, curve):
        self.curves[key] = curve
        
    def get_curve(self, key):
        return self.curves[key]
    
    def add_environment(self, env):
        for key in env.constants:
            self.constants[key] = env.constants[key]
        for key in env.lists:
            self.lists[key] = env.lists[key]
        for key in env.curves:
            self.curves[key] = env.curves[key]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            