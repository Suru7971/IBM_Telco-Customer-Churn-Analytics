-- ============================================================
-- IBM Telco Customer Churn Analysis
-- Author   : Suresh Vakil Pawar
-- Dataset  : IBM Telco Customer Churn (Kaggle)
-- Tool     : MySQL
-- Goal     : Identify churn drivers and quantify revenue risk
-- ============================================================

USE telco_db;

-- ============================================================
-- 1. Data Preview
-- ============================================================
SELECT *
FROM telco_churn
LIMIT 10;

-- ============================================================
-- 2. Total Customers
-- ============================================================
SELECT
    COUNT(*) AS total_customers
FROM telco_churn;

-- ============================================================
-- 3. Churn vs Retained Count
-- ============================================================
SELECT
    Churn,
    COUNT(*) AS customers
FROM telco_churn
GROUP BY Churn;

-- ============================================================
-- 4. Overall KPI Summary
-- All headline numbers in one result row
-- ============================================================
SELECT
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct,
    ROUND(AVG(MonthlyCharges), 2)                              AS avg_monthly_charges,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes'
            THEN MonthlyCharges ELSE 0 END), 2)                AS revenue_at_risk
FROM telco_churn;

-- ============================================================
-- 5. Churn by Contract Type with Churn Rate %
-- Month-to-month customers churn the most
-- ============================================================
SELECT
    Contract,
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct
FROM telco_churn
GROUP BY Contract
ORDER BY churn_customers DESC;

-- ============================================================
-- 6. Churn by Internet Service with Churn Rate %
-- Fiber optic has significantly higher churn rate than DSL
-- ============================================================
SELECT
    InternetService,
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct
FROM telco_churn
GROUP BY InternetService
ORDER BY churn_customers DESC;

-- ============================================================
-- 7. Churn by Monthly Charge Band
-- Higher spending customers show higher churn
-- ============================================================
SELECT
    CASE
        WHEN MonthlyCharges <= 30 THEN '1. 0-30'
        WHEN MonthlyCharges <= 60 THEN '2. 31-60'
        WHEN MonthlyCharges <= 90 THEN '3. 61-90'
        ELSE '4. 91+'
    END                                                         AS monthly_charge_band,
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct
FROM telco_churn
GROUP BY monthly_charge_band
ORDER BY monthly_charge_band;

-- ============================================================
-- 8. Churn by Tenure Group
-- New customers (0-12 months) churn at the highest rate
-- ============================================================
SELECT
    CASE
        WHEN tenure <= 12 THEN '1. 0-12 Months'
        WHEN tenure <= 24 THEN '2. 13-24 Months'
        WHEN tenure <= 48 THEN '3. 25-48 Months'
        ELSE '4. 49+ Months'
    END                                                         AS tenure_group,
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct
FROM telco_churn
GROUP BY tenure_group
ORDER BY tenure_group;

-- ============================================================
-- 9. Churn by Payment Method
-- Electronic check users churn most frequently
-- ============================================================
SELECT
    PaymentMethod,
    COUNT(*)                                                    AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)            AS churn_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2)                                 AS churn_rate_pct
FROM telco_churn
GROUP BY PaymentMethod
ORDER BY churn_customers DESC;

-- ============================================================
-- 10. Above Average Monthly Charges — Subquery
-- High value customers at risk of churning
-- ============================================================
SELECT
    customerID,
    Contract,
    InternetService,
    MonthlyCharges,
    Churn
FROM telco_churn
WHERE MonthlyCharges > (
    SELECT AVG(MonthlyCharges) FROM telco_churn
)
ORDER BY MonthlyCharges DESC
LIMIT 20;

-- ============================================================
-- 11. Revenue At Risk by Contract — CTE
-- Quantifies monthly revenue lost per contract type
-- ============================================================
WITH revenue_summary AS (
    SELECT
        Contract,
        COUNT(*)                        AS churn_customers,
        ROUND(SUM(MonthlyCharges), 2)  AS revenue_at_risk
    FROM telco_churn
    WHERE Churn = 'Yes'
    GROUP BY Contract
)
SELECT
    *,
    ROUND(revenue_at_risk * 0.10, 2)  AS recovery_at_10pct
FROM revenue_summary
ORDER BY revenue_at_risk DESC;

-- ============================================================
-- 12. Churn Segment Ranking — Window Function (RANK)
-- Ranks each contract + internet segment by churn volume
-- ============================================================
SELECT
    Contract,
    InternetService,
    COUNT(*)                                        AS churn_customers,
    ROUND(SUM(MonthlyCharges), 2)                  AS revenue_at_risk,
    RANK() OVER (ORDER BY COUNT(*) DESC)           AS churn_rank
FROM telco_churn
WHERE Churn = 'Yes'
GROUP BY Contract, InternetService
ORDER BY churn_rank;

-- ============================================================
-- Key Findings:
-- 1. Churn rate               : 26.54%
-- 2. Month-to-month contracts : 88.5% of all churn
-- 3. Fiber optic churn rate   : highest among internet types
-- 4. New customers (0-12m)    : highest churn risk group
-- 5. Electronic check         : highest churn payment method
-- 6. Revenue at risk          : $139,130.85 per month
-- 7. 10% recovery potential   : $13,913 per month
-- ============================================================
