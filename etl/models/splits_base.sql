MODEL (
  name support_data.splits_base,
  kind SEED (
    path '../seeds/bonus_and_splits.csv'
  ),
 columns (
    "SYMBOL" VARCHAR,
    "COMPANY NAME" VARCHAR,
    "SERIES" VARCHAR,
    "PURPOSE" VARCHAR,
    "FACE VALUE" INTEGER,
    "EX-DATE" DATE
  ),
);
