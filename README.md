# 📊 IBM Telco Customer Churn Analysis Dashboard
### Power BI · SQL · Python · DAX · Business Intelligence

---

> **Analyzing 7,043 telecom customers to identify churn drivers, quantify revenue at risk, and recommend a retention strategy through Power BI, SQL, and Python.**

---

## 🎯 Project Overview

This project analyzes the [IBM Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) — a real-world dataset of 7,043 telecom customers including their contract type, services, billing details, and churn status.

The goal was to build a complete churn analytics solution that answers real business questions:

- Which customer segments churn the most, and why?
- How much monthly revenue is at risk from churn?
- Which contract types, internet services, and payment methods correlate with churn?
- What retention strategy could recover lost revenue?

---

## 🚀 Why This Project Matters

This project demonstrates my ability to:

* Clean and prepare a real-world dataset with missing and inconsistent values
* Write SQL queries for segment-level churn analysis
* Use Python (pandas, matplotlib) for exploratory data analysis and visualization
* Build a 3-page interactive Power BI dashboard with DAX measures
* Translate churn patterns into a quantified, actionable retention strategy

This project covers the complete analytics workflow — from data cleaning to dashboard development to business recommendation.

## 📌 Executive Summary

Using 7,043 telecom customer records, this analysis identified a 26.54% overall churn rate, representing $139,130.85 in monthly revenue at risk.

The dashboard found that month-to-month contracts account for 88.5% of all churn, fiber optic customers churn at a significantly higher rate than DSL customers, and new customers (0-12 months tenure) are the highest-risk segment. Electronic check was the payment method most associated with churn.

These findings support a targeted retention strategy: converting high-risk month-to-month customers to annual contracts could recover an estimated $13,913 per month based on a 10% retention campaign recovery rate.

## 📊 Project Highlights

- 👥 7,043 Customers Analyzed
- 📉 26.54% Overall Churn Rate
- 💰 $139.13K Monthly Revenue At Risk
- 📈 3-Page Interactive Power BI Dashboard
- 🛠 12 SQL Queries (CTE, Subquery, Window Function)
- 🐍 Python EDA with pandas and matplotlib

## 📈 Dashboard Screenshots

![Executive Overview](Dashboard_Page1_Executive_Overview.png)
![Customer Behavior](Dashboard_Page2_Customer_Behavior.png)
![Retention Strategy](Dashboard_Page3_Retention_Strategy.png)

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Power BI Desktop** | Dashboard design, visualization, interactivity |
| **DAX** | KPI measures, churn rate calculations, conditional formatting |
| **SQL (MySQL)** | Data aggregation, segment analysis, churn rate calculations |
| **Python (pandas, matplotlib)** | Data cleaning, exploratory data analysis, charting |

---

## 📁 Project Structure

```
ibm-telco-churn-analysis/
│
├── Customer_Churn_Analytics.pbix          ← Power BI dashboard file
├── IBM_Telco_Churn_Analysis.sql           ← 12 SQL queries
├── IBM_Telco_Churn_Analysis.py            ← Python EDA script
├── WA_Fn-UseC_-Telco-Customer-Churn.csv   ← Raw dataset
├── Dashboard_Page1_Executive_Overview.png
├── Dashboard_Page2_Customer_Behavior.png
├── Dashboard_Page3_Retention_Strategy.png
└── README.md
```

---

## 📊 Dashboard Features

The dashboard is a 3-page interactive report with KPI cards, charts, tables, and slicers across all pages.

| Page | Visual | What it shows |
|------|--------|---------------|
| Executive Overview | KPI Cards | Total Customers, Churn Customers, Churn Rate %, Revenue At Risk, Avg Monthly Charges |
| Executive Overview | Bar Chart | Churn Count by Contract Type |
| Executive Overview | Bar Chart | Churn Distribution by Internet Service |
| Executive Overview | Bar Chart | Revenue At Risk by Contract Type |
| Executive Overview | Bar Chart | Churn Distribution by Monthly Charge Band |
| Customer Behavior | Bar Chart | Customer Churn by Tenure Group |
| Customer Behavior | Bar Chart | Churn by Gender |
| Customer Behavior | Matrix Table | Contract vs Internet Service |
| Customer Behavior | Bar Chart | Churn by Payment Method |
| Customer Behavior | Donut Chart | Churn by Senior Citizen |
| Retention Strategy | Table | High Risk Customer Segments |
| Retention Strategy | Bar Chart | Monthly Revenue Lost to Churn by Contract |
| Retention Strategy | Card | Revenue Recoverable (10%) |
| Retention Strategy | Text Panel | Key Insights |

**Interactive filters:** Contract slicer · InternetService slicer · Gender slicer — all visuals update together.

