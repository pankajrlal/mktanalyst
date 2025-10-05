MODEL (
    name tradebooks.zerodha_standard,
    kind FULL
);

SELECT
   symbol as symbol, 
   order_execution_time as trade_date,
   exchange as exchange,
   LOWER(trade_type) as trade_type,
   cast(quantity as int) as quantity,
   price as price,
   quantity * price as traded_value,
   order_id as order_id,
   'zerodha' as platform
from tradebooks.zerodha_raw
WHERE segment = 'EQ'
