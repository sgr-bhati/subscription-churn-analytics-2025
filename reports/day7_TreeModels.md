# Day 7 — Tree-Based Models Report (Random Forest & XGBoost)

## Objective
Build, tune, and evaluate tree-based churn models using the Day-4 feature-engineered dataset (no scaling / no feature removal). Produce actionable prediction files and save model artifacts for handoff to retention teams.

---

## Data & Pipeline Notes
- **Dataset used:** Day-4 feature-engineered dataset (missing values handled, categorical encoded, derived features present).  
- **Splits:** Performed X / y separation and train–test split prior to modeling.  
- **No scaling or feature dropping** was applied for tree models (trees handle raw / encoded features well).

---

## Modeling Workflow (common)
1. Train a **base model** to establish baseline metrics.  
2. Hyperparameter search:
   - **Random Forest:** `GridSearchCV` (CV=5) — exhaustive-ish search (~2160 parameter combos evaluated).  
   - **XGBoost:** `RandomizedSearchCV` (with early stopping during training to reduce overfitting / runtime).  
3. Select best estimator from CV.  
4. Evaluate at default threshold (0.5).  
5. Perform **probability threshold tuning** (business / cost-sensitive): evaluated thresholds in a wide range (0.20–0.80) and selected final thresholds based on recall/precision trade-offs and operational cost.  
6. Extract feature importances and produce actionable CSVs.  
7. Save final model artifacts.

---

## 1) Random Forest (RF)

### Base RF
- **Base parameters:**  
  `{'class_weight': 'balanced', 'max_depth': 10, 'min_samples_split': 10, 'n_estimators': 300}`
- **Performance:**  
  - Train ROC AUC: **0.8360**  
  - Test ROC AUC: **0.8452**

**Classification Report (threshold = 0.5, base):**
- Class 0 — precision: 0.90 | recall: 0.80 | f1: 0.85 (support 1552)  
- Class 1 — precision: 0.58 | recall: 0.74 | f1: 0.65 (support 561)  
- **Accuracy:** 0.79

---

### Tuned RF (GridSearchCV, CV=5)
- **Optimal RF parameters found:**  
  `{'class_weight': 'balanced', 'max_depth': 10, 'max_features': 'sqrt', 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 300}`
- **Performance:**  
  - CV ROC AUC (train): **0.8374**  
  - Test ROC AUC: **0.8459**

**Classification Report (threshold = 0.5, tuned):**
- Class 0 — precision: 0.90 | recall: 0.80 | f1: 0.85  
- Class 1 — precision: 0.58 | recall: 0.75 | f1: 0.65  
- **Accuracy:** 0.79

---

### Threshold Tuning (Cost-Sensitive)
- Evaluated thresholds 0.20 → 0.80 to optimize business objective (churn recall vs campaign cost).  
- **Selected threshold:** **0.38** (business decision: maximize churn coverage while keeping precision acceptable).

**Classification Report (threshold = 0.38):**
- Class 0 — precision: 0.93 | recall: 0.69 | f1: 0.79  
- Class 1 — precision: 0.50 | recall: 0.85 | f1: 0.63  
- **Accuracy:** 0.73

**Decision rationale:** at 0.38 recall for churners is high (85%) — good for retention coverage; precision 50% keeps campaign waste manageable.

---

### RF — Top 10 Feature Importances
1. `subscription_type` — 0.196862  
2. `months_subscribed` — 0.162268  
3. `total_revenue_log` — 0.119659  
4. `monthly_plan_cost` — 0.117116  
5. `streaming_quality` — 0.0984952  
6. `payment_mode_Electronic check` — 0.0528582  
7. `last30d_usage_hours` — 0.0511358  
8. `app_usage_hours` — 0.0439437  
9. `nps_score` — 0.030434  
10. `promo_email_clicks` — 0.0242386

---

## 2) XGBoost (XGB)

### Base XGBoost
- **Base parameters:**  
  `{'subsample': 0.8, 'n_estimators': 200, 'max_depth': 5, 'learning_rate': 0.05, 'colsample_bytree': 0.8}`
- **Performance:**  
  - Train ROC AUC: **0.9433** (indicates strong fit on train)  
  - Test ROC AUC: **0.8386**

**Classification Report (threshold = 0.5, base):**
- Class 0 — precision: 0.90 | recall: 0.76 | f1: 0.82  
- Class 1 — precision: 0.53 | recall: 0.76 | f1: 0.63  
- **Accuracy:** 0.76

---

### Tuned XGBoost (RandomSearchCV + Early Stopping)
- **Optimal XGB parameters found:**  
  `{'subsample': 0.8, 'reg_lambda': 1, 'reg_alpha': 0.1, 'n_estimators': 2000, 'min_child_weight': 10, 'max_depth': 3, 'learning_rate': 0.05, 'gamma': 0, 'colsample_bytree': 0.8}`
