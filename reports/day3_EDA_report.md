# EDA Report

Dataset: `../data/processed/cleaned_subscriptions_churn.csv`  
Rows: **7043**, Columns: **19**

## Column summary

| Column | Type | Non-null | Unique | Example values |
|---|---:|---:|---:|---|

| `gender` | object | 7043 | 2 | Female, Male |

| `months_subscribed` | int64 | 7043 | 73 | 1, 34, 2, 45, 8 |

| `streaming_quality` | object | 7043 | 3 | HD, 4K, SD |

| `subscription_type` | object | 7043 | 3 | Month-to-month, One year, Two year |

| `payment_mode` | object | 7043 | 4 | Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic) |

| `monthly_plan_cost` | float64 | 7043 | 1585 | 29.85, 56.95, 53.85, 42.3, 70.7 |

| `total_revenue` | float64 | 7043 | 6531 | 29.85, 1889.5, 108.15, 1840.75, 151.65 |

| `subscription_canceled` | int64 | 7043 | 2 | 0, 1 |

| `app_usage_hours` | float64 | 7043 | 66 | 4.1, 5.1, 2.4, 3.8, 6.3 |

| `last30d_usage_hours` | float64 | 7043 | 5249 | 125.9, 177.9, 88.5, 124.0, 182.8 |

| `customer_rating` | int64 | 7043 | 5 | 3, 4, 5, 1, 2 |

| `promo_email_clicks` | int64 | 7043 | 11 | 3, 2, 4, 5, 6 |

| `device_type` | object | 7043 | 3 | Mobile, Desktop, SmartTV |

| `num_profiles` | int64 | 7043 | 4 | 1, 2, 3, 4 |

| `auto_renew` | int64 | 7043 | 2 | 1, 0 |

| `support_tickets_last6m` | int64 | 7043 | 6 | 0, 1, 2, 3, 4 |

| `nps_score` | int64 | 7043 | 11 | 9, 7, 1, 6, 3 |

| `is_active_last30d` | int64 | 7043 | 1 | 1 |


## Numerical analysis (continuous / numeric columns)

### 1 — Summary statistics

Summary table (count, mean, std, min, 25%, 50%, 75%, max, skewness, kurtosis):


|                     |   count |       mean |        std |   min |      25% |     50% |     75% |      max |   skewness |   kurtosis |
|:--------------------|--------:|-----------:|-----------:|------:|---------:|--------:|--------:|---------:|-----------:|-----------:|
| months_subscribed   |    7043 |   32.3711  |   24.5595  |  0    |   9      |   29    |   55    |   72     |  0.23954   |  -1.38737  |
| monthly_plan_cost   |    7043 |   64.7617  |   30.09    | 18.25 |  35.5    |   70.35 |   89.85 |  118.75  | -0.220524  |  -1.25726  |
| total_revenue       |    7043 | 2281.92    | 2265.27    | 18.8  | 402.225  | 1397.47 | 3786.6  | 8684.8   |  0.963789  |  -0.2264   |
| app_usage_hours     |    7043 |    3.72641 |    1.87074 |  0.5  |   2.1    |    3.7  |    5.3  |    7     |  0.0427845 |  -1.20407  |
| last30d_usage_hours |    7043 |  138.792   |   76.8858  | 13.2  |  75.2607 |  132.3  |  190.7  |  399.286 |  0.500657  |  -0.343555 |
| promo_email_clicks  |    7043 |    3.00057 |    1.75024 |  0    |   2      |    3    |    4    |   10     |  0.558352  |   0.23339  |
| nps_score           |    7043 |    4.53145 |    2.91442 |  0    |   2      |    5    |    7    |   10     |  0.0086289 |  -1.21885  |


### 2 — Histogram + KDE (saved images)

![Histogram KDE months_subscribed](figures/hist_kde_months_subscribed.png)  

![Histogram KDE monthly_plan_cost](figures/hist_kde_monthly_plan_cost.png)  

![Histogram KDE total_revenue](figures/hist_kde_total_revenue.png)  

![Histogram KDE app_usage_hours](figures/hist_kde_app_usage_hours.png)  

![Histogram KDE last30d_usage_hours](figures/hist_kde_last30d_usage_hours.png)  

![Histogram KDE promo_email_clicks](figures/hist_kde_promo_email_clicks.png)  

![Histogram KDE nps_score](figures/hist_kde_nps_score.png)  


### 3 — Box plots (saved images)

![Boxplot months_subscribed](figures/box_months_subscribed.png)  

![Boxplot monthly_plan_cost](figures/box_monthly_plan_cost.png)  

![Boxplot total_revenue](figures/box_total_revenue.png)  

![Boxplot app_usage_hours](figures/box_app_usage_hours.png)  

![Boxplot last30d_usage_hours](figures/box_last30d_usage_hours.png)  

![Boxplot promo_email_clicks](figures/box_promo_email_clicks.png)  

![Boxplot nps_score](figures/box_nps_score.png)  


### 4 — Correlation matrix and heatmap

Pearson correlation matrix:


|                     |   months_subscribed |   monthly_plan_cost |   total_revenue |   app_usage_hours |   last30d_usage_hours |   promo_email_clicks |   nps_score |
|:--------------------|--------------------:|--------------------:|----------------:|------------------:|----------------------:|---------------------:|------------:|
| months_subscribed   |               1     |               0.248 |           0.825 |            -0.007 |                 0.097 |                0.004 |      -0.021 |
| monthly_plan_cost   |               0.248 |               1     |           0.651 |            -0.007 |                 0.218 |                0.009 |      -0.01  |
| total_revenue       |               0.825 |               0.651 |           1     |            -0.012 |                 0.175 |                0.009 |      -0.021 |
| app_usage_hours     |              -0.007 |              -0.007 |          -0.012 |             1     |                 0.902 |                0.019 |       0.002 |
| last30d_usage_hours |               0.097 |               0.218 |           0.175 |             0.902 |                 1     |                0.021 |      -0.007 |
| promo_email_clicks  |               0.004 |               0.009 |           0.009 |             0.019 |                 0.021 |                1     |       0     |
| nps_score           |              -0.021 |              -0.01  |          -0.021 |             0.002 |                -0.007 |                0     |       1     |


![Correlation heatmap](figures/corr_heatmap.png)  


### 5 — Scatter plots (pairwise) — sample pairplot

![Pairplot sample](figures/pairplot.png)  


### 6 — Pair plot
Pairplot (sample used for performance) above.


### 7 — Skewness and 8 — Kurtosis
Skewness and kurtosis were added to the summary table above.


### Outlier detection (per numeric column)

Outlier counts by methods (IQR / Z>3 / outside 1%–99%):


| column              |   n_nonnull |   iqr_outliers |   z_outliers |   pct1_99_outliers |
|:--------------------|------------:|---------------:|-------------:|-------------------:|
| months_subscribed   |        7043 |              0 |            0 |                 11 |
| monthly_plan_cost   |        7043 |              0 |            0 |                136 |
| total_revenue       |        7043 |              0 |            0 |                140 |
| app_usage_hours     |        7043 |              0 |            0 |                 81 |
| last30d_usage_hours |        7043 |             17 |           15 |                141 |
| promo_email_clicks  |        7043 |             90 |           25 |                 25 |
| nps_score           |        7043 |              0 |            0 |                 53 |



