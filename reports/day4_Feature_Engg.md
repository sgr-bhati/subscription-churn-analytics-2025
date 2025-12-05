# Feature Engineering – Day 4 Report

## 1. Missing Values Identification & Treatment
- Checked the entire dataset for missing values.
- No columns had any missing entries.
- **Conclusion:** No imputation or treatment required.

## 2. Handling Categorical Columns
Categorical features were divided into three groups:

### 2.1 Columns Not Useful for Modeling
- **CustomerID**: Dropped as it is not a predictive feature.

### 2.2 Ordinal Categorical Columns (Label Encoding)
- **Subscription Type**: 
  - Monthly → 0 
  - Yearly → 1 
  - Two-Yearly → 2
- **Streaming Quality**: 
  - SD → 0 
  - HD → 1 
  - 4K → 2

### 2.3 Nominal Categorical Columns (One-Hot Encoding)
Applied OHE to:
- Gender
- Payment Mode
- Device Type

## 3. Derived Features
- Skipped on Day 4 as all derived features were already created during Day 2 dataset modernization.

## 4. Outlier Detection & Treatment

### 4.1 Skewness-Based Feature Separation
- **High-Skewed Features (skewness > 0.5):** Added to `high_skewed_cols`  
- **Low-Skewed / Near-Normal Features (skewness ≤ 0.5):** Added to `low_skewed_cols`

### 4.2 Outlier Detection Methods
- **High-Skewed Features:** MAD (Median Absolute Deviation) Score Test  
- **Low-Skewed Features:** Z-Score Test

### 4.3 MAD Score Test Results
- **Total Revenue:** ~2% outliers  
- **Promo Email Clicks:** ~0.3% outliers (synthetic feature; skipped treatment)

### 4.4 Z-Score Test Results
- **Last30DayUsageHours:** ~0.2% outliers (synthetic feature; skipped treatment due to random multiplier applied during feature generation)

### 4.5 Outlier Treatment Decisions
- **Total Revenue:** Treated using **log1p transformation** (`np.log1p(x)`)  
  - Handles zero values  
  - Compresses long right tail  
  - Retains relative order  
  - Reduces impact of extreme values
- **Promo Email Clicks & Last30DayUsageHours:** Outlier treatment skipped  
  - Synthetic features  
  - Removing outliers would distort natural distribution and remove genuine high-engagement/high-usage behavior

## 5. Saving Feature-Engineered Dataset
- After completing all steps, the **feature-engineered dataset** was saved as a **Treated_subscriptions_churn.csv** for further use in modeling.

