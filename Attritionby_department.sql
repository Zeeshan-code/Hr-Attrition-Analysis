SELECT Department,
  COUNT(*) AS total,
  SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS left_count,
  ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_pct
FROM hr_data
GROUP BY Department
ORDER BY attrition_pct DESC;