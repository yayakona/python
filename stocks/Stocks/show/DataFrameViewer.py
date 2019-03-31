# coding: UTF-8

# from Stocks.Stocks.show.DataFrameViewer import DataFrameViewer

import datetime

import numpy as np
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib.dates import date2num


class DataFrameViewer:

    #https://qiita.com/kjybinp1105/items/be462b481b47b6f94b14
    def candlestick(df):
        fig = plt.figure()
        ax = plt.subplot()
        xdate = [x.date() for x in df.index]  # 日付
        print(xdate)
        ochl = np.vstack((date2num(xdate), df.values.T)).T
        mpf.candlestick_ohlc(ax, ochl, width=0.7, colorup='g', colordown='r')
        ax.grid()  # グリッド表示
        ax.set_xlim(df.index[0].date(), df.index[-1].date())  # x軸の範囲
        fig.autofmt_xdate()  # x軸のオートフォーマット
        fig.show()
        
if __name__ == "__main__":
    import os
    

    df = PandasDataAccessor.load(4563, start="2019-01-01",end="2019-03-31")
    DataFrameViewer.candlestick(df)