## Categorical analysis

### Column: `auto_renew`

Value counts (including NaN):


|   auto_renew |   count |
|-------------:|--------:|
|            1 |    4171 |
|            0 |    2872 |


![Bar auto_renew](figures/bar_auto_renew.png)  

### Column: `customer_rating`

Value counts (including NaN):


|   customer_rating |   count |
|------------------:|--------:|
|                 5 |    1425 |
|                 2 |    1422 |
|                 4 |    1409 |
|                 3 |    1395 |
|                 1 |    1392 |


![Bar customer_rating](figures/bar_customer_rating.png)  

### Column: `device_type`

Value counts (including NaN):


| device_type   |   count |
|:--------------|--------:|
| Mobile        |    4567 |
| Desktop       |    1408 |
| SmartTV       |    1068 |


![Bar device_type](figures/bar_device_type.png)  

### Column: `gender`

Value counts (including NaN):


| gender   |   count |
|:---------|--------:|
| Male     |    3555 |
| Female   |    3488 |


![Bar gender](figures/bar_gender.png)  

### Column: `is_active_last30d`

Value counts (including NaN):


|   is_active_last30d |   count |
|--------------------:|--------:|
|                   1 |    7043 |


![Bar is_active_last30d](figures/bar_is_active_last30d.png)  

### Column: `num_profiles`

Value counts (including NaN):


|   num_profiles |   count |
|---------------:|--------:|
|              1 |    4237 |
|              2 |    1736 |
|              3 |     735 |
|              4 |     335 |


![Bar num_profiles](figures/bar_num_profiles.png)  

### Column: `payment_mode`

Value counts (including NaN):


| payment_mode              |   count |
|:--------------------------|--------:|
| Electronic check          |    2365 |
| Mailed check              |    1612 |
| Bank transfer (automatic) |    1544 |
| Credit card (automatic)   |    1522 |


![Bar payment_mode](figures/bar_payment_mode.png)  

### Column: `streaming_quality`

Value counts (including NaN):


| streaming_quality   |   count |
|:--------------------|--------:|
| 4K                  |    3096 |
| HD                  |    2421 |
| SD                  |    1526 |


![Bar streaming_quality](figures/bar_streaming_quality.png)  

### Column: `subscription_canceled`

Value counts (including NaN):


|   subscription_canceled |   count |
|------------------------:|--------:|
|                       0 |    5174 |
|                       1 |    1869 |


![Bar subscription_canceled](figures/bar_subscription_canceled.png)  

### Column: `subscription_type`

Value counts (including NaN):


| subscription_type   |   count |
|:--------------------|--------:|
| Month-to-month      |    3875 |
| Two year            |    1695 |
| One year            |    1473 |


![Bar subscription_type](figures/bar_subscription_type.png)  

### Column: `support_tickets_last6m`

Value counts (including NaN):


|   support_tickets_last6m |   count |
|-------------------------:|--------:|
|                        0 |    3192 |
|                        1 |    2765 |
|                        2 |     820 |
|                        3 |     217 |
|                        4 |      44 |
|                        5 |       5 |


![Bar support_tickets_last6m](figures/bar_support_tickets_last6m.png)  


### Cross tab & Chi-square tests (categorical vs categorical)

#### Cross-tab: `auto_renew` x `customer_rating`

|   auto_renew |   1 |   2 |   3 |   4 |   5 |
|-------------:|----:|----:|----:|----:|----:|
|            0 | 559 | 559 | 548 | 615 | 591 |
|            1 | 833 | 863 | 847 | 794 | 834 |


- Chi-square test: chi2=7.871, p-value=0.09641, dof=4


#### Cross-tab: `auto_renew` x `device_type`

|   auto_renew |   Desktop |   Mobile |   SmartTV |
|-------------:|----------:|---------:|----------:|
|            0 |       549 |     1893 |       430 |
|            1 |       859 |     2674 |       638 |


- Chi-square test: chi2=2.831, p-value=0.2428, dof=2


#### Cross-tab: `auto_renew` x `gender`

|   auto_renew |   Female |   Male |
|-------------:|---------:|-------:|
|            0 |     1402 |   1470 |
|            1 |     2086 |   2085 |


- Chi-square test: chi2=0.926, p-value=0.336, dof=1


#### Cross-tab: `auto_renew` x `num_profiles`

|   auto_renew |    1 |    2 |   3 |   4 |
|-------------:|-----:|-----:|----:|----:|
|            0 | 1734 |  692 | 321 | 125 |
|            1 | 2503 | 1044 | 414 | 210 |


- Chi-square test: chi2=4.858, p-value=0.1825, dof=3


#### Cross-tab: `auto_renew` x `payment_mode`

|   auto_renew |   Bank transfer (automatic) |   Credit card (automatic) |   Electronic check |   Mailed check |
|-------------:|----------------------------:|--------------------------:|-------------------:|---------------:|
|            0 |                         653 |                       640 |                623 |            956 |
|            1 |                         891 |                       882 |               1742 |            656 |


- Chi-square test: chi2=435.687, p-value=4.115e-94, dof=3


#### Cross-tab: `auto_renew` x `streaming_quality`

|   auto_renew |   4K |   HD |   SD |
|-------------:|-----:|-----:|-----:|
|            0 |  701 | 1091 | 1080 |
|            1 | 2395 | 1330 |  446 |


- Chi-square test: chi2=1008.609, p-value=9.625e-220, dof=2


#### Cross-tab: `auto_renew` x `subscription_canceled`

|   auto_renew |    0 |    1 |
|-------------:|-----:|-----:|
|            0 | 2403 |  469 |
|            1 | 2771 | 1400 |


- Chi-square test: chi2=258.278, p-value=4.073e-58, dof=1


#### Cross-tab: `auto_renew` x `subscription_type`

|   auto_renew |   Month-to-month |   One year |   Two year |
|-------------:|-----------------:|-----------:|-----------:|
|            0 |             1289 |        673 |        910 |
|            1 |             2586 |        800 |        785 |


- Chi-square test: chi2=222.262, p-value=5.451e-49, dof=2


#### Cross-tab: `auto_renew` x `support_tickets_last6m`

|   auto_renew |    0 |    1 |   2 |   3 |   4 |   5 |
|-------------:|-----:|-----:|----:|----:|----:|----:|
|            0 | 1334 | 1093 | 347 |  83 |  14 |   1 |
|            1 | 1858 | 1672 | 473 | 134 |  30 |   4 |


- Chi-square test: chi2=6.878, p-value=0.2298, dof=5


#### Cross-tab: `customer_rating` x `device_type`

|   customer_rating |   Desktop |   Mobile |   SmartTV |
|------------------:|----------:|---------:|----------:|
|                 1 |       317 |      859 |       216 |
|                 2 |       256 |      935 |       231 |
|                 3 |       280 |      918 |       197 |
|                 4 |       274 |      917 |       218 |
|                 5 |       281 |      938 |       206 |


