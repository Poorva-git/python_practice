import matplotlib.pyplot as plt

# ==========================================
# 1. Line Chart
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 30000, 28000, 35000]

plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()


# ==========================================
# 2. Bar Chart
# ==========================================

departments = ["HR", "IT", "Sales", "Finance"]
employees = [12, 25, 18, 10]

plt.figure(figsize=(6,4))
plt.bar(departments, employees)
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.savefig("bar_chart.png")
plt.show()


# ==========================================
# 3. Pie Chart
# ==========================================

labels = ["Python", "SQL", "Excel", "Power BI"]
sizes = [35, 25, 20, 20]

plt.figure(figsize=(6,6))
plt.pie(sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Skills Distribution")
plt.savefig("pie_chart.png")
plt.show()


# ==========================================
# 4. Scatter Plot
# ==========================================

experience = [1,2,3,4,5,6,7]
salary = [25000,30000,38000,45000,55000,65000,80000]

plt.figure(figsize=(6,4))
plt.scatter(experience, salary)
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.show()


# ==========================================
# 5. Histogram
# ==========================================

marks = [45,55,60,65,70,75,80,85,90,95,55,60,72,81,67,74,88]

plt.figure(figsize=(6,4))
plt.hist(marks, bins=5)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("histogram.png")
plt.show()


# ==========================================
# 6. Multiple Line Chart
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]

product_a = [20,25,30,35,40]
product_b = [15,20,28,30,36]

plt.figure(figsize=(6,4))
plt.plot(months, product_a, marker='o', label="Product A")
plt.plot(months, product_b, marker='s', label="Product B")

plt.title("Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.savefig("multiple_line_chart.png")
plt.show()


print("Matplotlib Practice Completed Successfully!")