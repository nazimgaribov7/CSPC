import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")

print("=== FIRST LOOK AT THE DATA ===")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

columns = ["age", "chol", "trestbps", "thalach"]

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df[columns].describe())

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

df[columns].hist(figsize=(10, 8), bins=20)
plt.suptitle("Distributions of Heart Dataset Variables")
plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

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

plt.figure(figsize=(7, 5))
plt.boxplot([group0, group1], tick_labels=["Target 0", "Target 1"])
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Maximum Heart Rate by Target Group")
plt.tight_layout()
plt.savefig("thalach_comparison.png")
plt.close()

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

print("\n=== CORRELATION MATRIX ===")
print(chem.corr(numeric_only=True).round(3))

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

print("\n=== 95% CONFIDENCE INTERVALS ===")

for label, group in [(0, group0), (1, group1)]:
    mean = group.mean()
    confidence_interval = stats.t.interval(
        0.95,
        df=len(group) - 1,
        loc=mean,
        scale=stats.sem(group)
    )

    print(f"Target {label}:")
    print(f"  Mean = {mean:.2f}")
    print(
        f"  95% confidence interval = "
        f"({confidence_interval[0]:.2f}, "
        f"{confidence_interval[1]:.2f})"
    )

means = [group0.mean(), group1.mean()]
intervals = []

for group in [group0, group1]:
    ci = stats.t.interval(
        0.95,
        df=len(group) - 1,
        loc=group.mean(),
        scale=stats.sem(group)
    )
    intervals.append(ci)

errors = [
    [means[i] - intervals[i][0] for i in range(2)],
    [intervals[i][1] - means[i] for i in range(2)]
]

plt.figure(figsize=(7, 5))
plt.errorbar(
    ["Target 0", "Target 1"],
    means,
    yerr=errors,
    fmt="o",
    capsize=6
)
plt.ylabel("Mean maximum heart rate (thalach)")
plt.title("Mean Maximum Heart Rate with 95% Confidence Intervals")
plt.tight_layout()
plt.savefig("thalach_confidence_intervals.png")
plt.close()


print("\n=== TARGET CATEGORY BALANCE ===")

proportions = df["target"].value_counts(normalize=True).sort_index()
print("Target proportions:")
print(proportions)

entropy = -sum(p * np.log2(p) for p in proportions if p > 0)
print(f"Entropy = {entropy:.3f} bits")

print(
    "Maximum possible entropy for two equally balanced categories = 1 bit."
)
