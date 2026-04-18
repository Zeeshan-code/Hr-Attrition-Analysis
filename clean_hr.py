import pandas as pd

df = pd.read_csv(r'C:\Users\zeekh\OneDrive\Desktop\hr_project\WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Basic info
print("Shape:", df.shape)
print("\nAttrition counts:")
print(df['Attrition'].value_counts())
print("\nAttrition rate:", round(df['Attrition'].value_counts(normalize=True)['Yes'] * 100, 2), "%")

# Attrition by Department
print("\n=== ATTRITION BY DEPARTMENT ===")
dept = df.groupby('Department')['Attrition'].value_counts(normalize=True).unstack()
print((dept * 100).round(2))

# Attrition by Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[18,25,35,45,55,65],
                         labels=['18-25','26-35','36-45','46-55','56-65'])
print("\n=== ATTRITION RATE BY AGE GROUP ===")
age_att = df.groupby('AgeGroup', observed=True)['Attrition'].apply(
    lambda x: (x=='Yes').sum() / len(x) * 100).round(2)
print(age_att)

# Attrition by Job Role
print("\n=== ATTRITION BY JOB ROLE ===")
role = df.groupby('JobRole')['Attrition'].value_counts(normalize=True).unstack()
print((role * 100).round(2))

# Salary vs Attrition
print("\n=== AVG MONTHLY INCOME: LEFT vs STAYED ===")
print(df.groupby('Attrition')['MonthlyIncome'].mean().round(2))

# Work life balance
print("\n=== AVG WORK LIFE BALANCE: LEFT vs STAYED ===")
print(df.groupby('Attrition')['WorkLifeBalance'].mean().round(2))

# Years at company
print("\n=== AVG YEARS AT COMPANY: LEFT vs STAYED ===")
print(df.groupby('Attrition')['YearsAtCompany'].mean().round(2))

# Save cleaned file
df.to_csv(r'C:\Users\zeekh\OneDrive\Desktop\hr_project\hr_clean.csv', index=False)
print("\nDone! Cleaned file saved as hr_clean.csv")