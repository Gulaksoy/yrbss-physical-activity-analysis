# Youth Physical Activity Trends: A CDC YRBSS Analysis (2011–2023)

## Overview
This project analyzes CDC's Youth Risk Behavior Surveillance System (YRBSS) data to examine trends in physical activity and physical education (PE) participation among U.S. high school students between 2011 and 2023. The analysis combines SQL-based data exploration, Python visualization, and domain expertise from 17 years of experience as a physical education teacher.

**Data source:** [CDC Nutrition, Physical Activity, and Obesity — YRBSS](https://data.cdc.gov/Youth-Risk-Behaviors/Nutrition-Physical-Activity-and-Obesity-Youth-Ris/vba9-s8jp)

## Tools Used
- **SQL (SQLite)** — data querying, window functions (`LAG`), conditional aggregation
- **Python (pandas, matplotlib)** — data transformation and visualization
- **DB Browser for SQLite** — database management

## Project Files
| File | Description |
|---|---|
| `yrbss.db` | SQLite database (Physical Activity subset of YRBSS data) |
| `queries.sql` | Four SQL queries used in this analysis |
| `analysis.py` | Python script generating the trend chart |
| `yrbss_physical_activity_trend.png` | Visualization of key trends |

## Key Findings

**1. Physical activity has declined, and the gender gap persists.**
The share of students reporting 60+ minutes of daily physical activity fell from 38.3% (male) / 18.5% (female) in 2011 to 32.2% / 16.6% in 2023. Male participation has consistently been roughly double that of female participation throughout the period.

**2. Daily PE participation collapsed during the pandemic and has not recovered.**
Daily PE attendance dropped sharply in 2021 (16.7% female, 21.1% male) — the lowest point in the 2001–2023 series — and remains below pre-pandemic (2017) levels as of 2023.

**3. State-level declines vary dramatically.**
Between 2013 and 2023, Oklahoma saw the steepest drop (-11.7 points), roughly double the decline of most other states in the bottom 10. Several of the largest declines cluster in the South/Southwest, though this would need broader state-level comparison to confirm as a regional pattern.

**4. The narrowing gender gap reflects decline, not progress.**
The gap between male and female activity rates shrank from 19.8 points (2011) to 15.6 points (2023) — not because girls became more active, but because boys' activity rates declined faster than girls'.

## Interpretation (from 17 years of classroom experience)

The dataset does not measure *why* activity has declined — that requires qualitative insight. Based on my experience teaching PE in Turkish public schools (2005–2022), two factors stand out as likely contributors:

**Digital engagement as a social necessity, not just entertainment.** Games like Roblox have become less about the activity itself and more about social belonging — students who have never played a game will still ask to download it simply to avoid being excluded from classroom conversations about it. This peer-driven pull is, in my observation, often stronger than the appeal of the game itself.

**Declining perceived safety of outdoor environments.** Parents increasingly hesitate to let children play outside independently due to traffic and safety concerns, compared to previous generations. This pushes children toward indoor, individual activities by default rather than by choice.

These are hypotheses grounded in direct classroom observation, not conclusions drawn from this dataset — a distinction worth keeping clear in any discussion of this analysis.

## Policy Implications
- Schools that cut PE time during pandemic scheduling adjustments should prioritize restoring it, given the data shows no organic recovery by 2023.
- Programs addressing the social dynamics of screen time (not just "screen time limits") may be more effective than restriction-only approaches.
- States with outlier declines (e.g., Oklahoma) warrant case-study investigation into specific policy or budget changes during this period.

## Next Steps
- Extend analysis to race/ethnicity stratification
- Build an interactive dashboard (Tableau Public / Streamlit) for state-level exploration
- Add statistical significance testing for the observed trends
