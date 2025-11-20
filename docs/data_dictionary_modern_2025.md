# Data Dictionary — Modernized Subscription Dataset (OTT/SaaS 2025)

This dictionary adds new behavioral and platform-relevant features to transform the dataset
into a 2025-ready subscription/OTT churn prediction problem.


## Customer Information
| Column Name   | Type     | Description                                  |
| ------------- | -------- | -------------------------------------------- |
| `customer_id` | string   | Unique identifier assigned to each customer. |
| `gender`      | category | Gender of the customer (Male/Female).        |


## Subscription Details
| Column Name         | Type     | Description                                                            |
| ------------------- | -------- | ---------------------------------------------------------------------- |
| `months_subscribed` | int      | Total number of months the customer has been subscribed.               |
| `subscription_type` | category | The type of subscription plan chosen (e.g., Month-to-month, One year). |
| `streaming_quality` | category | Preferred streaming quality selected by the customer (HD/4K/etc.).     |
| `num_profiles`      | int      | Number of user profiles created under the account.                     |
| `auto_renew`        | int      | Auto-renewal status (1 = enabled, 0 = disabled).                       |


## Modern Engagement Features
| Column Name           | Type     | Description                                                                 |
| --------------------- | -------- | --------------------------------------------------------------------------- |
| `app_usage_hours`     | float    | Average daily app usage hours.                                              |
| `last30d_usage_hours` | float    | Total app usage hours in the last 30 days.                                  |
| `is_active_last30d`   | int      | Indicates if the customer was active in the last 30 days (1 = Yes, 0 = No). |
| `device_type`         | category | Primary device type used by the customer (Mobile/TV/Web/etc.).              |


## Target Variable
| Column Name             | Type | Description                                                  |
| ----------------------- | ---- | ------------------------------------------------------------ |
| `subscription_canceled` | int  | Indicates if the customer churned (1 = churned, 0 = active). |


## Pricing Sensitivity & Payments
| Column Name         | Type     | Description                                        |
| ------------------- | -------- | -------------------------------------------------- |
| `payment_mode`      | category | Payment method used by the customer.               |
| `monthly_plan_cost` | float    | Monthly subscription cost.                         |
| `total_revenue`     | float    | Total revenue collected from the customer to date. |


## Experience & Satisfaction Indicators
| Column Name              | Type | Description                                              |
| ------------------------ | ---- | -------------------------------------------------------- |
| `customer_rating`        | int  | Customer satisfaction rating (1–5 scale).                |
| `nps_score`              | int  | Net Promoter Score provided by the customer.             |
| `promo_email_clicks`     | int  | Number of promotional emails clicked by the customer.    |
| `support_tickets_last6m` | int  | Number of support tickets raised in the last six months. |