- **Performance:**  
  - CV ROC AUC (train): **0.8436**  
  - Test ROC AUC: **0.8488** (best overall ROC AUC across tree models)

**Classification Report (threshold = 0.5, tuned):**
- Class 0 — precision: 0.92 | recall: 0.71 | f1: 0.80  
- Class 1 — precision: 0.51 | recall: 0.83 | f1: 0.63  
- **Accuracy:** 0.74

**Notes:** early stopping used during training to reduce overfitting and select appropriate boosting rounds.

---

### Threshold Tuning (Cost-Sensitive)
- Thresholds evaluated: 0.30 → 0.80; F1-optimized range observed 0.45–0.65.  
- **Selected threshold:** **0.46**

**Classification Report (threshold = 0.46):**
- Class 0 — precision: 0.94 | recall: 0.67 | f1: 0.78  
- Class 1 — precision: 0.49 | recall: 0.88 | f1: 0.63  
- **Accuracy:** 0.72

**Decision rationale:** at 0.46 churn recall is highest (88%), with acceptable precision (49%) — good for coverage-first retention campaigns.

---

### XGBoost — Top 10 Feature Importances
1. `subscription_type` — 0.354601  
2. `payment_mode_Electronic check` — 0.131761  
3. `streaming_quality` — 0.126007  
4. `months_subscribed` — 0.0662991  
5. `monthly_plan_cost` — 0.0393772  
6. `total_revenue_log` — 0.0376258  
7. `auto_renew` — 0.03314  
8. `payment_mode_Mailed check` — 0.0318367  
9. `gender_Male` — 0.0233966  
10. `device_type_SmartTV` — 0.019355

---

## 3) Model Comparison & Observations (summary)
- **ROC AUC (best):** XGBoost (0.849) > RandomForest (0.846) > L1 Logistic (0.836).  
- **Churn Recall (best):** XGBoost (88%) > RandomForest (85%) > L1 Logistic (81%).  
- **Precision (best):** L1 Logistic (53%) > RandomForest (50%) > XGBoost (49%).  
- **Accuracy (best):** L1 Logistic (76%) > RandomForest (73%) > XGBoost (72%).  
- **Interpretability:** L1 Logistic > RandomForest > XGBoost.  
- **Compute/Runtime:** XGBoost (heaviest) > RandomForest > Logistic.

**Trade-off insight:** XGBoost maximizes ranking & recall (best for coverage-driven retention); RF provides strong middle-ground; L1 Logistic is best for explainability and precision.

---

## 4) Artifacts & Actionables (saved)
Both models were finalized and artifacts produced (customized per model as discussed):

### Random Forest artifacts
- **Model:** `final_rf_churn_model.joblib`  
- **Actionables CSV:** `rf_churn_predictions_ACTIONABLE.csv`  
- **Threshold used:** `0.38` (for retention flagging)  
- **Notes:** Balanced class_weight, tuned hyperparams, saved top feature importance file (optional).

### XGBoost artifacts
- **Model:** `final_xgb_churn_model.joblib`  
- **Actionables CSV:** `xgb_churn_predictions_ACTIONABLE.csv`  
- **Threshold used:** `0.46` (for retention flagging)  
- **Notes:** Early stopping used, RandomSearchCV tuning, saved feature importance and SHAP (recommended) outputs if required.

> Each actionable CSV includes: original customer identifiers (if retained), churn probability, churn prediction (0/1), retention_flag ("YES"/"NO"), and key explanatory columns for outreach prioritization.

---

## 5) Next Proposed Steps
**Operational Considerations (Proposed — NOT implemented in this capstone)**
These are recommended `future` steps for productionization and A/B testing:
- **Pilot retention campaign:** Run the model on a limited sample, measure uplift, and estimate cost-per-retention.  
- **Threshold optimization by cost matrix:** Convert business costs (false negative vs false positive) into a loss matrix and select thresholds that minimize expected cost.  
- **Monitoring & retraining:** Implement data-drift and performance monitoring; schedule periodic retraining (monthly/quarterly) as needed.  
- **Explainability for operations:** Compute SHAP summaries per segment to aid call scripts and personalized retention offers.  
- **A/B testing & uplift measurement:** Test model-driven interventions vs control to quantify true ROI.

---

## Appendix / Quick References
- RF GridSearchCV combinations evaluated: ~**2160**  
- XGB tuning: **RandomSearchCV** + **early stopping**  
- Test-set size used for final reports: **2113** customers (actionable report size)  

---

**Day 7 complete.**  
Artifacts for both RandomForest and XGBoost have been saved and are ready for handoff or deployment. If you’d like, I can now:
- Generate the **final Day 7 markdown report file** for copy-paste,  
- Produce **deployment pipeline code** (scoring script + cron / job example), or  
- Create a **short executive slide** summarizing model choice and actionables.

