    --  columns = {
    --      "Instrument": "str",
    --      "Qty.": "int",
    --      "Avg. cost": "float",
    --      "LTP": "float",
    --      "Invested": "float",
    --      "Cur. val": "float",
    --      "P&L": "float",
    --      "Net chg.": "float",
    --      "Day chg.": "float",
    --      "holdings_date": "datetime",
    --  }

MODEL (
    name holdings.zerodha_standard,
    kind FULL
);

SELECT
   "Instrument" as symbol, 
   cast("Qty." as int) as quantity,
   cast("Avg. cost" as float) as avg_cost,
   cast("LTP" as float) as ltp,
   cast("Invested" as float) as invested,
   cast("Cur. val" as float) as current_value,
   cast("P&L" as float) as pl,
   "holdings_date"::DATE as holdings_date,
   'zerodha' as platform
from holdings.zerodha_raw
