# Data Dictionary — Modernized Subscription Dataset (OTT/SaaS 2025)

This dictionary adds new behavioral and platform-relevant features to transform the dataset
into a 2025-ready subscription/OTT churn prediction problem.

## Core Account Structure (From Raw Dataset)
Columns retained from the raw dataset:
customerID, gender, SeniorCitizen, Partner, Dependents,
tenure, Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn

## Modern Engagement Features
| Column Name            | Type   | Description |
|------------------------|--------|-------------|
| daily_watch_minutes    | float  | Average minutes watched per day on the app. |
| viewing_hours_last_30d | float  | Total hours watched in the last 30 days. |
| num_profiles           | int    | Number of user profiles on the account. |
| preferred_genre        | category | User's most watched genre (Drama/Action/Sports/etc.). |
| device_type            | category | Primary viewing device (Mobile/TV/Laptop/Multiple). |
| ad_interactions        | int    | Count of ads clicked or skipped. |

## Experience & Satisfaction Indicators
| Column Name         | Type   | Description |
|---------------------|--------|-------------|
| app_rating          | float  | User's in-app satisfaction rating (1–5 scale). |
| customer_support_calls | int | Number of customer support queries made. |

## Pricing Sensitivity & Payments
| Column Name              | Type     | Description |
|--------------------------|----------|-------------|
| offer_redemption_count   | int      | Number of promo codes or offers redeemed. |
| last_payment_success     | category | Whether the last payment attempt succeeded. |
| auto_renewal             | bool     | Whether auto-renew is enabled. |
| subscription_type        | category | Free / Basic / Standard / Premium plan tier. |

