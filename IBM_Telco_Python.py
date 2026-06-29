"""
IBM Telco Customer Churn Analysis
Strong Fresher Python Project

Tools:
- pandas
- matplotlib

"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preview
print(df.head())
print(df.shape)

# Check missing values
print(df.isnull().sum())

# Clean TotalCharges
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Basic KPIs
total_customers = len(df)
churn_customers = len(df[df["Churn"]=="Yes"])
churn_rate = round(churn_customers / total_customers * 100,2)

print("Total Customers:", total_customers)
print("Churn Customers:", churn_customers)
print("Churn Rate:", churn_rate,"%")

# Churn by Contract
contract = pd.crosstab(df["Contract"], df["Churn"])
print(contract)

contract.plot(kind="bar")
plt.title("Churn by Contract")
plt.xlabel("Contract")
plt.ylabel("Customers")
plt.tight_layout()
plt.show()

# Churn by Internet Service
internet = pd.crosstab(df["InternetService"], df["Churn"])
print(internet)

internet.plot(kind="bar")
plt.title("Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Customers")
plt.tight_layout()
plt.show()

# Tenure Group
def tenure_group(x):
    if x <= 12:
        return "0-12 Months"
    elif x <= 24:
        return "13-24 Months"
    elif x <= 48:
        return "25-48 Months"
    else:
        return "49+ Months"

df["Tenure_Group"] = df["tenure"].apply(tenure_group)

tenure = pd.crosstab(df["Tenure_Group"], df["Churn"])
print(tenure)

# Monthly Charges Band
bins = [0,30,60,90,200]
labels = ["0-30","31-60","61-90","91+"]

df["Monthly_Band"] = pd.cut(df["MonthlyCharges"], bins=bins, labels=labels)

band = pd.crosstab(df["Monthly_Band"], df["Churn"])
print(band)

# Average Monthly Charges by Contract
avg = df.groupby("Contract")["MonthlyCharges"].mean().round(2)
print(avg)

# Top 10 Monthly Charges
top10 = df.sort_values("MonthlyCharges", ascending=False)[
    ["customerID","Contract","MonthlyCharges","Churn"]
].head(10)

print(top10)

print("Analysis Completed")
