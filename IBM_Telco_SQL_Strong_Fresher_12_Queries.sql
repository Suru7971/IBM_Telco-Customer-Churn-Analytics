-- IBM TELCO CUSTOMER CHURN ANALYSIS
USE telco_db;

--1
SELECT * FROM telco_churn LIMIT 10;
--2
SELECT COUNT(*) AS Total_Customers FROM telco_churn;
--3
SELECT Churn,COUNT(*) Customers FROM telco_churn GROUP BY Churn;
--4
SELECT Contract,COUNT(*) Customers,SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) Churn_Customers FROM telco_churn GROUP BY Contract ORDER BY Churn_Customers DESC;
--5
SELECT InternetService,COUNT(*) Customers,SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) Churn_Customers FROM telco_churn GROUP BY InternetService ORDER BY Churn_Customers DESC;
--6
SELECT Contract,ROUND(AVG(MonthlyCharges),2) Avg_Monthly_Charges FROM telco_churn GROUP BY Contract;
--7
SELECT CASE WHEN tenure<=12 THEN '0-12 Months' WHEN tenure<=24 THEN '13-24 Months' WHEN tenure<=48 THEN '25-48 Months' ELSE '49+ Months' END Tenure_Group,COUNT(*) Customers,SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) Churn_Customers FROM telco_churn GROUP BY Tenure_Group;
--8
SELECT CASE WHEN MonthlyCharges<=30 THEN '0-30' WHEN MonthlyCharges<=60 THEN '31-60' WHEN MonthlyCharges<=90 THEN '61-90' ELSE '91+' END Monthly_Band,COUNT(*) Customers,SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) Churn_Customers FROM telco_churn GROUP BY Monthly_Band;
--9 CTE
WITH ChurnData AS (SELECT Contract,MonthlyCharges FROM telco_churn WHERE Churn='Yes') SELECT Contract,COUNT(*) Churn_Customers,ROUND(AVG(MonthlyCharges),2) Avg_Monthly_Charge FROM ChurnData GROUP BY Contract;
--10 CTE
WITH Revenue AS (SELECT Contract,SUM(MonthlyCharges) Revenue_At_Risk FROM telco_churn WHERE Churn='Yes' GROUP BY Contract) SELECT * FROM Revenue ORDER BY Revenue_At_Risk DESC;
--11 Window
SELECT customerID,Contract,MonthlyCharges,RANK() OVER(ORDER BY MonthlyCharges DESC) Charge_Rank FROM telco_churn;
--12 Window
SELECT customerID,MonthlyCharges,AVG(MonthlyCharges) OVER() Overall_Average FROM telco_churn;