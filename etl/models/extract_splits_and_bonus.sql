MODEL (
  name support_data.splits_and_bonus_extract,
  kind FULL
);

WITH raw AS (
  SELECT * FROM support_data.splits_base
),
WITH cleaned AS (
  SELECT
    symbol,
    "company name" as company_name,
    purpose,
    regexp_replace(purpose, '[^a-zA-Z0-9]', '', 'g') as cleaned_purpose,
    "face value" as face_value,
    "ex-date" as ex_date
  FROM
    raw
)
WITH extracted AS (
  SELECT
    symbol,
    company_name,
    purpose,
    cleaned_purpose,
    face_value,
    ex_date,
    coalesce(
      NULLIF(regexp_extract(cleaned_purpose, 'SplitR[se]*([0-9]+)',1),''),
      NULLIF(regexp_extract(cleaned_purpose, 'FromR[se]([0-9]+)', 1),''),
      NULLIF(regexp_extract(cleaned_purpose, 'From.*([0-9]+)', 1),'')
    ) as split_from,
    coalesce(
      NULLIF(regexp_extract(cleaned_purpose, 'ToR[se]*([0-9]+)',1),''),
      NULLIF(regexp_extract(cleaned_purpose, 'ToR[es]*([0-9]+)', 1),''),
      NULLIF(regexp_extract(cleaned_purpose, 'To.*([0-9]+)', 1),'')
    ) as split_to,
    coalesce(
      NULLIF(regexp_extract(purpose, 'Bonus ([0-9]+):',1),''),
      NULLIF(regexp_extract(purpose, 'Bonus.*([0-9]+).*:',1),''),
    ) as bonus_left,
    coalesce(
      NULLIF(regexp_extract(purpose, 'Bonus [0-9]+:([0-9]+)',1),''),
      NULLIF(regexp_extract(purpose, 'Bonus.*[0-9]+.*:.*([0-9]+)',1),''),
    ) as bonus_right
  FROM
    cleaned
  WHERE PURPOSE ILIKE '%SPLIT%' OR PURPOSE ILIKE '%BONUS%'
)

select * from extracted