- Chi-square test: chi2=13.947, p-value=0.08315, dof=8


#### Cross-tab: `customer_rating` x `gender`

|   customer_rating |   Female |   Male |
|------------------:|---------:|-------:|
|                 1 |      698 |    694 |
|                 2 |      701 |    721 |
|                 3 |      683 |    712 |
|                 4 |      700 |    709 |
|                 5 |      706 |    719 |


- Chi-square test: chi2=0.434, p-value=0.9796, dof=4


#### Cross-tab: `customer_rating` x `num_profiles`

|   customer_rating |   1 |   2 |   3 |   4 |
|------------------:|----:|----:|----:|----:|
|                 1 | 838 | 340 | 147 |  67 |
|                 2 | 863 | 351 | 148 |  60 |
|                 3 | 822 | 333 | 155 |  85 |
|                 4 | 866 | 339 | 148 |  56 |
|                 5 | 848 | 373 | 137 |  67 |


- Chi-square test: chi2=12.328, p-value=0.4197, dof=12


#### Cross-tab: `customer_rating` x `payment_mode`

|   customer_rating |   Bank transfer (automatic) |   Credit card (automatic) |   Electronic check |   Mailed check |
|------------------:|----------------------------:|--------------------------:|-------------------:|---------------:|
|                 1 |                         315 |                       284 |                475 |            318 |
|                 2 |                         310 |                       328 |                461 |            323 |
|                 3 |                         289 |                       324 |                481 |            301 |
|                 4 |                         298 |                       305 |                473 |            333 |
|                 5 |                         332 |                       281 |                475 |            337 |


- Chi-square test: chi2=12.070, p-value=0.4401, dof=12


#### Cross-tab: `customer_rating` x `streaming_quality`

|   customer_rating |   4K |   HD |   SD |
|------------------:|-----:|-----:|-----:|
|                 1 |  614 |  475 |  303 |
|                 2 |  644 |  485 |  293 |
|                 3 |  605 |  506 |  284 |
|                 4 |  603 |  494 |  312 |
|                 5 |  630 |  461 |  334 |


- Chi-square test: chi2=8.612, p-value=0.3761, dof=8


#### Cross-tab: `customer_rating` x `subscription_canceled`

|   customer_rating |    0 |   1 |
|------------------:|-----:|----:|
|                 1 | 1043 | 349 |
|                 2 | 1016 | 406 |
|                 3 | 1010 | 385 |
|                 4 | 1059 | 350 |
|                 5 | 1046 | 379 |


- Chi-square test: chi2=7.382, p-value=0.117, dof=4


#### Cross-tab: `customer_rating` x `subscription_type`

|   customer_rating |   Month-to-month |   One year |   Two year |
|------------------:|-----------------:|-----------:|-----------:|
|                 1 |              756 |        303 |        333 |
|                 2 |              795 |        289 |        338 |
|                 3 |              786 |        288 |        321 |
|                 4 |              758 |        290 |        361 |
|                 5 |              780 |        303 |        342 |


- Chi-square test: chi2=4.234, p-value=0.8354, dof=8


#### Cross-tab: `customer_rating` x `support_tickets_last6m`

|   customer_rating |   0 |   1 |   2 |   3 |   4 |   5 |
|------------------:|----:|----:|----:|----:|----:|----:|
|                 1 | 640 | 538 | 160 |  41 |  11 |   2 |
|                 2 | 674 | 536 | 160 |  44 |   8 |   0 |
|                 3 | 626 | 560 | 159 |  37 |  12 |   1 |
|                 4 | 620 | 568 | 172 |  43 |   5 |   1 |
|                 5 | 632 | 563 | 169 |  52 |   8 |   1 |


- Chi-square test: chi2=12.958, p-value=0.8792, dof=20


#### Cross-tab: `device_type` x `gender`

| device_type   |   Female |   Male |
|:--------------|---------:|-------:|
| Desktop       |      672 |    736 |
| Mobile        |     2297 |   2270 |
| SmartTV       |      519 |    549 |


- Chi-square test: chi2=3.274, p-value=0.1945, dof=2


#### Cross-tab: `device_type` x `num_profiles`

| device_type   |    1 |    2 |   3 |   4 |
|:--------------|-----:|-----:|----:|----:|
| Desktop       |  838 |  359 | 149 |  62 |
| Mobile        | 2765 | 1118 | 464 | 220 |
| SmartTV       |  634 |  259 | 122 |  53 |


- Chi-square test: chi2=2.713, p-value=0.8439, dof=6


#### Cross-tab: `device_type` x `payment_mode`

| device_type   |   Bank transfer (automatic) |   Credit card (automatic) |   Electronic check |   Mailed check |
|:--------------|----------------------------:|--------------------------:|-------------------:|---------------:|
| Desktop       |                         322 |                       301 |                460 |            325 |
| Mobile        |                        1009 |                       977 |               1525 |           1056 |
| SmartTV       |                         213 |                       244 |                380 |            231 |


- Chi-square test: chi2=5.975, p-value=0.426, dof=6


#### Cross-tab: `device_type` x `streaming_quality`

| device_type   |   4K |   HD |   SD |
|:--------------|-----:|-----:|-----:|
| Desktop       |  626 |  484 |  298 |
| Mobile        | 1995 | 1567 | 1005 |
| SmartTV       |  475 |  370 |  223 |


- Chi-square test: chi2=0.963, p-value=0.9153, dof=4


#### Cross-tab: `device_type` x `subscription_canceled`

| device_type   |    0 |    1 |
|:--------------|-----:|-----:|
| Desktop       | 1016 |  392 |
| Mobile        | 3371 | 1196 |
| SmartTV       |  787 |  281 |


- Chi-square test: chi2=1.542, p-value=0.4627, dof=2


#### Cross-tab: `device_type` x `subscription_type`

| device_type   |   Month-to-month |   One year |   Two year |
|:--------------|-----------------:|-----------:|-----------:|
| Desktop       |              771 |        302 |        335 |
| Mobile        |             2514 |        957 |       1096 |
| SmartTV       |              590 |        214 |        264 |


- Chi-square test: chi2=0.858, p-value=0.9305, dof=4


#### Cross-tab: `device_type` x `support_tickets_last6m`

| device_type   |    0 |    1 |   2 |   3 |   4 |   5 |
|:--------------|-----:|-----:|----:|----:|----:|----:|
| Desktop       |  615 |  548 | 188 |  48 |   7 |   2 |
| Mobile        | 2089 | 1796 | 519 | 132 |  28 |   3 |
| SmartTV       |  488 |  421 | 113 |  37 |   9 |   0 |


- Chi-square test: chi2=10.482, p-value=0.3993, dof=10


#### Cross-tab: `gender` x `num_profiles`

| gender   |    1 |   2 |   3 |   4 |
|:---------|-----:|----:|----:|----:|
| Female   | 2101 | 852 | 360 | 175 |
| Male     | 2136 | 884 | 375 | 160 |


- Chi-square test: chi2=1.219, p-value=0.7483, dof=3


