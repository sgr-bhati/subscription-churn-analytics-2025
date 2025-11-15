import pandas as pd
import numpy as np

n = 200  # tiny sample for Day 1
np.random.seed(42)
df = pd.DataFrame({
    'customer_id': [f'CUST_{i:05d}' for i in range(n)],
    'gender': np.random.choice(['Male','Female'], n),
    'months_subscribed': np.random.randint(0,48,n),
    'subscription_type': np.random.choice(['Monthly','Quarterly','Annual'], n, p=[0.6,0.2,0.2]),
    'streaming_quality': np.random.choice(['Basic','Standard','Premium'], n, p=[0.3,0.5,0.2]),
    'payment_mode': np.random.choice(['UPI','Wallet','Credit Card','Debit Card'], n),
    'monthly_plan_cost': np.round(np.random.uniform(49,499, n),2),
    'total_revenue': lambda x: x['monthly_plan_cost'] * (x['months_subscribed']+1),
    'subscription_canceled': np.random.choice(['Yes','No'], n, p=[0.2,0.8]),
    'app_usage_hours': np.round(np.random.uniform(0.5,6.0,n),2),
    'customer_rating': np.random.randint(1,6,n),
    'promo_email_clicks': np.random.randint(0,12,n),
    'device_type': np.random.choice(['Mobile','Desktop','SmartTV'], n)
})
df['total_revenue'] = df['monthly_plan_cost'] * (df['months_subscribed'] + 1)
df.to_csv('data/raw/sample_customer_data.csv', index=False)
print("sample_customer_data.csv created")