---

## 📐 DAX Measures

```dax
Total Customers =
DISTINCTCOUNT(telco_churn[customerID])

Churn Customers =
CALCULATE(
    DISTINCTCOUNT(telco_churn[customerID]),
    telco_churn[Churn] = "Yes"
)

Churn Rate % =
DIVIDE([Churn Customers], [Total Customers], 0)

Revenue At Risk =
CALCULATE(
    SUM(telco_churn[MonthlyCharges]),
    telco_churn[Churn] = "Yes"
)

Avg Monthly Charges =
AVERAGE(telco_churn[MonthlyCharges])

Revenue Recoverable (10%) =
[Revenue At Risk] * 0.10
```

---

## 🔍 Key Insights

These findings were derived from the dashboard, SQL, and Python analysis:

1. Month-to-Month Contracts Drive Most Churn

Month-to-month contracts account for 88.5% of all churn (1,655 of 1,869 churned customers), making contract type the single strongest churn predictor in the dataset.

2. Fiber Optic Customers Churn at a Higher Rate

Fiber optic customers show a significantly higher churn rate than DSL customers, suggesting service quality or pricing may be a factor worth investigating further.

3. New Customers Are the Highest Risk Segment

Customers with 0-12 months of tenure churn at a much higher rate than customers with 49+ months tenure, pointing to a gap in early-stage onboarding or engagement.

4. Electronic Check Payment Correlates with Higher Churn

Customers paying via electronic check churn more frequently than those using automatic payment methods, indicating a possible link between payment friction and retention.

---
## 🎯 Skills Demonstrated

* Customer Churn Analysis
* Data Cleaning (Python, Power Query)
* Exploratory Data Analysis (EDA)
* SQL Aggregation and Segmentation
* KPI Development
* DAX Calculations
* Data Visualization
* Dashboard Storytelling
* Business Recommendation Development

## 📈 Dataset Information

| Property | Detail |
|----------|--------|
| Dataset | IBM Telco Customer Churn |
| Source | [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Total Customers | 7,043 |
| Churned Customers | 1,869 |
| Churn Rate | 26.54% |
| Monthly Revenue At Risk | $139,130.85 |
| Contract Types | Month-to-month, One year, Two year |
| Internet Services | DSL, Fiber optic, No internet |

---

## 🗄️ SQL Concepts Used

- `GROUP BY` with aggregate functions (`SUM`, `COUNT`, `AVG`)
- `CASE WHEN` for conditional logic and banding (tenure groups, charge bands)
- Subquery for above-average monthly charge filtering
- Common Table Expression (CTE) for revenue-at-risk summary
- `RANK()` window function for churn segment ranking

---

## 🐍 Python Analysis

The Python script performs data cleaning, feature engineering, and exploratory analysis independent of the Power BI dashboard, producing matching KPIs and supporting charts.

- Cleaned `TotalCharges` column (converted to numeric, filled missing values with median)
- Created `Tenure_Group` and `Monthly_Band` features using `apply()` and `pd.cut()`
- Used `pd.crosstab()` to analyze churn by contract, internet service, tenure, and payment method
- Generated and saved 3 charts using matplotlib
- Identified top 10 highest-value churned customers

---

## 💡 Business Recommendations

**1. Convert month-to-month customers to annual contracts**
With month-to-month driving 88.5% of churn, a targeted discount for switching to annual plans could meaningfully reduce churn volume.

**2. Investigate fiber optic service quality and pricing**
Fiber optic's higher churn rate compared to DSL warrants a closer look at pricing competitiveness and service reliability.

**3. Strengthen early-customer onboarding**
Since 0-12 month customers churn the most, a structured onboarding or check-in process in the first 90 days could reduce early churn.

**4. Reduce friction in electronic check payments**
Encouraging migration to automatic payment methods (credit card, bank transfer) may reduce churn tied to payment friction.

---

## 👤 About This Project

This project demonstrates end-to-end Customer Analytics and Business Intelligence capabilities, including Python-based data cleaning and EDA, SQL-based segmentation, Power BI dashboard creation, DAX calculations, and business recommendation generation.

**Core Technologies:**
`Power BI` `SQL` `DAX` `Python` `pandas` `matplotlib`

**Analytics Areas:**
`Customer Analytics` `Churn Analysis` `Revenue Risk Analysis` `Data Visualization`
`KPI Development` `Dashboard Storytelling` `Business Intelligence Reporting`

---

## 📬 Connect With Me

🔗 LinkedIn:
www.linkedin.com/in/suresh-pawar-a2b7bb26b

💻 GitHub:
github.com/Suru7971

📧 Email:
surupawar7971@gmail.com

---

> ⭐ If you found this project useful, feel free to star the repository!
