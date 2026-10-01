"""
YRBSS Physical Activity Trend Analysis
Source: CDC Nutrition, Physical Activity, and Obesity - YRBSS
2011-2023, U.S. high school students
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("yrbss.db")

# --- Query 1: National trend by sex - "60+ min/day activity" ---
q1 = """
SELECT YearStart, Sex, Data_Value AS Percent
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'-
  AND StratificationCategory1 = 'Sex'
ORDER BY YearStart, Sex;
"""
df_activity = pd.read_sql(q1, conn).dropna()

# --- Query 2: National trend by sex - "daily PE class participation" ---
q2 = """
SELECT YearStart, Sex, Data_Value AS Percent
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who participate in daily physical education'
  AND StratificationCategory1 = 'Sex'
ORDER BY YearStart, Sex;
"""
df_pe = pd.read_sql(q2, conn).dropna()

conn.close()

# ============================================================
# Chart 1: Physical activity trend by sex
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

for sex, color in [("Female", "#d1495b"), ("Male", "#2e86ab")]:
    sub = df_activity[df_activity["Sex"] == sex]
    axes[0].plot(sub["YearStart"], sub["Percent"], marker="o", label=sex, color=color, linewidth=2)

axes[0].set_title("60+ Minutes of Daily Physical Activity\n(U.S. high school students, national)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Percent (%)")
axes[0].legend()
axes[0].grid(alpha=0.3)
axes[0].set_ylim(0, 45)

for sex, color in [("Female", "#d1495b"), ("Male", "#2e86ab")]:
    sub = df_pe[df_pe["Sex"] == sex]
    axes[1].plot(sub["YearStart"], sub["Percent"], marker="o", label=sex, color=color, linewidth=2)

axes[1].set_title("Daily Physical Education Participation\n(U.S. high school students, national)")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Percent (%)")
axes[1].legend()
axes[1].grid(alpha=0.3)
axes[1].set_ylim(0, 45)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/yrbss_physical_activity_trend.png", dpi=150)
print("Chart saved.")

# ============================================================
# Print summary tables to console
# ============================================================
print("\n--- Physical Activity (60+ min/day) ---")
print(df_activity.pivot(index="YearStart", columns="Sex", values="Percent"))

print("\n--- Daily PE Participation ---")
print(df_pe.pivot(index="YearStart", columns="Sex", values="Percent"))
