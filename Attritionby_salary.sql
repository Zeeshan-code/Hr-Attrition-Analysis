SELECT Attrition,
  ROUND(AVG(MonthlyIncome), 2) AS avg_salary,
  ROUND(AVG(YearsAtCompany), 2) AS avg_years,
  ROUND(AVG(WorkLifeBalance), 2) AS avg_worklife
FROM hr_data
GROUP BY Attrition;