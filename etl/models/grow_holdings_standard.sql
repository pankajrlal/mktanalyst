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
    name holdings.groww_standard,
    kind FULL
);

with holdings_base as (
    SELECT
       "stock name" as stock_name, 
       "isin" as isin,
       "quantity" as quantity,
       cast("average buy price" as float) as avg_cost,
       cast("closing price" as float) as ltp,
       cast("buy value" as float) as invested,
       cast("closing value" as float) as current_value,
       cast("unrealised p&l" as float) as pl,
       "holdings_date"::DATE as holdings_date,
       'groww' as platform
    from holdings.groww_raw
),
holdings_enriched as (
SELECT
   tb."Symbol" as symbol, 
   hb.quantity as quantity,
   hb.avg_cost as avg_cost,
   hb.ltp as ltp,
   hb.invested as invested,
   hb.current_value as current_value,
   hb.pl as pl,
   hb.holdings_date as holdings_date,
   hb.platform as platform,
from holdings_base hb
inner join tradebooks.groww_raw tb on hb.isin = tb."ISIN"
)
SELECT DISTINCT
  symbol, quantity, avg_cost, ltp, invested, current_value, pl, holdings_date, platform
FROM holdings_enriched;
