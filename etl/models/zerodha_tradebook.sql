MODEL (
  name tradebooks.zerodha_raw,
  kind FULL
);

select * from read_csv_auto("seeds/zerodha/tradebook_*.csv")
