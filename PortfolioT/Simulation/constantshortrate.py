# -*- coding: utf-8 -*-
"""
Copyright 2017 Nguyen Minh, Thanh

Python for Financial Analysis

Project Name:
Draft Number:

@author:Nguyen Minh Thanh
"""

class constantshortrate(object):
    def __inti__(self, name, short_rate):
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError("Short rate negative")
            
    def get_discount_factors(self, date_list, dtobjects = True):
        if dtobjects is True:
            dlist= get_year_deltas(date_list)

