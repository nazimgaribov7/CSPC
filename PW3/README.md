# Practical Work 3: Data, Distributions, Testing, and Causation

## 1. Introduction

The goal of this practical work is to analyse two datasets using Python, pandas, NumPy, SciPy, and Matplotlib. The analysis includes descriptive statistics, normality tests, comparison of groups, correlation analysis, and a discussion of correlation versus causation.

## 2. Heart Disease Dataset

The dataset contains 303 observations and 14 columns. No missing values were found.

### 2.1 Descriptive Statistics

| Variable | Mean | Standard deviation | Median |
|---|---:|---:|---:|
| Age | 54.44 | 9.04 | 56 |
| Cholesterol (chol) | 246.69 | 51.78 | 241 |
| Resting blood pressure (trestbps) | 131.69 | 17.60 | 130 |
| Maximum heart rate (thalach) | 149.61 | 22.88 | 153 |

### 2.2 Normality Tests

The D’Agostino-Pearson normality test was applied to age, cholesterol, resting blood pressure, and maximum heart rate.

All four variables had p-values below 0.05. Therefore, the null hypothesis of normality was rejected for each variable at the 5% significance level.

The histograms are saved in `distributions.png`.

### 2.3 Comparison Between Groups

Maximum heart rate was compared between the two target groups using Welch’s t-test.

- Target 0 mean: 158.38
- Target 1 mean: 139.26
- t-statistic: 7.86
- p-value: approximately 9.11 × 10⁻¹⁴

Since the p-value is below 0.05, there is a statistically significant difference in mean maximum heart rate between the two groups.

The comparison is visualised in `thalach_comparison.png`.

### 2.4 Correlation Between Age and Maximum Heart Rate

Pearson’s correlation coefficient was calculated for age and maximum heart rate.

- Correlation coefficient: -0.394
- p-value: approximately 1.11 × 10⁻¹²

The results show a moderate negative correlation: older participants tend to have lower maximum heart rates in this dataset. However, correlation alone does not prove causation.

The relationship is shown in `age_thalach.png`.

## 3. Chemicals and Cancer Dataset

The second dataset contains 1,000 observations and five variables: benzene, cadmium, pollution index, age, and malignancy.

### 3.1 Correlation Analysis

Pearson correlation coefficients were calculated between each explanatory variable and malignancy.

| Variable | Correlation with malignancy | p-value |
|---|---:|---:|
| Benzene | 0.385 | < 0.001 |
| Cadmium | 0.880 | < 0.001 |
| Pollution index | 0.895 | < 0.001 |
| Age | -0.034 | 0.285 |

Benzene, cadmium, and pollution index show positive correlations with malignancy. The correlations for cadmium and pollution index are particularly strong. Age does not show a statistically significant linear correlation with malignancy at the 5% significance level.

### 3.2 Correlation Versus Causation

Cadmium and pollution index are very strongly correlated with each other (r = 0.982). This means their effects cannot be easily distinguished using simple correlation analysis alone.

Although several variables are associated with malignancy, these associations do not establish that the variables cause cancer. Other variables, confounding factors, and the way the data were generated may influence the observed relationships.

To establish causation, additional evidence and an appropriate study design would be required.

The scatter plots are saved as `benzene_malignancy.png`, `cadmium_malignancy.png`, `pollution_index_malignancy.png`, and `age_malignancy.png`.

## 4. Conclusion

This practical work demonstrated how to load and analyse data with pandas, summarise distributions, test normality, compare groups, and measure correlations.

The heart dataset showed non-normal distributions for the four examined variables, a significant difference in maximum heart rate between target groups, and a moderate negative correlation between age and maximum heart rate.

The chemicals dataset showed strong associations between malignancy and several chemical-related variables. However, the results also demonstrated why correlation should not be interpreted as proof of causation.

## 5. Files Generated

- `analysis.py` — Python analysis script.
- `distributions.png` — Histograms of heart dataset variables.
- `thalach_comparison.png` — Maximum heart rate comparison.
- `age_thalach.png` — Age versus maximum heart rate.
- `benzene_malignancy.png` — Benzene versus malignancy.
- `cadmium_malignancy.png` — Cadmium versus malignancy.
- `pollution_index_malignancy.png` — Pollution index versus malignancy.
- `age_malignancy.png` — Age versus malignancy.
