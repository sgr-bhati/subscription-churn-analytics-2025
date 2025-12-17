
## **1. Train–Test Split & X–Y Separation**
- Separated **X (features)** and **y (subscription_canceled)**.  
- Performed **train–test split** before any scaling.  
- All scalers were **fit only on X_train** and then applied to both X_train and X_test to avoid data leakage.

---

## **2. Feature Scaling**
Scaling was applied only where meaningful:

### **2.1 MinMaxScaler Group**
Used for features with wider or varied ranges:
- `streaming_quality`
- `subscription_type`
- `customer_rating`
- `promo_email_clicks`
- `num_profiles`
- `support_tickets_last6m`
- `nps_score`

### **2.2 StandardScaler Group**
Used for continuous magnitude-based features:
- `months_subscribed`
- `monthly_plan_cost`
- `total_revenue_log` (after outlier treatment on Day 4)
- `app_usage_hours`
- `last30d_usage_hours`

### **2.3 No Scaling Applied To**
- Binary variables (already 0–1)
- One-hot encoded categorical columns  
These do not benefit from scaling.

---

## **3. Feature Selection – Pearson Correlation**
- Computed a **Pearson correlation matrix** on scaled training data.
- Identified **highly correlated feature pairs**.
- For logistic regression, correlated features must be removed to avoid multicollinearity.
- For tree-based models, these correlated features **do not harm model performance**, so they can be retained.

Based on the correlation results, a set of recommended features for logistic regression was finalized (as per screenshot shared).

---

## **4. Outcome of Day 5**
At the end of Day 5:

### ✔ Feature scaling completed using a grouped-scaler approach  
### ✔ Feature selection completed using Pearson correlation  
### ✔ Identified features to drop **only for logistic regression**  
### ✔ Decided to follow a **two-model strategy**:
1. **Logistic Regression Model**  
2. **Tree-Based Model (Decision Tree / Random Forest / XGBoost)**  
(because tree models are not affected by multicollinearity)

Model building will begin on **Day 6**.

---

