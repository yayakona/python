# -*- coding: utf-8 -*-

import datetime


def load_data(stock_id: Int, start: String = None, end: String = None):
    """
    Parameter
    ___
        stock_id





    """
    # 今日の日付をYYYYMMDD形式で取得する
    now_date: String = datetime.datetime.now().strftime("%Y/%m/%d")
    # DBに最後にアップデートした取得した日付をYYYYMMDD形式で取得する
    updated_date: String = "TODO"
    

    ## DBからstock_idの
