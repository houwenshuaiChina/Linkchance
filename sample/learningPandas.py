import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
print(s)
dates = pd.date_range('20130101', periods=6)
print(dates)
s1=pd.Series([1,3])
s2=pd.Series([2,4,6],index=['A','B','C'])
print(s1,s2[2])
# s3=pd.DataFramd("1A":['1','2','3'],"2B":['3','4','5'])