import copy
import pandas as pd

class Data:
    def __init__(self, X, y):
        self.X = X
        self.y = y         
        
    @property
    def Xy(self):
        return pd.merge(self.X, self.y, on='ID')
    
    def head(self, num):
        other = copy.deepcopy(self)
        other.X = self.X.iloc[:num,:]
        other.y = self.y.iloc[:num,:]  
        return other
     
        
    def tail(self, num):
        other = copy.deepcopy(self)
        other.X = self.X.iloc[-num:,:]
        other.y = self.y.iloc[-num:,:]   
        return other