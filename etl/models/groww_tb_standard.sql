MODEL (
    name tradebooks.groww_standard,
    kind FULL
);

SELECT
   "Symbol" as symbol, 
strptime("Execution date and time",'%d-%m-%Y %I:%M %p')::DATE as trade_date,
   "Exchange" as exchange,
   LOWER("Type") as trade_type,
   cast("Quantity" as int) as quantity,
   "Value"/"Quantity" as price,
   "Value" as traded_value,
   "Exchange Order Id" as order_id,
   'groww' as platform
from tradebooks.groww_raw
