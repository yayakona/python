# -*- coding: utf-8 -*-

import datetime


def load_data(stock_id: Int, start: String = None, end: String = None):
    """
    Parameter
    ___
        stock_id
        start
        end
        all_update
        diff_update




    """
    # 今日の日付をYYYYMMDD形式で取得する
    now_date: String = datetime.datetime.now().strftime("%Y/%m/%d")
    # DBに最後にアップデートした取得した日付をYYYYMMDD形式で取得する
    updated_date: String = "TODO"

    conn = db.cor
    
    if all_update_flag:
        conn.executor(Sqls.all_delete(stock_id))
download_data(stock_id)
    
    elif diff_update_flag or update_date < now_date:
    
    
        
