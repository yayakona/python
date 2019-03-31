# coding: UTF-8

#from Stocks.Stocks.load.PandasDataAccessor import PandasDataAccessor

from datetime import datetime

import pandas_datareader.data as web

class PandasDataAccessor:

    @staticmethod
    def sort_date(df):
        df.sort_values("Date")
    
    @staticmethod
    def load(stock_id, start="1000-01-01", end="9999-12-31"):

        start_year, start_month, start_day = map(int, start.split("-"))
        end_year, end_month, end_day = map(int, end.split("-"))

        start_datatime = datetime(start_year, start_month, start_day)
        end_datatime = datetime(end_year, end_month, end_day)

        df = web.DataReader('{}.JP'.format(stock_id), 'stooq', start_datatime, end_datatime)

        return PandasDataAccessor.sort_date(df)

if __name__ == "__main__":
    df = PandasDataAccessor.load(4563, start="2019-01-01",end="2019-03-31")
    print(df)