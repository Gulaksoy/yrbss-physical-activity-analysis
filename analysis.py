"""
YRBSS Fiziksel Aktivite Trend Analizi
Kaynak: CDC Nutrition, Physical Activity, and Obesity - YRBSS
2011-2023 arası, ABD lise öğrencileri
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("yrbss.db")

# --- Sorgu 1: Ulusal düzeyde cinsiyete göre "günde 60+ dk aktivite" trendi ---
q1 = """
SELECT YearStart, Sex, Data_Value AS Percent
FROM physical_activity
WHERE LocationDesc = 'National'
  AND Question = 'Percent of students in grades 9-12 who achieve 1 hour or more of moderate-and/or vigorous-intensity physical activity daily'
  AND StratificationCategory1 = 'Sex'
ORDER BY YearStart, Sex;
"""
df_activity = pd.read_sql(q1, conn).dropna()

# --- Sorgu 2: Ulusal düzeyde cinsiyete göre "günlük PE dersi" trendi ---
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
# Grafik 1: Fiziksel aktivite trendi (cinsiyete göre)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

for sex, color in [("Female", "#d1495b"), ("Male", "#2e86ab")]:
    sub = df_activity[df_activity["Sex"] == sex]
    axes[0].plot(sub["YearStart"], sub["Percent"], marker="o", label=sex, color=color, linewidth=2)

axes[0].set_title("Günde 60+ Dakika Fiziksel Aktivite\n(ABD lise öğrencileri, ulusal)")
axes[0].set_xlabel("Yıl")
axes[0].set_ylabel("Yüzde (%)")
axes[0].legend()
axes[0].grid(alpha=0.3)
axes[0].set_ylim(0, 45)

for sex, color in [("Female", "#d1495b"), ("Male", "#2e86ab")]:
    sub = df_pe[df_pe["Sex"] == sex]
    axes[1].plot(sub["YearStart"], sub["Percent"], marker="o", label=sex, color=color, linewidth=2)

axes[1].set_title("Her Gün Beden Eğitimi Dersine Katılım\n(ABD lise öğrencileri, ulusal)")
axes[1].set_xlabel("Yıl")
axes[1].set_ylabel("Yüzde (%)")
axes[1].legend()
axes[1].grid(alpha=0.3)
axes[1].set_ylim(0, 45)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/yrbss_physical_activity_trend.png", dpi=150)
print("Grafik kaydedildi.")

# ============================================================
# Konsola özet tablo bas
# ============================================================
print("\n--- Fiziksel Aktivite (60+ dk/gün) ---")
print(df_activity.pivot(index="YearStart", columns="Sex", values="Percent"))

print("\n--- Günlük PE Katılımı ---")
print(df_pe.pivot(index="YearStart", columns="Sex", values="Percent"))
