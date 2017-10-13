


from metrics import *
from dateutil.relativedelta import relativedelta
import pandas as pd

class Performance(object):
    
    def __init__(self):
        super().__init__()
        
    def CAGR(self, decimals = 5):
        return CAGR(self.beginning_cash, self.ending_cash,
                    relativedelta(self.end_time,self.start_time).years,
                    decimals)
        
        def sharpe_ratio