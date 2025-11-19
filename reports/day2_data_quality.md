# Day 2 – Data Quality Report

### Null Values (after cleaning)
- No missing records remaining  
- `TotalCharges` cleaned using median imputation  

### Data Type Corrections
- `TotalCharges` → float  
- `tenure`, `MonthlyCharges` → float  

### Added Synthetic Features
| Feature | Description |
|----------|--------------|
| app_usage_hours | Avg. daily watch/usage time |
| customer_rating | User satisfaction (1–5) |
| promo_email_clicks | Marketing engagement score |
| device_type | Device category |

### Duplicates Removed
- ✅ Duplicates checked and dropped  

**Next:** Proceed to Day 3 – EDA & Feature Insight Extraction.