#### Cross-tab: `gender` x `payment_mode`

| gender   |   Bank transfer (automatic) |   Credit card (automatic) |   Electronic check |   Mailed check |
|:---------|----------------------------:|--------------------------:|-------------------:|---------------:|
| Female   |                         788 |                       752 |               1170 |            778 |
| Male     |                         756 |                       770 |               1195 |            834 |


- Chi-square test: chi2=2.449, p-value=0.4846, dof=3


#### Cross-tab: `gender` x `streaming_quality`

| gender   |   4K |   HD |   SD |
|:---------|-----:|-----:|-----:|
| Female   | 1553 | 1188 |  747 |
| Male     | 1543 | 1233 |  779 |


- Chi-square test: chi2=0.902, p-value=0.6368, dof=2


#### Cross-tab: `gender` x `subscription_canceled`

| gender   |    0 |   1 |
|:---------|-----:|----:|
| Female   | 2549 | 939 |
| Male     | 2625 | 930 |


- Chi-square test: chi2=0.484, p-value=0.4866, dof=1


#### Cross-tab: `gender` x `subscription_type`

| gender   |   Month-to-month |   One year |   Two year |
|:---------|-----------------:|-----------:|-----------:|
| Female   |             1925 |        718 |        845 |
| Male     |             1950 |        755 |        850 |


- Chi-square test: chi2=0.468, p-value=0.7913, dof=2


#### Cross-tab: `gender` x `support_tickets_last6m`

| gender   |    0 |    1 |   2 |   3 |   4 |   5 |
|:---------|-----:|-----:|----:|----:|----:|----:|
| Female   | 1611 | 1361 | 398 | 103 |  14 |   1 |
| Male     | 1581 | 1404 | 422 | 114 |  30 |   4 |


- Chi-square test: chi2=9.192, p-value=0.1016, dof=5


#### Cross-tab: `num_profiles` x `payment_mode`

|   num_profiles |   Bank transfer (automatic) |   Credit card (automatic) |   Electronic check |   Mailed check |
|---------------:|----------------------------:|--------------------------:|-------------------:|---------------:|
|              1 |                         926 |                       918 |               1431 |            962 |
|              2 |                         380 |                       362 |                575 |            419 |
|              3 |                         165 |                       163 |                247 |            160 |
|              4 |                          73 |                        79 |                112 |             71 |


- Chi-square test: chi2=3.508, p-value=0.9407, dof=9


#### Cross-tab: `num_profiles` x `streaming_quality`

|   num_profiles |   4K |   HD |   SD |
|---------------:|-----:|-----:|-----:|
|              1 | 1841 | 1481 |  915 |
|              2 |  774 |  573 |  389 |
|              3 |  342 |  249 |  144 |
|              4 |  139 |  118 |   78 |


- Chi-square test: chi2=5.770, p-value=0.4495, dof=6


#### Cross-tab: `num_profiles` x `subscription_canceled`

|   num_profiles |    0 |    1 |
|---------------:|-----:|-----:|
|              1 | 3098 | 1139 |
|              2 | 1286 |  450 |
|              3 |  539 |  196 |
|              4 |  251 |   84 |


- Chi-square test: chi2=0.970, p-value=0.8085, dof=3


#### Cross-tab: `num_profiles` x `subscription_type`

|   num_profiles |   Month-to-month |   One year |   Two year |
|---------------:|-----------------:|-----------:|-----------:|
|              1 |             2339 |        893 |       1005 |
|              2 |              948 |        357 |        431 |
|              3 |              406 |        157 |        172 |
|              4 |              182 |         66 |         87 |


- Chi-square test: chi2=1.844, p-value=0.9335, dof=6


#### Cross-tab: `num_profiles` x `support_tickets_last6m`

|   num_profiles |    0 |    1 |   2 |   3 |   4 |   5 |
|---------------:|-----:|-----:|----:|----:|----:|----:|
|              1 | 1929 | 1652 | 488 | 137 |  29 |   2 |
|              2 |  795 |  680 | 199 |  50 |  10 |   2 |
|              3 |  325 |  285 | 104 |  17 |   3 |   1 |
|              4 |  143 |  148 |  29 |  13 |   2 |   0 |


- Chi-square test: chi2=14.670, p-value=0.4754, dof=15


#### Cross-tab: `payment_mode` x `streaming_quality`

| payment_mode              |   4K |   HD |   SD |
|:--------------------------|-----:|-----:|-----:|
| Bank transfer (automatic) |  646 |  566 |  332 |
| Credit card (automatic)   |  597 |  594 |  331 |
| Electronic check          | 1595 |  648 |  122 |
| Mailed check              |  258 |  613 |  741 |


- Chi-square test: chi2=1381.076, p-value=3.032e-295, dof=6


#### Cross-tab: `payment_mode` x `subscription_canceled`

| payment_mode              |    0 |    1 |
|:--------------------------|-----:|-----:|
| Bank transfer (automatic) | 1286 |  258 |
| Credit card (automatic)   | 1290 |  232 |
| Electronic check          | 1294 | 1071 |
| Mailed check              | 1304 |  308 |


- Chi-square test: chi2=648.142, p-value=3.682e-140, dof=3


#### Cross-tab: `payment_mode` x `subscription_type`

| payment_mode              |   Month-to-month |   One year |   Two year |
|:--------------------------|-----------------:|-----------:|-----------:|
| Bank transfer (automatic) |              589 |        391 |        564 |
| Credit card (automatic)   |              543 |        398 |        581 |
| Electronic check          |             1850 |        347 |        168 |
| Mailed check              |              893 |        337 |        382 |


- Chi-square test: chi2=1001.582, p-value=4.068e-213, dof=6


#### Cross-tab: `payment_mode` x `support_tickets_last6m`

| payment_mode              |    0 |   1 |   2 |   3 |   4 |   5 |
|:--------------------------|-----:|----:|----:|----:|----:|----:|
| Bank transfer (automatic) |  705 | 620 | 170 |  43 |   4 |   2 |
| Credit card (automatic)   |  687 | 627 | 169 |  32 |   6 |   1 |
| Electronic check          | 1075 | 916 | 260 |  92 |  21 |   1 |
| Mailed check              |  725 | 602 | 221 |  50 |  13 |   1 |


- Chi-square test: chi2=30.539, p-value=0.01012, dof=15


#### Cross-tab: `streaming_quality` x `subscription_canceled`

| streaming_quality   |    0 |    1 |
|:--------------------|-----:|-----:|
| 4K                  | 1799 | 1297 |
| HD                  | 1962 |  459 |
| SD                  | 1413 |  113 |


- Chi-square test: chi2=732.310, p-value=9.572e-160, dof=2


#### Cross-tab: `streaming_quality` x `subscription_type`

| streaming_quality   |   Month-to-month |   One year |   Two year |
|:--------------------|-----------------:|-----------:|-----------:|
| 4K                  |             2128 |        539 |        429 |
| HD                  |             1223 |        570 |        628 |
| SD                  |              524 |        364 |        638 |


