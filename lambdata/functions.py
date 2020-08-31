"""module 1 functions
""" 

import pandas as pd
import numpy as np
import datetime


def splitdate(df, date):
    #make col datetime
    if (df['date'].dtype == object):
        df['date'] = pd.to_datetime(df['date'])
    elif (df['date'].dtype == np.float64 or df['date'].dtype == np.int64):
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    else:
        print('col already in datetime... spliting..')
        
    #then split into year, month, day
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

def addlist(df, list):
    s = pd.Series(list, index=df.index)
    df['listcol'] = s