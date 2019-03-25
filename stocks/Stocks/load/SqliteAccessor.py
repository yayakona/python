

# from Stocks.load.SqliteAccessor import SqliteAccessor

import os
from datetime import datetime

import pandas as pd


db_name = os.path.join("data", "sqllite", "dev.db")
update_sql_m_stock_info = "UPDATE m_stock_info SET update_by = ? WHERE stock_id = ?;"


class SqliteAccessor:

    def __init__(self):
        self.conn = sqlite3.connect(db_name)


    def __delete__(self):
        self.conn.close()

    """
    table
        m_stock_info
    columns
        
    method
        C: 
        R:
        U:
        D: 
    """

    def select_m_stock_info(self, stock_id = None):
        sql = "select * from m_stock_info"
        df = None
        if stock_id:
            sql += " where stock_id = ?"
            df =  self.conn.execute(sql, (stck_id,))
        else:
            df = self.conn.execute(sql)
        return pd.DataFrame(df,columns = ["stock_id", "company_name" , "updated_at"])
        
    def update_m_stock_info(self, stock_id):
        """

        TODO
            pandasからうまくupdateかけたいけど無理そう
            http://paperface.hatenablog.com/entry/2019/02/04/【SQLite_%2B_Python_%2B_Pandas】SQLiteをPandas（DataFrame）で扱う
            これ以上調べるのめんどくさいから普通に自分でquery書いた方が良さげ
        """ update_sql_m_stock_info = datetime.now().strftime("%Y-%m-%d")
        conn.execute(update_sql_m_stock_info, (update_at, stock_id))

    def update_m_stock_info(self, stock_id):
        
     

