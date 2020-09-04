"""module 1 functions
"""

import pandas as pd
import numpy as np
import datetime


def splitdate(df, date):
    '''Convert columns to datetime, then add additional columns for
    day, month, year'''
    if type(df[date]) == object:
        df[date] = pd.to_datetime(df[date])
    elif type(df[date]) == np.float64 or type(df[date]) == np.int64:
        df[date] = pd.to_datetime(df[date], format='%Y%m%d')
    else:
        df[date] = pd.to_datetime(df[date])
   
    # then split into year, month, day
    df['year'] = df[date].dt.year
    df['month'] = df[date].dt.month
    df['day'] = df[date].dt.day


def addlist(df, list):
    '''Converts list to Series then adds to DataFrame'''
    s = pd.Series(list, index=df.index)
    df['listcol'] = s

    