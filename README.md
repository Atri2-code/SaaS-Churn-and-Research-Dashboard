# Real-World Customer Churn & Retention Analytics

## Overview
A Python-based analytics engine built to process real-world business data (IBM Telco Customer Churn Dataset). This project identifies the leading operational indicators of customer churn and generates visual dashboards to guide Customer Operations strategies.

## Business Impact & Insights
By analyzing over 7,000 real customer records, this project uncovers actionable insights for scaling operations:
1. **The Support Deficit:** Customers lacking dedicated Tech Support churn at nearly triple the rate of those with it, highlighting the ROI of a strong Customer Operations team.
2. **The "Month-One" Cliff:** The highest volume of churn occurs in the first 1-3 months of tenure, proving that robust, frictionless onboarding is the most critical phase of the customer lifecycle.

## Technologies Used
* **Python 3**
* **Pandas** (Data cleaning and aggregation)
* **Seaborn & Matplotlib** (Data visualization and dashboarding)

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Fetch the real IBM dataset: `python fetch_real_data.py`
4. Run the analytics engine: `python churn_analysis.py`
5. Review the exported `.png` charts to inform operational strategy.
