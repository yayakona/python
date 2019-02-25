# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from time import sleep
import datetime

WAIT_SECOND = 10

class download_csv:
    URL = "https://kabuoji3.com/stock/"
    download_directory='data//'
    def __init__(self):
        self.now_year = datetime.date.today().year

    def download(self,stock_id):
        cur_year = self.now_year
        driver = self.init_selenium(stock_id)

        while True:
            try:
                #ボタン遷移いれずに直接遷移先にアクセス掛けたい
                driver.get("https://kabuoji3.com/stock/"+str(stock_id)+"/"+str(cur_year)+"/")
                driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()
                WebDriverWait(driver, WAIT_SECOND).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn_form btn_download"]')))
                driver.find_element_by_xpath('//button[@class="btn_form btn_download"]').click()
                cur_year -= 1
            except:
                #driver.close()
                break

    def __del__(self):
        print("download finished")
        #ダウンロードディレクトリをもどす


    def init_selenium(self,stock_id):
        ###Chromeへオプションを設定
        stock_download_directory = self.download_directory + str(stock_id)
        if not os.path.exists(stock_download_directory):
            os.mkdir(stock_download_directory)
        chop = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : stock_download_directory}
        chop.add_experimental_option("prefs",prefs)
        chop.add_argument('--ignore-certificate-errors') #SSLエラー対策
        driver = webdriver.Chrome(chrome_options = chop)
        return driver



if __name__ == '__main__':
    odj_download = download_csv()
    odj_download.download("7974")
