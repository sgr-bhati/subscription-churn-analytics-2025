# 📄 Day 2 – Data Cleaning & Modernization Report
**Project:** Subscription Retention & CLTV Analytics  
**Dataset:** Telco Customer Churn  
**Objective:** Clean and modernize the dataset for 2025-ready OTT/SaaS analytics.

---

## 1. Overview
Day 2 focuses on:
- Cleaning raw Telco data  
- Fixing missing values and incorrect types  
- Modernizing columns for OTT/SaaS subscription use cases  
- Creating new behavioral features  
- Ensuring readiness for Day 3 EDA & modeling

---

## 2. Data Cleaning Tasks Completed

### 2.1 Handling Missing Values
- Converted blank `TotalCharges` to `NaN`
- Cast `TotalCharges` to float
- Imputed missing values using **median**
- Verified no missing values in essential fields:
  - `TotalCharges`
  - `tenure`
  - `MonthlyCharges`
  - `Churn`

---

### 2.2 Fixing Data Types
| Column | Old Type | New Type | Reason |
|--------|----------|----------|--------|
| TotalCharges | object | float | Required for revenue metrics |
| tenure | int | int | Verified |
| MonthlyCharges | float | float | Clean |
| Churn | object | int (0/1) | Required for ML |

Text columns were cleaned: trimmed and lowercased(whereever req).

---


## 3. Modernization of Features

### 3.1 Directly Mapped Features
| Telco Column | Modern Name |
|--------------|-------------|
| customerID | customer_id |
| gender | gender |
| tenure | months_subscribed |
| MonthlyCharges | monthly_plan_cost |
| TotalCharges | total_revenue |
| Contract | subscription_type |
| PaymentMethod | payment_mode |
| Churn | subscription_canceled |

---

### 3.2 Transformed Features
| Telco Column | New Feature | Logic |
|--------------|-------------|--------|
| InternetService | streaming_quality | Plan speed maps to preferred streaming tier |
| StreamingTV, StreamingMovies | app_usage_hours, last30d_usage_hours, is_active_last30d | Maps entertainment interest to OTT usage |
| MultipleLines | num_profiles | Multiple lines ↔ multi-profile households |
| TechSupport | support_tickets_last6m | Tech support users tend to raise fewer tickets |
| PaperlessBilling | auto_renew | Suggests saved card → auto-renew enabled |

---

## 4. New Feature Engineering

| New Feature | Purpose |
|-------------|----------|
| customer_rating | Satisfaction score for retention modeling |
| nps_score | Churn/advocacy predictor |
| promo_email_clicks | Measures marketing engagement |
| device_type | Identifies primary streaming device |

---

## 5. Validation & Quality Checks
- No missing values in essential modeling fields  
- All numeric fields validated  
- Outliers preserved unless erroneous  
- Categorical values standardized  
- Modern schema aligned with Day 1 documentation  

---

## 6. Summary
Day 2 successfully:
- Cleaned the dataset  
- Modernized Telco‐era features  
- Created new SaaS/OTT behavioral metrics  
- Ensured the dataset is ready for Day 3 EDA

The dataset is now **modeling-ready**.