- Chi-square test: chi2=603.110, p-value=3.29e-129, dof=4


#### Cross-tab: `streaming_quality` x `support_tickets_last6m`

| streaming_quality   |    0 |    1 |   2 |   3 |   4 |   5 |
|:--------------------|-----:|-----:|----:|----:|----:|----:|
| 4K                  | 1386 | 1225 | 355 | 109 |  19 |   2 |
| HD                  | 1105 |  998 | 238 |  66 |  12 |   2 |
| SD                  |  701 |  542 | 227 |  42 |  13 |   1 |


- Chi-square test: chi2=34.344, p-value=0.0001615, dof=10


#### Cross-tab: `subscription_canceled` x `subscription_type`

|   subscription_canceled |   Month-to-month |   One year |   Two year |
|------------------------:|-----------------:|-----------:|-----------:|
|                       0 |             2220 |       1307 |       1647 |
|                       1 |             1655 |        166 |         48 |


- Chi-square test: chi2=1184.597, p-value=5.863e-258, dof=2


#### Cross-tab: `subscription_canceled` x `support_tickets_last6m`

|   subscription_canceled |    0 |    1 |   2 |   3 |   4 |   5 |
|------------------------:|-----:|-----:|----:|----:|----:|----:|
|                       0 | 2359 | 2054 | 584 | 144 |  29 |   4 |
|                       1 |  833 |  711 | 236 |  73 |  15 |   1 |


- Chi-square test: chi2=10.409, p-value=0.06444, dof=5


#### Cross-tab: `subscription_type` x `support_tickets_last6m`

| subscription_type   |    0 |    1 |   2 |   3 |   4 |   5 |
|:--------------------|-----:|-----:|----:|----:|----:|----:|
| Month-to-month      | 1736 | 1455 | 507 | 143 |  32 |   2 |
| One year            |  679 |  595 | 152 |  39 |   7 |   1 |
| Two year            |  777 |  715 | 161 |  35 |   5 |   2 |


- Chi-square test: chi2=41.380, p-value=9.664e-06, dof=10


### Stacked bar charts (sample)

![Stacked auto_renew_by_customer_rating](figures/stacked_auto_renew_by_customer_rating.png)  

![Stacked customer_rating_by_device_type](figures/stacked_customer_rating_by_device_type.png)  

![Stacked device_type_by_gender](figures/stacked_device_type_by_gender.png)  

![Stacked gender_by_is_active_last30d](figures/stacked_gender_by_is_active_last30d.png)  

![Stacked is_active_last30d_by_num_profiles](figures/stacked_is_active_last30d_by_num_profiles.png)  

![Stacked num_profiles_by_payment_mode](figures/stacked_num_profiles_by_payment_mode.png)  

![Stacked payment_mode_by_streaming_quality](figures/stacked_payment_mode_by_streaming_quality.png)  

![Stacked streaming_quality_by_subscription_canceled](figures/stacked_streaming_quality_by_subscription_canceled.png)  

![Stacked subscription_canceled_by_subscription_type](figures/stacked_subscription_canceled_by_subscription_type.png)  

![Stacked subscription_type_by_support_tickets_last6m](figures/stacked_subscription_type_by_support_tickets_last6m.png)  


## Bivariate analysis


### 15 — Box plots (numeric grouped by categorical)

![Box months_subscribed_by_auto_renew](figures/box_months_subscribed_by_auto_renew.png)  

![Box monthly_plan_cost_by_auto_renew](figures/box_monthly_plan_cost_by_auto_renew.png)  

![Box total_revenue_by_auto_renew](figures/box_total_revenue_by_auto_renew.png)  

![Box app_usage_hours_by_auto_renew](figures/box_app_usage_hours_by_auto_renew.png)  

![Box last30d_usage_hours_by_auto_renew](figures/box_last30d_usage_hours_by_auto_renew.png)  

![Box promo_email_clicks_by_auto_renew](figures/box_promo_email_clicks_by_auto_renew.png)  

![Box nps_score_by_auto_renew](figures/box_nps_score_by_auto_renew.png)  

![Box months_subscribed_by_customer_rating](figures/box_months_subscribed_by_customer_rating.png)  

![Box monthly_plan_cost_by_customer_rating](figures/box_monthly_plan_cost_by_customer_rating.png)  

![Box total_revenue_by_customer_rating](figures/box_total_revenue_by_customer_rating.png)  

![Box app_usage_hours_by_customer_rating](figures/box_app_usage_hours_by_customer_rating.png)  

![Box last30d_usage_hours_by_customer_rating](figures/box_last30d_usage_hours_by_customer_rating.png)  

![Box promo_email_clicks_by_customer_rating](figures/box_promo_email_clicks_by_customer_rating.png)  

![Box nps_score_by_customer_rating](figures/box_nps_score_by_customer_rating.png)  

![Box months_subscribed_by_device_type](figures/box_months_subscribed_by_device_type.png)  

![Box monthly_plan_cost_by_device_type](figures/box_monthly_plan_cost_by_device_type.png)  

![Box total_revenue_by_device_type](figures/box_total_revenue_by_device_type.png)  

![Box app_usage_hours_by_device_type](figures/box_app_usage_hours_by_device_type.png)  

![Box last30d_usage_hours_by_device_type](figures/box_last30d_usage_hours_by_device_type.png)  

![Box promo_email_clicks_by_device_type](figures/box_promo_email_clicks_by_device_type.png)  

![Box nps_score_by_device_type](figures/box_nps_score_by_device_type.png)  

![Box months_subscribed_by_gender](figures/box_months_subscribed_by_gender.png)  

![Box monthly_plan_cost_by_gender](figures/box_monthly_plan_cost_by_gender.png)  

![Box total_revenue_by_gender](figures/box_total_revenue_by_gender.png)  

![Box app_usage_hours_by_gender](figures/box_app_usage_hours_by_gender.png)  

![Box last30d_usage_hours_by_gender](figures/box_last30d_usage_hours_by_gender.png)  

![Box promo_email_clicks_by_gender](figures/box_promo_email_clicks_by_gender.png)  

![Box nps_score_by_gender](figures/box_nps_score_by_gender.png)  

![Box months_subscribed_by_is_active_last30d](figures/box_months_subscribed_by_is_active_last30d.png)  

![Box monthly_plan_cost_by_is_active_last30d](figures/box_monthly_plan_cost_by_is_active_last30d.png)  

![Box total_revenue_by_is_active_last30d](figures/box_total_revenue_by_is_active_last30d.png)  

![Box app_usage_hours_by_is_active_last30d](figures/box_app_usage_hours_by_is_active_last30d.png)  

![Box last30d_usage_hours_by_is_active_last30d](figures/box_last30d_usage_hours_by_is_active_last30d.png)  

![Box promo_email_clicks_by_is_active_last30d](figures/box_promo_email_clicks_by_is_active_last30d.png)  

![Box nps_score_by_is_active_last30d](figures/box_nps_score_by_is_active_last30d.png)  

![Box months_subscribed_by_num_profiles](figures/box_months_subscribed_by_num_profiles.png)  

