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
## 6. Distribution Shapes

The histograms show the following patterns:

- **Age:** The distribution is concentrated mainly around middle and older adulthood. It is not perfectly symmetric.
- **Cholesterol (chol):** The distribution is right-skewed, with some unusually high values.
- **Resting blood pressure (trestbps):** Most observations are concentrated around 120–140, with a tail towards higher values.
- **Maximum heart rate (thalach):** Values are concentrated around 140–170, with a tail towards lower values.

These visual observations agree with the normality tests, which rejected normality for all four variables at the 5% significance level.

## 7. Uncertainty in Mean Maximum Heart Rate

The means and 95% confidence intervals are:

| Target group | Mean thalach | 95% confidence interval |
|---|---:|---:|
| Target 0 | 158.38 | (155.42, 161.34) |
| Target 1 | 139.26 | (135.47, 143.05) |

The intervals do not overlap. This agrees with the Welch t-test, which found a statistically significant difference between the groups (p < 0.001).

The figure `thalach_confidence_intervals.png` displays the means and their 95% confidence intervals.

## 8. Bonus: Predictability of the Target Category

The proportions are:

- Target 0: 54.1%
- Target 1: 45.9%

The entropy is 0.995 bits, close to the maximum of 1 bit for two categories. The classes are therefore nearly balanced. Always guessing the majority category would give an accuracy of only about 54.1%.

## 9. Investigating the Chemical Mystery

In the full dataset, the correlations with malignancy are:

- Benzene: r = 0.385
- Cadmium: r = 0.880
- Pollution index: r = 0.895

A naive analysis would therefore make cadmium look like the stronger candidate.

However, cadmium and pollution index are extremely strongly correlated (r = 0.982). To investigate possible confounding, I restricted the analysis to observations with a pollution index between 40 and 60. This left 199 observations.

Within this restricted group:

- Benzene and malignancy: r = 0.702
- Cadmium and malignancy: r = 0.316

The association with benzene remains strong, while the association with cadmium becomes much weaker. This supports the interpretation that benzene is the intended causal chemical in this synthetic dataset, whereas cadmium appeared more strongly associated because it tracked the pollution index.

This is evidence consistent with confounding, not mathematical proof of causation. Restricting the pollution range does not control every possible confounder, and causal conclusions depend on how the synthetic data were generated.

## 10. Data Source and Method Limitations

The heart disease dataset is the Cleveland heart disease dataset, associated with the UCI Machine Learning Repository and also distributed through Kaggle.

The normality tests, Welch's t-test, and Pearson correlations quantify patterns in the observed data. Statistical significance does not by itself establish practical importance or causation. The chemical dataset is synthetic, so conclusions about its intended causal mechanism should not be generalised directly to real patients.

References:
- UCI Machine Learning Repository, Heart Disease dataset: https://archive.ics.uci.edu/dataset/45/heart+disease
- Kaggle, Heart Disease dataset: https://www.kaggle.com/datasets
