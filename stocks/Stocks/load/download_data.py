# -*- coding: utf-8 -*-


import os
from time import sleep
import datetime
import tempfile


import codecs
from glob import glob
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WAIT_SECOND = 10

class DownloadCsv:
    URL = "https://kabuoji3.com/stock/"
    def __init__(self):
        self.now_year = datetime.date.today().year

    def download_csv(self,stock_id, download_dir, start = 0, end = 9999):
        cur_year = min(self.now_year, end)

        driver = self.init_selenium(stock_id, download_dir)

        while True:
            try:
                #ボタン遷移いれずに直接遷移先にアクセス掛けたい
                driver.get("https://kabuoji3.com/stock/"+str(stock_id)+"/"+str(cur_year)+"/")
                driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()
                WebDriverWait(driver, WAIT_SECOND).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn_form btn_download"]')))
                driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()
                cur_year -= 1
                if cur_year < start:
                    break
            except:
                #driver.close()
                break

    def __del__(self):
        print("download finished")
        #ダウンロードディレクトリをもどす


    def init_selenium(self,stock_id, download_dir):
        ###Chromeへオプションを設定
        chop = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : download_dir}
        chop.add_experimental_option("prefs",prefs)
        chop.add_argument('--ignore-certificate-errors') #SSLエラー対策
        driver = webdriver.Chrome(chrome_options = chop)
        return driver



def read_stock(file_name):
    file_name = codecs.open(file_name, "r", "Shift-JIS", "ignore")
    return pd.read_csv(file_name, header=1)


def get_stock_data(dir_path):
    file_names =  glob(os.path.join(dir_path, "*.csv"))
    print(file_names)
    stock_data = read_stock(file_names.pop())
    while not len(file_names) == 0:
        tmp = read_stock(file_names.pop())
        stock_data = pd.concat([stock_data, tmp])
    return stock_data.sort_values(by=u"日付")

def transfrom_columns_jp_to_en(df):
    return df.rename(columns = {
        u"日付" : "date",
        u"始値" : "open",
        u"高値" : "high",
        u"安値" : "low",
        u"終値" : "close",
        u"出来高" : "yeild",
        u"終値調整値" : "adjusted_close",
    })

def add_adujust_prices(df):
    adjusted_ratio = df["adjusted_close"] / df["close"]
    df["adjusted_open"] = df["open"] * adjusted_ratio
    df["adjusted_high"] = df["high"] * adjusted_ratio
    df["adjusted_low"] = df["low"] * adjusted_ratio
    return df

def download_data(stock_id, start="0000-00-00", end="9999-99-99"):
    df = None
    with tempfile.TemporaryDirectory() as dname:
        download_driver = DownloadCsv()
        download_driver.download_csv(stock_id, dname, int(start[0:4]), int(end[0:4]))
        df = get_stock_data(dname)
        df = transfrom_columns_jp_to_en(df)
        df = add_adujust_prices(df)
    return df[start <= df["date"] <= end]

if __name__ == '__main__':
    print(download_data(6193))