![Box monthly_plan_cost_by_num_profiles](figures/box_monthly_plan_cost_by_num_profiles.png)  

![Box total_revenue_by_num_profiles](figures/box_total_revenue_by_num_profiles.png)  

![Box app_usage_hours_by_num_profiles](figures/box_app_usage_hours_by_num_profiles.png)  

![Box last30d_usage_hours_by_num_profiles](figures/box_last30d_usage_hours_by_num_profiles.png)  

![Box promo_email_clicks_by_num_profiles](figures/box_promo_email_clicks_by_num_profiles.png)  

![Box nps_score_by_num_profiles](figures/box_nps_score_by_num_profiles.png)  

![Box months_subscribed_by_payment_mode](figures/box_months_subscribed_by_payment_mode.png)  

![Box monthly_plan_cost_by_payment_mode](figures/box_monthly_plan_cost_by_payment_mode.png)  

![Box total_revenue_by_payment_mode](figures/box_total_revenue_by_payment_mode.png)  

![Box app_usage_hours_by_payment_mode](figures/box_app_usage_hours_by_payment_mode.png)  

![Box last30d_usage_hours_by_payment_mode](figures/box_last30d_usage_hours_by_payment_mode.png)  

![Box promo_email_clicks_by_payment_mode](figures/box_promo_email_clicks_by_payment_mode.png)  

![Box nps_score_by_payment_mode](figures/box_nps_score_by_payment_mode.png)  

![Box months_subscribed_by_streaming_quality](figures/box_months_subscribed_by_streaming_quality.png)  

![Box monthly_plan_cost_by_streaming_quality](figures/box_monthly_plan_cost_by_streaming_quality.png)  

![Box total_revenue_by_streaming_quality](figures/box_total_revenue_by_streaming_quality.png)  

![Box app_usage_hours_by_streaming_quality](figures/box_app_usage_hours_by_streaming_quality.png)  

![Box last30d_usage_hours_by_streaming_quality](figures/box_last30d_usage_hours_by_streaming_quality.png)  

![Box promo_email_clicks_by_streaming_quality](figures/box_promo_email_clicks_by_streaming_quality.png)  

![Box nps_score_by_streaming_quality](figures/box_nps_score_by_streaming_quality.png)  

![Box months_subscribed_by_subscription_canceled](figures/box_months_subscribed_by_subscription_canceled.png)  

![Box monthly_plan_cost_by_subscription_canceled](figures/box_monthly_plan_cost_by_subscription_canceled.png)  

![Box total_revenue_by_subscription_canceled](figures/box_total_revenue_by_subscription_canceled.png)  

![Box app_usage_hours_by_subscription_canceled](figures/box_app_usage_hours_by_subscription_canceled.png)  

![Box last30d_usage_hours_by_subscription_canceled](figures/box_last30d_usage_hours_by_subscription_canceled.png)  

![Box promo_email_clicks_by_subscription_canceled](figures/box_promo_email_clicks_by_subscription_canceled.png)  

![Box nps_score_by_subscription_canceled](figures/box_nps_score_by_subscription_canceled.png)  

![Box months_subscribed_by_subscription_type](figures/box_months_subscribed_by_subscription_type.png)  

![Box monthly_plan_cost_by_subscription_type](figures/box_monthly_plan_cost_by_subscription_type.png)  

![Box total_revenue_by_subscription_type](figures/box_total_revenue_by_subscription_type.png)  

![Box app_usage_hours_by_subscription_type](figures/box_app_usage_hours_by_subscription_type.png)  

![Box last30d_usage_hours_by_subscription_type](figures/box_last30d_usage_hours_by_subscription_type.png)  

![Box promo_email_clicks_by_subscription_type](figures/box_promo_email_clicks_by_subscription_type.png)  

![Box nps_score_by_subscription_type](figures/box_nps_score_by_subscription_type.png)  

![Box months_subscribed_by_support_tickets_last6m](figures/box_months_subscribed_by_support_tickets_last6m.png)  

![Box monthly_plan_cost_by_support_tickets_last6m](figures/box_monthly_plan_cost_by_support_tickets_last6m.png)  

![Box total_revenue_by_support_tickets_last6m](figures/box_total_revenue_by_support_tickets_last6m.png)  

![Box app_usage_hours_by_support_tickets_last6m](figures/box_app_usage_hours_by_support_tickets_last6m.png)  

![Box last30d_usage_hours_by_support_tickets_last6m](figures/box_last30d_usage_hours_by_support_tickets_last6m.png)  

![Box promo_email_clicks_by_support_tickets_last6m](figures/box_promo_email_clicks_by_support_tickets_last6m.png)  

![Box nps_score_by_support_tickets_last6m](figures/box_nps_score_by_support_tickets_last6m.png)  


### 16 — Violin charts (numeric grouped by categorical)

![Violin months_subscribed_by_auto_renew](figures/violin_months_subscribed_by_auto_renew.png)  

![Violin monthly_plan_cost_by_auto_renew](figures/violin_monthly_plan_cost_by_auto_renew.png)  

![Violin total_revenue_by_auto_renew](figures/violin_total_revenue_by_auto_renew.png)  

![Violin app_usage_hours_by_auto_renew](figures/violin_app_usage_hours_by_auto_renew.png)  

![Violin last30d_usage_hours_by_auto_renew](figures/violin_last30d_usage_hours_by_auto_renew.png)  

![Violin promo_email_clicks_by_auto_renew](figures/violin_promo_email_clicks_by_auto_renew.png)  

![Violin nps_score_by_auto_renew](figures/violin_nps_score_by_auto_renew.png)  

![Violin months_subscribed_by_customer_rating](figures/violin_months_subscribed_by_customer_rating.png)  

![Violin monthly_plan_cost_by_customer_rating](figures/violin_monthly_plan_cost_by_customer_rating.png)  

![Violin total_revenue_by_customer_rating](figures/violin_total_revenue_by_customer_rating.png)  

![Violin app_usage_hours_by_customer_rating](figures/violin_app_usage_hours_by_customer_rating.png)  

![Violin last30d_usage_hours_by_customer_rating](figures/violin_last30d_usage_hours_by_customer_rating.png)  

![Violin promo_email_clicks_by_customer_rating](figures/violin_promo_email_clicks_by_customer_rating.png)  

![Violin nps_score_by_customer_rating](figures/violin_nps_score_by_customer_rating.png)  

![Violin months_subscribed_by_device_type](figures/violin_months_subscribed_by_device_type.png)  

![Violin monthly_plan_cost_by_device_type](figures/violin_monthly_plan_cost_by_device_type.png)  

![Violin total_revenue_by_device_type](figures/violin_total_revenue_by_device_type.png)  

![Violin app_usage_hours_by_device_type](figures/violin_app_usage_hours_by_device_type.png)  

![Violin last30d_usage_hours_by_device_type](figures/violin_last30d_usage_hours_by_device_type.png)  

![Violin promo_email_clicks_by_device_type](figures/violin_promo_email_clicks_by_device_type.png)  

![Violin nps_score_by_device_type](figures/violin_nps_score_by_device_type.png)  

