from datetime import datetime


dname = "name"
update_sql = "UPDATE ? SET カラム名1 = 値, カラム名2 = 値2, ... WHERE 条件式;"


class SqliteAccessor:

    def __ini__(self):
        self.conn = sqlite3.connect(dbname)


    def __delete__(self):
        self.conn.close()

    def update_info(self, stock_id):
        update_at = datetime.now().strftime("%Y-%m-%d")