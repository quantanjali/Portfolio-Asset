# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 14:29:47 2017

@author: Administrator
"""

from numpy import matrix, array, zeros, empty, sqrt, ones, dot, append, mean, cov, transpose, linspace
from numpy.linalg import inv, pinv
import numpy as np
import scipy.optimize
import math
import functools

window = 255
refresh_rate = 40


def rename_col(df):
    df = df.rename(columns = {"Market Capitalization":"cap"})
    df = df.fillna(method = 'ffill')
    df = df.tshift(1, freq = 'b')
    return df

def compute_mean(W,R):
    return sum(W*R)

def compute_var(W, C):
    return dot(dot(W,C), W)

def compute_mean_var(W, C, R):
    return compute_mean(W,R), compute_var(W, R)

def fitness(W, R, C, r):
    mean_1, var = compute_mean_var(W, R, C)
    penalty = 0.1*abs(mean_1 - r)
    return var + penalty

def solve_weights(R, C, rf):
    n = len(R)
    W = ones([n])/n
    b_ = [(0.1,1) for i in range(n)]
    c_ = ({'type':'eq', 'fun':lambda w: sum(w)-1.})
    optimized = scipy.optimize.minimize(fitness, W, (R, C, sum(R*W)),
                                        method = "SLSQP", constraints = c_,
                                        bounds = b_) #check
    if not optimized.success:
        raise BaseException(optimized.message)
    return optimized.x

daily_returns = np.zeros((len(context.securities), window))




def assets_meanvar(daily_returns):
    expreturns = array([])
    (rows, cols) = daily_returns.shape
    for r in range(rows):
        expreturns = append(expreturns, mean(daily_returns[r]))

    covars = cov(daily_returns)
    expreturns = (1+expreturns)**255 - 1
    covars = covars *255
    return expreturns, covars



def initialize(context):

    context.day = 0

    context.securities = [sid(24), sid(26578), sid(3149), sid(5061), sid(16841)]
    context.market_cap = [479.51, 377.58, 272.76, 300.86, 180.96]
    context.cap_wts = np.array(context.market_cap)/sum(np.array(context.market_cap))
    context.max_notational = 1000000.1
    context.min_notational = -1000000.0

def handle_data(context, data):

    all_prices = get_past_prices(data)

    if all_prices is None:
        return

    if context.day % refresh_rate is not 0:
        context.day = context.day + 1
        return

    daily_returns = np.zeros((len(context.securities), window))

    security_index = 0
    for security in context.securities:
        if data.has_key(security):
            for day in range(0, window):
                day_of = all_prices[security][day]
                day_before = all_prices[security][day-1]
                daily_returns[securities_index][day] = (day_of - day_before)/day_before
            security_index = security_index + 1