![Violin months_subscribed_by_gender](figures/violin_months_subscribed_by_gender.png)  

![Violin monthly_plan_cost_by_gender](figures/violin_monthly_plan_cost_by_gender.png)  

![Violin total_revenue_by_gender](figures/violin_total_revenue_by_gender.png)  

![Violin app_usage_hours_by_gender](figures/violin_app_usage_hours_by_gender.png)  

![Violin last30d_usage_hours_by_gender](figures/violin_last30d_usage_hours_by_gender.png)  

![Violin promo_email_clicks_by_gender](figures/violin_promo_email_clicks_by_gender.png)  

![Violin nps_score_by_gender](figures/violin_nps_score_by_gender.png)  

![Violin months_subscribed_by_is_active_last30d](figures/violin_months_subscribed_by_is_active_last30d.png)  

![Violin monthly_plan_cost_by_is_active_last30d](figures/violin_monthly_plan_cost_by_is_active_last30d.png)  

![Violin total_revenue_by_is_active_last30d](figures/violin_total_revenue_by_is_active_last30d.png)  

![Violin app_usage_hours_by_is_active_last30d](figures/violin_app_usage_hours_by_is_active_last30d.png)  

![Violin last30d_usage_hours_by_is_active_last30d](figures/violin_last30d_usage_hours_by_is_active_last30d.png)  

![Violin promo_email_clicks_by_is_active_last30d](figures/violin_promo_email_clicks_by_is_active_last30d.png)  

![Violin nps_score_by_is_active_last30d](figures/violin_nps_score_by_is_active_last30d.png)  

![Violin months_subscribed_by_num_profiles](figures/violin_months_subscribed_by_num_profiles.png)  

![Violin monthly_plan_cost_by_num_profiles](figures/violin_monthly_plan_cost_by_num_profiles.png)  

![Violin total_revenue_by_num_profiles](figures/violin_total_revenue_by_num_profiles.png)  

![Violin app_usage_hours_by_num_profiles](figures/violin_app_usage_hours_by_num_profiles.png)  

![Violin last30d_usage_hours_by_num_profiles](figures/violin_last30d_usage_hours_by_num_profiles.png)  

![Violin promo_email_clicks_by_num_profiles](figures/violin_promo_email_clicks_by_num_profiles.png)  

![Violin nps_score_by_num_profiles](figures/violin_nps_score_by_num_profiles.png)  

![Violin months_subscribed_by_payment_mode](figures/violin_months_subscribed_by_payment_mode.png)  

![Violin monthly_plan_cost_by_payment_mode](figures/violin_monthly_plan_cost_by_payment_mode.png)  

![Violin total_revenue_by_payment_mode](figures/violin_total_revenue_by_payment_mode.png)  

![Violin app_usage_hours_by_payment_mode](figures/violin_app_usage_hours_by_payment_mode.png)  

![Violin last30d_usage_hours_by_payment_mode](figures/violin_last30d_usage_hours_by_payment_mode.png)  

![Violin promo_email_clicks_by_payment_mode](figures/violin_promo_email_clicks_by_payment_mode.png)  

![Violin nps_score_by_payment_mode](figures/violin_nps_score_by_payment_mode.png)  

![Violin months_subscribed_by_streaming_quality](figures/violin_months_subscribed_by_streaming_quality.png)  

![Violin monthly_plan_cost_by_streaming_quality](figures/violin_monthly_plan_cost_by_streaming_quality.png)  

![Violin total_revenue_by_streaming_quality](figures/violin_total_revenue_by_streaming_quality.png)  

![Violin app_usage_hours_by_streaming_quality](figures/violin_app_usage_hours_by_streaming_quality.png)  

![Violin last30d_usage_hours_by_streaming_quality](figures/violin_last30d_usage_hours_by_streaming_quality.png)  

![Violin promo_email_clicks_by_streaming_quality](figures/violin_promo_email_clicks_by_streaming_quality.png)  

![Violin nps_score_by_streaming_quality](figures/violin_nps_score_by_streaming_quality.png)  

![Violin months_subscribed_by_subscription_canceled](figures/violin_months_subscribed_by_subscription_canceled.png)  

![Violin monthly_plan_cost_by_subscription_canceled](figures/violin_monthly_plan_cost_by_subscription_canceled.png)  

![Violin total_revenue_by_subscription_canceled](figures/violin_total_revenue_by_subscription_canceled.png)  

![Violin app_usage_hours_by_subscription_canceled](figures/violin_app_usage_hours_by_subscription_canceled.png)  

![Violin last30d_usage_hours_by_subscription_canceled](figures/violin_last30d_usage_hours_by_subscription_canceled.png)  

![Violin promo_email_clicks_by_subscription_canceled](figures/violin_promo_email_clicks_by_subscription_canceled.png)  

![Violin nps_score_by_subscription_canceled](figures/violin_nps_score_by_subscription_canceled.png)  

![Violin months_subscribed_by_subscription_type](figures/violin_months_subscribed_by_subscription_type.png)  

![Violin monthly_plan_cost_by_subscription_type](figures/violin_monthly_plan_cost_by_subscription_type.png)  

![Violin total_revenue_by_subscription_type](figures/violin_total_revenue_by_subscription_type.png)  

![Violin app_usage_hours_by_subscription_type](figures/violin_app_usage_hours_by_subscription_type.png)  

![Violin last30d_usage_hours_by_subscription_type](figures/violin_last30d_usage_hours_by_subscription_type.png)  

![Violin promo_email_clicks_by_subscription_type](figures/violin_promo_email_clicks_by_subscription_type.png)  

![Violin nps_score_by_subscription_type](figures/violin_nps_score_by_subscription_type.png)  

![Violin months_subscribed_by_support_tickets_last6m](figures/violin_months_subscribed_by_support_tickets_last6m.png)  

![Violin monthly_plan_cost_by_support_tickets_last6m](figures/violin_monthly_plan_cost_by_support_tickets_last6m.png)  

![Violin total_revenue_by_support_tickets_last6m](figures/violin_total_revenue_by_support_tickets_last6m.png)  

![Violin app_usage_hours_by_support_tickets_last6m](figures/violin_app_usage_hours_by_support_tickets_last6m.png)  

![Violin last30d_usage_hours_by_support_tickets_last6m](figures/violin_last30d_usage_hours_by_support_tickets_last6m.png)  

![Violin promo_email_clicks_by_support_tickets_last6m](figures/violin_promo_email_clicks_by_support_tickets_last6m.png)  

![Violin nps_score_by_support_tickets_last6m](figures/violin_nps_score_by_support_tickets_last6m.png)  


### 17 — T-tests (numeric by binary categorical) and 18 — ANOVA (numeric by multi-level categorical)

#### months_subscribed by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=0.516, p=0.606


#### monthly_plan_cost by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=31.036, p=9.303e-196


#### total_revenue by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=13.823, p=7.077e-43


#### app_usage_hours by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=-0.653, p=0.5136


#### last30d_usage_hours by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=6.126, p=9.546e-10


#### promo_email_clicks by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=-0.144, p=0.8859


#### nps_score by auto_renew

