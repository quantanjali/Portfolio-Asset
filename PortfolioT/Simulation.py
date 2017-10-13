# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 18:22:54 2017

@author: Administrator
"""
import numpy as np


s = {'1':'1'}

r = 0.05
sigma = 0.2
T = 0.5
dt = T/100
for i in range(2,100):
    s[i] = s[i-1] + r*s[i-1]*dt + sigma * s[i-1]*np.sqrt(dt)*np.random.normal(0,1,1)
    

S0 = 100
r = 0.05
sigma = 0.25
T = 2.0
I = 10000
ST1 = S0 * np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T) * npr.standard_normal(I))
plt.hist(ST1, bins=50)

a = npr.standard_normal(I)

I = 10000
M = 50
dt = T/M
S = np.zeros((M+1, I))
S[0] = S0

S = np.zeros(I + 1)



S0 = 100
K = 100.
r = 0.05
sigma = 0.05
T = 1
N = 252
deltat = T/N
i = 1000
discount_factor = np.exp(-r*T)


np.random.seed(123)


def gen_paths(S0, r, sigma, T, M, I):
    dt = float(T)/M
    paths = np.zeros((M+1, I), np.float64)
    paths[0] = S0
    for t in range(1, M + 1):
        rand = np.random.standard_normal(I)
        paths[t] = paths[t-1] * np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*rand)




S0 = 100
K = 100.
r = 0.05
T = 1
N = 1000
deltat = T/N
paths = np.zeros(1000,np.float64)
paths[0] = 100
for i in range(1,1000):
    rand = np.random.standard_normal(1)
    paths[t] = paths[t-1]*np.exp((r-0.05*sigma**2)*deltat)



    