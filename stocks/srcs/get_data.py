# -*- coding: utf-8 -*-

import os
import codecs
from glob import glob
import pandas as pd

def read_stock(file_name):
    file_name = codecs.open(file_name, "r", "Shift-JIS", "ignore")
    return pd.read_csv(file_name, header=1)


def get_stock_data(number):
    file_names =  glob(str(number) + "//*.csv")
    stock_data = read_stock(file_names.pop())
    while not len(file_names) == 0:
        tmp = read_stock(file_names.pop())
        stock_data = pd.concat([stock_data, tmp])
    return stock_data.sort_values(by=u"日付")


if __name__ == '__main__':
    data = get_stock_data(7974)
    print(data)