- Levels: ['1', '0']  

- Two-sample t-test (Welch): t=-0.631, p=0.528


#### months_subscribed by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=1.371, p=0.2414


#### monthly_plan_cost by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=0.756, p=0.5541


#### total_revenue by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=0.815, p=0.5155


#### app_usage_hours by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=1.144, p=0.3338


#### last30d_usage_hours by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=0.751, p=0.557


#### promo_email_clicks by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=0.646, p=0.6295


#### nps_score by customer_rating

- Levels: ['3', '4', '5', '1', '2']  

- One-way ANOVA: F=1.509, p=0.1966


#### months_subscribed by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.000, p=0.9996


#### monthly_plan_cost by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.830, p=0.436


#### total_revenue by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.338, p=0.7131


#### app_usage_hours by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.653, p=0.5203


#### last30d_usage_hours by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.725, p=0.4842


#### promo_email_clicks by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=0.768, p=0.4639


#### nps_score by device_type

- Levels: ['Mobile', 'Desktop', 'SmartTV']  

- One-way ANOVA: F=2.717, p=0.06611


#### months_subscribed by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=-0.429, p=0.6683


#### monthly_plan_cost by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=1.223, p=0.2215


#### total_revenue by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=0.000, p=0.9999


#### app_usage_hours by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=-0.091, p=0.9278


#### last30d_usage_hours by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=0.250, p=0.8028


#### promo_email_clicks by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=0.858, p=0.3909


#### nps_score by gender

- Levels: ['Female', 'Male']  

- Two-sample t-test (Welch): t=0.428, p=0.6689


#### months_subscribed by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.223, p=0.8804


#### monthly_plan_cost by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=1.634, p=0.1791


#### total_revenue by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.503, p=0.6805


#### app_usage_hours by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.853, p=0.4649


#### last30d_usage_hours by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.272, p=0.8457


#### promo_email_clicks by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.953, p=0.414


#### nps_score by num_profiles

- Levels: ['1', '2', '3', '4']  

- One-way ANOVA: F=0.106, p=0.9564


#### months_subscribed by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=446.467, p=1.504e-265


#### monthly_plan_cost by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=450.319, p=1.18e-267


#### total_revenue by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=327.882, p=2.749e-199


#### app_usage_hours by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=0.535, p=0.6584


#### last30d_usage_hours by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=23.464, p=4.169e-15


#### promo_email_clicks by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=0.281, p=0.8389


#### nps_score by payment_mode

- Levels: ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']  

- One-way ANOVA: F=0.563, p=0.6393


#### months_subscribed by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=5.390, p=0.004582


#### monthly_plan_cost by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=16111.646, p=0


#### total_revenue by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=798.113, p=3.937e-313


#### app_usage_hours by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=1.348, p=0.2599


#### last30d_usage_hours by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=87.637, p=2.546e-38


#### promo_email_clicks by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=0.089, p=0.9145


#### nps_score by streaming_quality

- Levels: ['HD', '4K', 'SD']  

- One-way ANOVA: F=0.195, p=0.8225


#### months_subscribed by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=34.824, p=1.195e-232


#### monthly_plan_cost by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=-18.408, p=8.592e-73


#### total_revenue by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=18.768, p=2.059e-75


#### app_usage_hours by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=-0.765, p=0.4442


#### last30d_usage_hours by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=-2.239, p=0.02525


#### promo_email_clicks by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=0.754, p=0.451


#### nps_score by subscription_canceled

- Levels: ['0', '1']  

- Two-sample t-test (Welch): t=-0.845, p=0.398


#### months_subscribed by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=2960.015, p=0


#### monthly_plan_cost by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=20.828, p=9.575e-10


#### total_revenue by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=928.428, p=0


#### app_usage_hours by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=0.033, p=0.9676


#### last30d_usage_hours by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=8.394, p=0.0002285


#### promo_email_clicks by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=0.278, p=0.7571


#### nps_score by subscription_type

- Levels: ['Month-to-month', 'One year', 'Two year']  

- One-way ANOVA: F=1.423, p=0.2409


#### months_subscribed by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=11.667, p=2.987e-11


#### monthly_plan_cost by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=6.797, p=2.484e-06


#### total_revenue by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=14.160, p=8.224e-14


#### app_usage_hours by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=0.115, p=0.9892


#### last30d_usage_hours by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=0.168, p=0.9745


#### promo_email_clicks by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=0.919, p=0.4673


#### nps_score by support_tickets_last6m

- Levels: ['0', '1', '2', '3', '4', '5']  

- One-way ANOVA: F=1.448, p=0.2036



### Numeric–Numeric associations (Pearson & Spearman)

Pearson correlations:


|                     |   months_subscribed |   monthly_plan_cost |   total_revenue |   app_usage_hours |   last30d_usage_hours |   promo_email_clicks |   nps_score |
|:--------------------|--------------------:|--------------------:|----------------:|------------------:|----------------------:|---------------------:|------------:|
| months_subscribed   |               1     |               0.248 |           0.825 |            -0.007 |                 0.097 |                0.004 |      -0.021 |
| monthly_plan_cost   |               0.248 |               1     |           0.651 |            -0.007 |                 0.218 |                0.009 |      -0.01  |
| total_revenue       |               0.825 |               0.651 |           1     |            -0.012 |                 0.175 |                0.009 |      -0.021 |
| app_usage_hours     |              -0.007 |              -0.007 |          -0.012 |             1     |                 0.902 |                0.019 |       0.002 |
| last30d_usage_hours |               0.097 |               0.218 |           0.175 |             0.902 |                 1     |                0.021 |      -0.007 |
| promo_email_clicks  |               0.004 |               0.009 |           0.009 |             0.019 |                 0.021 |                1     |       0     |
| nps_score           |              -0.021 |              -0.01  |          -0.021 |             0.002 |                -0.007 |                0     |       1     |


Spearman correlations:


|                     |   months_subscribed |   monthly_plan_cost |   total_revenue |   app_usage_hours |   last30d_usage_hours |   promo_email_clicks |   nps_score |
|:--------------------|--------------------:|--------------------:|----------------:|------------------:|----------------------:|---------------------:|------------:|
| months_subscribed   |               1     |               0.276 |           0.887 |            -0.009 |                 0.083 |                0.009 |      -0.021 |
| monthly_plan_cost   |               0.276 |               1     |           0.637 |            -0.011 |                 0.189 |                0.014 |      -0.011 |
| total_revenue       |               0.887 |               0.637 |           1     |            -0.013 |                 0.143 |                0.017 |      -0.022 |
| app_usage_hours     |              -0.009 |              -0.011 |          -0.013 |             1     |                 0.931 |                0.022 |       0.002 |
| last30d_usage_hours |               0.083 |               0.189 |           0.143 |             0.931 |                 1     |                0.024 |      -0.001 |
| promo_email_clicks  |               0.009 |               0.014 |           0.017 |             0.022 |                 0.024 |                1     |       0     |
| nps_score           |              -0.021 |              -0.011 |          -0.022 |             0.002 |                -0.001 |                0     |       1     |

