import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the heart disease dataset
df = pd.read_csv("heart.csv")

print("=== FIRST LOOK AT THE DATA ===")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# 1. Describe the distributions
columns = ["age", "chol", "trestbps", "thalach"]

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[columns].describe())

# 2. Check normality
print("\n=== NORMALITY TESTS ===")
for column in columns:
    data = df[column].dropna()
    statistic, p_value = stats.normaltest(data)

    print(f"\n{column}:")
    print(f"  p-value = {p_value:.5f}")

    if p_value < 0.05:
        print("  The distribution is not normally distributed.")
    else:
        print("  There is not enough evidence against normality.")

# Plot histograms
df[columns].hist(figsize=(10, 8), bins=20)
plt.suptitle("Distributions of Heart Dataset Variables")
plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

# 3. Compare maximum heart rate between target groups
group0 = df[df["target"] == 0]["thalach"].dropna()
group1 = df[df["target"] == 1]["thalach"].dropna()

print("\n=== COMPARISON OF THALACH ===")
print("Target 0: mean =", group0.mean())
print("Target 1: mean =", group1.mean())

t_statistic, p_value = stats.ttest_ind(
    group0, group1, equal_var=False
)

print("Welch t-test statistic:", t_statistic)
print("Welch t-test p-value:", p_value)

if p_value < 0.05:
    print("The groups differ significantly.")
else:
    print("There is no statistically significant difference.")

# Boxplot
plt.figure(figsize=(7, 5))
plt.boxplot([group0, group1], tick_labels=["Target 0", "Target 1"])
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Maximum Heart Rate by Target Group")
plt.tight_layout()
plt.savefig("thalach_comparison.png")
plt.close()

# 4. Relationship between age and maximum heart rate
correlation, p_value = stats.pearsonr(df["age"], df["thalach"])

print("\n=== AGE AND MAXIMUM HEART RATE ===")
print("Pearson correlation:", correlation)
print("p-value:", p_value)

plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Age vs Maximum Heart Rate")
plt.tight_layout()
plt.savefig("age_thalach.png")
plt.close()

print("\nAnalysis complete. Three plots have been saved.")
# 5. Chemical exposure and cancer: correlation vs causation
chem = pd.read_csv("chemicals_cancer.csv")

print("\n=== CHEMICALS AND CANCER DATA ===")
print(chem.head())
print("\nDataset shape:", chem.shape)
print("\nDescriptive statistics:")
print(chem.describe())

print("\n=== CORRELATIONS WITH MALIGNANCY ===")
for column in ["benzene", "cadmium", "pollution_index", "age"]:
    r, p = stats.pearsonr(chem[column], chem["malignancy"])
    print(f"{column}: correlation = {r:.3f}, p-value = {p:.5g}")

# Correlation matrix
print("\n=== CORRELATION MATRIX ===")
print(chem.corr(numeric_only=True).round(3))

# Scatter plots
for column in ["benzene", "cadmium", "pollution_index", "age"]:
    plt.figure(figsize=(7, 5))
    plt.scatter(chem[column], chem["malignancy"], alpha=0.6)
    plt.xlabel(column)
    plt.ylabel("Malignancy")
    plt.title(f"{column} vs Malignancy")
    plt.tight_layout()
    plt.savefig(f"{column}_malignancy.png")
    plt.close()

print("\nChemical data analysis complete.")
