



import pandas as pd
import numpy as np

BDAYS_PER_M = 21
BDAYS_PER_Y = 252
W_PER_Y = 52
M_PER_Y = 12
SEC_PER_D = 24*60*60
SEC_PER_Y = SEC_PER_D * 365.24
ANNULIZATION_FACTORS = {'daily': BDAYS_PER_Y,
                        'weekly': W_PER_Y,
                        'monthly': M_PER_Y}


def CAGR(beg_val, end_val, years, decimals=5):
    try:
        cagr = (np.power((end_val/beg_val), (1/years)))-1
        return cagr.round(decimals)
    except ZeroDivisionError:
        years = 1
        cagr = (np.power((end_val/beg_val), (1/years)))-1
        return cagr.round(decimals)
    
    
def sharpe_ratio(asset_returns, risk_free_rate=.05, period='daily',
                 decimal=3):
    excess_returns = np.mean(asset_returns - risk_free_rate)
    sigma_of_asset = np.std(asset_returns)
    sr = (excess_returns/sigma_of_asset)*\
    np.sqrt(ANNUALIZATION_FACTORS[period])
    
    return np.round(sr, decimal)



def rate_of_return(array):
    
    if isinstance(array, pd.DataFrame):
        if array.iloc[0] == 0:
            raise ZeroDivisionError
        return ((array.iloc[-1]-array.iloc[0])/array.iloc[0]).item()
    
    elif isinstance(array, pd.Series):
        if array.iloc[0] ==0:
            raise ZeroDivisionError
        return (array.iloc[-1]-array.iloc[0])/array.iloc[0]
    else:
        if array[0] == 0:
            raise ZeroDivisionError
        return (array[-1]-array[0])/array[0]
    
def VAR(returns, percentile=.05):
    percentile = percentile*100
    returns = np.sort(returns)
    if isinstance(returns, np.ndarray):
        return np.round(np.percentile(returns,percentile), 2)
    else:
        return np.round(np.percentile(returns.values, percentile),2)
    
def expected_shortfall():
    pass

def max_drawdown(array):
    dd = drawdowns(array)
    return dd[dd['Length'] == dd['Length'].max()]

def drawdowns(array, target='Value'):
    
    if not isinstance(array, pd.DataFrame):
        raise Exception("Array must be a pandas DataFrame")
        
    drawdown_down_times = []
    drawdown_up_times = []
    in_drawdown_period = False
    
    array = array.copy()
    array['return'] = array[target].pct_change()
    if array['pct.change'].ix[1] < 0:
        drawdown_down_times.append(array['pct.change'].index(0))
        in_drawdown_period = True
        
    for i in range(1, len(array['pct.change'])):
        time = array['pct.change'].index[i-1]
        if in_drawdown_period:
            if array['pct.change'][i] > 0:
                drawdown_up_times.append(time)
                in_drawdown_period = False
        if not in_drawdown_period:
            if array['pct.change'].index[time] < 0:
                drawdown_down_times.append(time)
                in_drawdown_period = True
    
    
    
