# -*- coding: utf-8 -*-

import os
import datetime
import sqlite3
from contextlib import closing

import pandas as pd

from download_data import download_data
import sqls


all_delete = ""

def load_data(stock_id, start="0000-00-00", end="9999-99-99", should_all_update=False, should__diff_update=False):
    """
    Parameter
    _________
    stock_id : Int
    start : String, Optional=None
    end : String, Optional=None
    should_all_update : Boolean, Optional=False
    should__diff_update : Boolean, Optional=False
    """
    stock_id = str(stock_id)
    dbname = os.path.join("data", "sqllite", "dev.db")

    expected_df = "111"

    with closing(sqlite3.connect(dbname)) as conn:
        with closing(conn.cursor()) as cursor:

            # executeメソッドでSQL文を実行する
            create_table = sqls.last_modified_sql
            cursor.execute(create_table, (stock_id,))
            
            conn.commit()
            
            # 今日の日付をYYYYMMDD形式で取得する
            now_date = datetime.datetime.now().strftime("%Y-%m-%d")
            # DBに最後にアップデートした取得した日付をYYYYMMDD形式で取得する
            updated_date = conn.execute(sqls.last_modified_sql, (stock_id,))
            updated_date.close()
            """
        
            if all_update_flag:
                df = download_data(stock_id)
                df.ix[:,["stock_id", "date", "open", "high", "low", "close", "adjusted_open", "adjusted_high", "adjusted_low", "adjusted_close", "yeild"]].to_sql("t_stock_prices", conn, if_exists="append")
                conn.execute(sqls.delete_m_stock_info, (stock_id,))
                conn.execute(sqls.insert_m_stock_info, (stock_id, "sample", now_date))
                conn.commit()
        
            elif diff_update_flag or update_date < now_date:
                df = download_data(stock_id, start)
                df[start < df[date]].ix[:,["stock_id", "date", "open", "high", "low", "close", "adjusted_open", "adjusted_high", "adjusted_low", "adjusted_close", "yeild"]].to_sql("t_stock_prices", conn, if_exists="append")
                conn.execute(sqls.delete_m_stock_info, (stock_id,))
                conn.execute(sqls.insert_m_stock_info, (stock_id, "sample", now_date))
                conn.commit()

            # expected_df = pd.read_sql("select * from t_stock_prices where stock_id = "+str(stock_id)+" and date "+start+" and "+end, conn)
            conn.commit()
            """
    return expected_df

    
        
if __name__ == '__main__':
    print(load_data(6193))