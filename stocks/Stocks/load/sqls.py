# coding: UTF-8

last_modified_sql = """
select
    max(updated_at)
from
    m_stock_info
where
    stock_id = ?
;
"""

insert_t_stock_prices = """
insert into
t_stock_prices(stock_id, date, open, high, low, close, adjusted_open, adjusted_high, adjusted_low, adjusted_close, yeild)
values(?,?,?,?,?,?,?,?,?,?,?)
;
"""

delete_t_stock_prices = """
delete from t_stock_prices
where stock_id = ?
;
"""

insert_m_stock_info = """
insert into
m_stock_info(stock_id, company_name, updated_at)
values(?,?,?)
;
"""

delete_m_stock_info = """
delete from m_stock_info
where stock_id = ?
;
"""