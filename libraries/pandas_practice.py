import pandas as pd

# ======================================
# 1. LOAD CSV FILE
# ======================================

print("\n========== 1. LOAD CSV FILE ==========")

df = pd.read_csv("D:/anaconda/files/day24.py/day24_Employee_Data (1).csv")

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

# ======================================
# 2. BASIC INFORMATION
# ======================================

print("\n========== 2. BASIC INFORMATION ==========")

print("Shape :", df.shape)

print("\nColumns")
print(df.columns)

print("\nInformation")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# ======================================
# 3. DATA CLEANING
# ======================================

print("\n========== 3. DATA CLEANING ==========")

df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["Department"] = df["Department"].str.strip().str.title()

print(df[["Employee_Name","City","Department"]].head())

# ======================================
# 4. CHECK MISSING VALUES
# ======================================

print("\n========== 4. MISSING VALUES ==========")

print(df.isnull().sum())

# Fill Missing Values
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")

print("\nAfter Filling Missing Values")
print(df.isnull().sum())

# ======================================
# 5. REMOVE DUPLICATES
# ======================================

print("\n========== 5. REMOVE DUPLICATES ==========")

print("Duplicate Rows :", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicates Removed Successfully")

# ======================================
# 6. FILTER DATA
# ======================================

print("\n========== 6. FILTER DATA ==========")

mumbai = df[df["City"]=="Mumbai"]

print("\nEmployees From Mumbai")
print(mumbai)

high_salary = df[df["Salary"]>60000]

print("\nEmployees Salary > 60000")
print(high_salary)

# ======================================
# 7. SORTING
# ======================================

print("\n========== 7. SORTING ==========")

salary_sort = df.sort_values("Salary",ascending=False)

print(salary_sort.head())

joining_sort = df.sort_values("Joining_Year")

print(joining_sort.head())

# ======================================
# 8. SELECT COLUMNS
# ======================================

print("\n========== 8. SELECT COLUMNS ==========")

print(df[["Employee_Name","Department","Salary"]])

# ======================================
# 9. LOC
# ======================================

print("\n========== 9. LOC ==========")

print(df.loc[0])

print(df.loc[0:4])

# ======================================
# 10. ILOC
# ======================================

print("\n========== 10. ILOC ==========")

print(df.iloc[0])

print(df.iloc[0:5])

# ======================================
# 11. ADD NEW COLUMNS
# ======================================

print("\n========== 11. NEW COLUMNS ==========")

df["Salary_Category"] = df["Salary"].apply(
    lambda x:"High" if x>=60000 else "Medium" if x>=50000 else "Low"
)

df["Experience"] = 2025-df["Joining_Year"]

print(df.head())

# ======================================
# 12. VALUE COUNTS
# ======================================

print("\n========== 12. VALUE COUNTS ==========")

print(df["Department"].value_counts())

# ======================================
# 13. UNIQUE VALUES
# ======================================

print("\n========== 13. UNIQUE VALUES ==========")

print(df["Department"].unique())

print("Number of Departments :",df["Department"].nunique())

# ======================================
# 14. GROUP BY
# ======================================

print("\n========== 14. GROUP BY ==========")

print("\nAverage Salary By Department")

print(df.groupby("Department")["Salary"].mean())

print("\nMaximum Salary By Department")

print(df.groupby("Department")["Salary"].max())

print("\nMinimum Salary By Department")

print(df.groupby("Department")["Salary"].min())

print("\nEmployee Count")

print(df.groupby("Department")["Employee_ID"].count())

# ======================================
# 15. STATISTICS
# ======================================

print("\n========== 15. STATISTICS ==========")

print("Average Salary :",df["Salary"].mean())

print("Median Salary :",df["Salary"].median())

print("Maximum Salary :",df["Salary"].max())

print("Minimum Salary :",df["Salary"].min())

print("Salary Standard Deviation :",df["Salary"].std())

# ======================================
# 16. HIGHEST SALARY EMPLOYEE
# ======================================

print("\n========== 16. HIGHEST SALARY EMPLOYEE ==========")

highest = df[df["Salary"]==df["Salary"].max()]

print(highest)

# ======================================
# 17. LOWEST SALARY EMPLOYEE
# ======================================

print("\n========== 17. LOWEST SALARY EMPLOYEE ==========")

lowest = df[df["Salary"]==df["Salary"].min()]

print(lowest)

# ======================================
# 18. CORRELATION
# ======================================

print("\n========== 18. CORRELATION ==========")

print(df.corr(numeric_only=True))

# ======================================
# 19. RENAME COLUMN
# ======================================

print("\n========== 19. RENAME COLUMN ==========")

df.rename(columns={"Salary":"Monthly_Salary"},inplace=True)

print(df.head())

# ======================================
# 20. EXPORT FILES
# ======================================

print("\n========== 20. EXPORT ==========")

salary_sort.to_csv("Employee_Sorted_By_Salary.csv",index=False)

df.to_csv("Employee_Cleaned_Data.csv",index=False)

print("Files Exported Successfully!")

# ======================================
# 21. SAMPLE DATA
# ======================================

print("\n========== 21. RANDOM SAMPLE ==========")

print(df.sample(5))

# ======================================
# 22. DATA TYPES
# ======================================

print("\n========== 22. DATA TYPES ==========")

print(df.dtypes)

# ======================================
# END
# ======================================

print("\n🎉 Pandas Practice Completed Successfully!")