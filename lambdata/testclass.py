import pandas as pd
import numpy as np
import datetime

#simple class
class Adding:
    def __init__(self, dataframe, list):
        self.dataframe = dataframe
        self.list = list

    def addlist(self):
        s = pd.Series(self.list, index = self.dataframe.index)
        self.dataframe['listcol'] = s




# base class for datawrangling
class Dfwrangler:
    def __init__(self, dataframe):
        self.dataframe = dataframe


# child class for dataframes with date columns
class Dates(Dfwrangler):
    def __init__(self, dataframe, datecol):
        super().__init__(dataframe)
        self.datecol = dataframe[datecol]

    def splitdates(self):
        # make col datatime
        if type(self.datecol) == object:
            self.datecol = pd.to_datetime(self.datecol)
        elif type(self.datecol) == np.float64 or type(self.datecol) == np.int64:
            self.datecol = pd.to_datetime(self.datecol, format='%Y%m%d')
        else:
            self.datecol = pd.to_datetime(self.datecol)
   
        # then split into year, month, day
        self.dataframe['year'] = self.datecol.dt.year
        self.dataframe['month'] = self.datecol.dt.month
        self.dataframe['day'] = self.datecol.dt.day
