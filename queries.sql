-- ============================================================
-- YRBSS Physical Activity Analysis - SQL Queries
-- Data source: CDC Nutrition, Physical Activity, and Obesity - YRBSS
-- ============================================================

-- 1) National-level trend by sex, by year
--    "1+ hour of moderate/vigorous physical activity daily"
SELECT
    YearStart,
    Sex,
    Data_Value AS Percent
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'
  AND StratificationCategory1 = 'Sex'
ORDER BY YearStart, Sex;


-- 2) National-level trend by sex, by year
--    "Daily physical education class participation"
SELECT
    YearStart,
    Sex,
    Data_Value AS Percent
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who participate in daily physical education'
  AND StratificationCategory1 = 'Sex'
ORDER BY YearStart, Sex;


-- 3) States with the largest decline between 2013 and 2023
--    (window function: LAG for year-over-year comparison)
WITH state_trend AS (
    SELECT
        LocationDesc,
        YearStart,
        Data_Value AS Percent,
        LAG(Data_Value) OVER (
            PARTITION BY LocationDesc
            ORDER BY YearStart
        ) AS Prev_Value
    FROM physical_activity
    WHERE Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'
      AND StratificationCategory1 = 'Total'
      AND YearStart IN (2013, 2023)
      AND LocationDesc != 'National'
)
SELECT
    LocationDesc,
    MAX(CASE WHEN YearStart = 2013 THEN Percent END) AS Pct_2013,
    MAX(CASE WHEN YearStart = 2023 THEN Percent END) AS Pct_2023,
    MAX(CASE WHEN YearStart = 2023 THEN Percent END)
        - MAX(CASE WHEN YearStart = 2013 THEN Percent END) AS Change
FROM physical_activity
WHERE Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'
  AND StratificationCategory1 = 'Total'
  AND YearStart IN (2013, 2023)
  AND LocationDesc != 'National'
GROUP BY LocationDesc
HAVING Pct_2013 IS NOT NULL AND Pct_2023 IS NOT NULL
ORDER BY Change ASC
LIMIT 10;


-- 4) How has the gender gap changed over the years?
SELECT
    YearStart,
    MAX(CASE WHEN Sex = 'Male' THEN Data_Value END) AS Male_Pct,
    MAX(CASE WHEN Sex = 'Female' THEN Data_Value END) AS Female_Pct,
    MAX(CASE WHEN Sex = 'Male' THEN Data_Value END)
        - MAX(CASE WHEN Sex = 'Female' THEN Data_Value END) AS Gender_Gap
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'
  AND StratificationCategory1 = 'Sex'
GROUP BY YearStart
ORDER BY YearStart;
