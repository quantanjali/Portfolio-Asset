# -*- coding: utf-8 -*-
"""
Copyright 2017 Nguyen Minh, Thanh

Python for Financial Analysis

Project Name:
Draft Number:

@author:Nguyen Minh Thanh
"""

import numpy as np
import datetime as dt

def get_year_deltas(date_list, day_count=365.):
    start = date_list[0]
    delta_list = [(date-start).days/day_count for date in date_list]
    return np.array(delta_list)


dates = [dt.datetime(2015, 1, 1), dt.datetime(2015,7,1), dt.datetime(2016,1,1)]
get_year_deltas(dates)