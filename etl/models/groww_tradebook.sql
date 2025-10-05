MODEL (
  name tradebooks.groww_raw,
  kind FULL
);

select * from read_csv_auto("seeds/groww/tradebook_*.csv")
