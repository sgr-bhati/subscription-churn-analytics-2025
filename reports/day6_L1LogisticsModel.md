# Day 6 – L1 Logistic Regression Model (Churn Prediction)

## Objective
To build an interpretable churn prediction model using **L1-regularized Logistic Regression**, optimized for churn recall while maintaining business usability through threshold tuning and actionable outputs.

---

## Modeling Path Selection
Based on Day 5 feature selection results:
- **Logistic Model Path** → Correlated features removed
- **Tree Model Path** → To be explored separately (Day 7)

This day focuses exclusively on the **Logistic Model Path**.

---

## Data Preparation
- Used **scaled and feature-reduced dataset** from Day 5
- **Train–test split reused** from Day 5 to avoid data leakage
- Scaling fitted **only on training data**, applied to test data
- Same `random_state` maintained for reproducibility

---

## Model Choice
- **Model:** Logistic Regression with **L1 regularization**
- **Rationale:**
  - Sparse feature selection
  - High interpretability
  - Suitable for churn modeling

---

## Hyperparameter Tuning
- **Technique:** GridSearchCV
- **Metric:** ROC-AUC
- **Best Regularization Strength (C):** `0.1`

---

## Initial Model Performance (Baseline)
- Churn recall was low (~49%)
- Model biased toward majority (non-churn) class

This prompted **class imbalance handling**.

---

## Class Imbalance Treatment
- Applied `class_weight = "balanced"`
- Resulted in:
  - Significant improvement in **churn recall**
  - Acceptable trade-off in precision
  - Stable ROC-AUC

---

## Threshold Optimization
- Default threshold (0.50) was suboptimal
- Tested thresholds in range **0.30–0.80**
- **Best threshold selected:** `0.55`

This balanced:
- Churn recall
- Precision
- Operational feasibility

---

## Final Model Performance (Threshold = 0.55)

| Class | Precision | Recall | F1-score | Support |
|------|----------|--------|---------|---------|
| Non-Churn (0) | 0.91 | 0.74 | 0.82 | 1552 |
| Churn (1) | 0.53 | 0.81 | 0.64 | 561 |

**Overall Accuracy:** 76%  
**Key Win:** High churn recall (81%) with controlled precision

---

## Risk Segmentation of Flagged Customers
Customers flagged for retention were segmented by predicted churn probability:

- **High Risk (60–80%)** → Majority segment
- **Very High Risk (80%+)** → Critical churn candidates
- **Moderate Risk (49–60%)** → Early intervention group
- **Low Risk (<49%)** → Not targeted

This segmentation enables **prioritized retention strategies**.

---

## Model Interpretability – L1 Coefficients

### Top Churn Drivers (Positive Coefficients)
| Feature | Interpretation |
|------|---------------|
| `months_subscribed` | Tenure-related churn risk |
| `payment_mode_Mailed check` | Manual payment friction |
| `gender_Male` | Behavioral signal |
| `nps_score` | Customer sentiment impact |

---

### Top Retention Drivers (Negative Coefficients)
| Feature | Interpretation |
|------|---------------|
| `streaming_quality` | Product experience |
| `auto_renew` | Reduced churn intent |
| `device_type_Mobile` | Usage convenience |
| `payment_mode_Electronic check` | Seamless billing |

> L1 regularization automatically zeroed out weak or redundant features, ensuring sparsity and clarity.

---

## Model Artifacts & Delivery

- **Saved Model:**  
  `final_l1_logistic_model.joblib`

- **Saved Actionable Predictions:**  
  `l1_churn_predictions_ACTIONABLE.csv`

---

## Final Delivery Summary
- **Total customers evaluated:** 2113  
- **Customers flagged for retention:** 876  

---

## Key Takeaways
- Class imbalance handling was the **most impactful improvement**
- Threshold tuning aligned the model with **business objectives**
- L1 regularization delivered both **performance and interpretability**
- Outputs are **actionable, explainable, and production-ready**

---

**Day 6 successfully completed.**


