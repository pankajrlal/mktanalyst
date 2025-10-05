MODEL (
    name tradebooks.unified,
    kind FULL
);

with zerodha_tradebook as (
SELECT 
* from tradebooks.zerodha_standard
),
with groww_tradebook as (
    SELECT
    * from tradebooks.groww_standard
)

SELECT * from zerodha_tradebook
UNION ALL
SELECT * from groww_tradebook
