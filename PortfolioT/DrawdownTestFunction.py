



import numpy as np
import pandas as pd

data = pd.read_csv("Monthdata.csv")
data = data.iloc[:,0:2]
data.head()

def drawdowns(array, target='BID'):
    pass

if not isinstance(data, pd.DataFrame):
    raise Exception("Array must be a pandas dataframe")
    
drawdown_down_times = []
drawdown_up_times = []
in_drawdown_period = False

array = data.copy()
array['pct.change'] = array['BID'].pct_change()

if array['pct.change'].ix[1] < 0:
    drawdown_down_times.append(array['pct.change'].index[0])
    in_drawdown_period = True
    
for i in range(1, len(array['pct.change'])):
    time = array['pct.change'].index[i-1]
    if in_drawdown_period:
        if array['pct.change'][i] > 0:
            drawdown_up_times.append(time)
            in_drawdown_period = False
    elif not in_drawdown_period:
        if array['pct.change'][i+1] < 0:
            drawdown_down_times.append(time)
            in_drawdown_period = True
            
if in_drawdown_period:
    drawdown_up_times.append(array['pct.change'].index[-1])
    
drawdown_df = pd.DataFrame({'From': drawdown_down_times,
                            'To': drawdown_up_times})
    
drawdown_df['Length'] = drawdown_df['To'] - drawdown_df['From']


    
    
            
    
            
        
        