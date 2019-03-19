from datetime import datetime


dname = "name"
update_sql_m_stock_info = "UPDATE SET update_by = ? WHERE stock_id = ?;"


class SqliteAccessor:

    def __ini__(self):
        self.conn = sqlite3.connect(dbname)


    def __delete__(self):
        self.conn.close()

    def update_m_stock_info(self, stock_id):
        update_sql_m_stock_info = datetime.now().strftime("%Y-%m-%d")
        conn.execute(update_sql_m_stock_info, (update_at, stock_id))

    def select_