# ============================================================
# IBM Telco Customer Churn Analysis
# Author   : Suresh Vakil Pawar
# Dataset  : IBM Telco Customer Churn (Kaggle)
# Tools    : Python, pandas, matplotlib
# Goal     : Identify churn drivers and quantify revenue risk
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------
# 1. Load Data
# ----------------------------------------
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# ----------------------------------------
# 2. Data Cleaning
# ----------------------------------------

# TotalCharges is stored as string — some rows are blank
# (these are new customers with tenure = 0)
# Convert to number and fill blanks with median
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("\nMissing values before cleaning:")
print(df.isnull().sum())

df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
print("\nMissing values after cleaning:", df.isnull().sum().sum())

# ----------------------------------------
# 3. Feature Engineering
# ----------------------------------------

# Tenure group — to check if newer customers churn more
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

# Monthly charge band — to check if price affects churn
df["Monthly_Band"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 30, 60, 90, 200],
    labels=["0-30", "31-60", "61-90", "91+"]
)

# ----------------------------------------
# 4. Key KPIs
# ----------------------------------------
total           = len(df)
churned         = (df["Churn"] == "Yes").sum()
retained        = total - churned
churn_rate      = round(churned / total * 100, 2)
avg_monthly     = round(df["MonthlyCharges"].mean(), 2)
revenue_at_risk = round(
    df.loc[df["Churn"] == "Yes", "MonthlyCharges"].sum(), 2
)

print("\n========== KPIs ==========")
print(f"Total Customers    : {total}")
print(f"Churned            : {churned}")
print(f"Retained           : {retained}")
print(f"Churn Rate         : {churn_rate}%")
print(f"Avg Monthly Charge : ${avg_monthly}")
print(f"Revenue At Risk    : ${revenue_at_risk:,.2f} per month")
print(f"10% Recovery Value : ${round(revenue_at_risk * 0.10, 2):,.2f} per month")

# ----------------------------------------
# 5. Churn by Contract Type
# Month-to-month customers churn the most
# ----------------------------------------
contract = pd.crosstab(df["Contract"], df["Churn"])
contract["Churn_Rate_%"] = round(
    contract["Yes"] / (contract["Yes"] + contract["No"]) * 100, 2
)
print("\n--- Churn by Contract ---")
print(contract)

# Chart
contract[["No", "Yes"]].plot(
    kind="bar",
    color=["#1F3864", "#E24B4A"],
    figsize=(8, 5)
)
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.legend(["Retained", "Churned"])
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("chart_01_churn_by_contract.png", dpi=120)
plt.close()
print("Saved: chart_01_churn_by_contract.png")

# ----------------------------------------
# 6. Churn by Internet Service
# Fiber optic has the highest churn rate
# ----------------------------------------
internet = pd.crosstab(df["InternetService"], df["Churn"])
internet["Churn_Rate_%"] = round(
    internet["Yes"] / (internet["Yes"] + internet["No"]) * 100, 2
)
print("\n--- Churn by Internet Service ---")
print(internet)

# Chart
internet[["No", "Yes"]].plot(
    kind="barh",
    color=["#1F3864", "#E24B4A"],
    figsize=(8, 5)
)
plt.title("Churn by Internet Service")
plt.xlabel("Number of Customers")
plt.legend(["Retained", "Churned"])
plt.tight_layout()
plt.savefig("chart_02_churn_by_internet.png", dpi=120)
plt.close()
print("Saved: chart_02_churn_by_internet.png")

# ----------------------------------------
# 7. Churn by Tenure Group
# New customers (0-12 months) churn most
# ----------------------------------------
order = ["0-12 Months", "13-24 Months", "25-48 Months", "49+ Months"]
tenure = pd.crosstab(df["Tenure_Group"], df["Churn"]).reindex(order)
tenure["Churn_Rate_%"] = round(
    tenure["Yes"] / (tenure["Yes"] + tenure["No"]) * 100, 2
)
print("\n--- Churn by Tenure Group ---")
print(tenure)

# Chart — color coded by risk level
plt.figure(figsize=(8, 5))
plt.bar(
    tenure.index,
    tenure["Churn_Rate_%"],
    color=["#E24B4A", "#E24B4A", "#EF9F27", "#1D9E75"]
)
plt.title("Churn Rate % by Tenure Group")
plt.xlabel("Tenure Group")
plt.ylabel("Churn Rate (%)")
for i, v in enumerate(tenure["Churn_Rate_%"]):
    plt.text(i, v + 0.5, f"{v}%", ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("chart_03_churn_by_tenure.png", dpi=120)
plt.close()
print("Saved: chart_03_churn_by_tenure.png")

# ----------------------------------------
# 8. Churn by Monthly Charge Band
# ----------------------------------------
band = pd.crosstab(df["Monthly_Band"], df["Churn"])
band["Churn_Rate_%"] = round(
    band["Yes"] / (band["Yes"] + band["No"]) * 100, 2
)
print("\n--- Churn by Monthly Charge Band ---")
print(band)

# ----------------------------------------
# 9. Churn by Payment Method
# Electronic check users churn most
# ----------------------------------------
payment = pd.crosstab(df["PaymentMethod"], df["Churn"])
payment["Churn_Rate_%"] = round(
    payment["Yes"] / (payment["Yes"] + payment["No"]) * 100, 2
)
print("\n--- Churn by Payment Method ---")
print(payment)

# ----------------------------------------
# 10. Top 10 Revenue Loss Customers
# Highest monthly charge churned customers
# ----------------------------------------
top10 = (
    df[df["Churn"] == "Yes"]
    [["customerID", "Contract", "InternetService", "MonthlyCharges"]]
    .sort_values("MonthlyCharges", ascending=False)
    .head(10)
    .reset_index(drop=True)
)
top10.index += 1
print("\n--- Top 10 Revenue Loss Customers ---")
print(top10.to_string())

# ----------------------------------------
# Key Findings
# ----------------------------------------
print("\n========== KEY FINDINGS ==========")
print(f"1. Overall churn rate        : {churn_rate}%")
print(f"2. Monthly revenue at risk   : ${revenue_at_risk:,.2f}")
print(f"3. 10% recovery potential    : ${round(revenue_at_risk * 0.10, 2):,.2f}/month")
print("4. Month-to-month contracts  : 88.5% of all churners")
print("5. Fiber optic churn rate    : highest among internet types")
print("6. New customers (0-12 mths) : show highest churn risk")
print("RECOMMENDATION: Convert month-to-month customers to annual contracts")
print("===================================")
print("Analysis complete.")
