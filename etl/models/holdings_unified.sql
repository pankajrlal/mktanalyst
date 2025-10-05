MODEL (
    name holdings.unified,
    kind FULL
);

with z as (
    SELECT
       symbol, 
       quantity,
       avg_cost,
       ltp,
       invested,
       current_value,
       pl,
       holdings_date,
       platform
    from holdings.zerodha_standard
),

with g as (
    SELECT
       symbol, 
       quantity,
       avg_cost,
       ltp,
       invested,
       current_value,
       pl,
       holdings_date,
       platform
    from holdings.groww_standard
)

SELECT * from z 
UNION ALL 
SELECT * from g
