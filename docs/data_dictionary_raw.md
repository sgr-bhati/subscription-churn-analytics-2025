# Data Dictionary — Original Telco Customer Churn Dataset

This document describes the raw dataset before modernization.

## Customer Demographics
| Column Name     | Type     | Description |
|-----------------|----------|-------------|
| customerID      | string   | Unique customer identifier. |
| gender          | category | Gender of the customer (Male/Female). |
| SeniorCitizen   | int      | Indicates if age ≥ 65 (1 = Yes, 0 = No). |
| Partner         | category | Whether the customer has a spouse (Yes/No). |
| Dependents      | category | Whether the customer has dependents (Yes/No). |

## Customer Tenure
| Column Name | Type | Description |
|-------------|------|-------------|
| tenure      | int  | Number of months the customer has stayed with the company. |

## Services Subscribed
| Column Name         | Type     | Description |
|---------------------|----------|-------------|
| PhoneService        | category | Phone line service (Yes/No). |
| MultipleLines       | category | Multiple phone lines (Yes/No/No phone service). |
| InternetService     | category | Internet type (DSL/Fiber optic/None). |
| OnlineSecurity      | category | Online security add-on (Yes/No/No internet). |
| OnlineBackup        | category | Online backup add-on (Yes/No/No internet). |
| DeviceProtection    | category | Device protection add-on (Yes/No/No internet). |
| TechSupport         | category | Tech support add-on (Yes/No/No internet). |
| StreamingTV         | category | Streaming TV usage (Yes/No/No internet). |
| StreamingMovies     | category | Streaming movie usage (Yes/No/No internet). |

## Account Information
| Column Name       | Type     | Description |
|-------------------|----------|-------------|
| Contract          | category | Contract type: Month-to-month, One year, Two year. |
| PaperlessBilling  | category | Whether billing is paperless (Yes/No). |
| PaymentMethod     | category | Payment method used. |
| MonthlyCharges    | float    | Monthly bill amount. |
| TotalCharges      | float    | Total amount charged to date. |

## Target Variable
| Column Name | Type     | Description |
|-------------|----------|-------------|
| Churn       | category | Whether customer churned (Yes/No). |

