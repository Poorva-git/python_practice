import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
tips = sns.load_dataset("tips")

# ==========================================
# 1. Dataset Preview
# ==========================================

print("\nFirst 5 Rows")
print(tips.head())

print("\nDataset Information")
print(tips.info())

print("\nStatistical Summary")
print(tips.describe())

# ==========================================
# 2. Scatter Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter Plot - Total Bill vs Tip")
plt.savefig("scatter_plot.png")
plt.show()

# ==========================================
# 3. Line Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.lineplot(data=tips, x="size", y="total_bill")
plt.title("Line Plot")
plt.savefig("line_plot.png")
plt.show()

# ==========================================
# 4. Bar Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Bill by Day")
plt.savefig("bar_plot.png")
plt.show()

# ==========================================
# 5. Count Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.countplot(data=tips, x="day")
plt.title("Customers by Day")
plt.savefig("count_plot.png")
plt.show()

# ==========================================
# 6. Histogram
# ==========================================

plt.figure(figsize=(6,4))
sns.histplot(data=tips, x="total_bill", bins=10)
plt.title("Histogram of Total Bill")
plt.savefig("histogram.png")
plt.show()

# ==========================================
# 7. Box Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Box Plot")
plt.savefig("box_plot.png")
plt.show()

# ==========================================
# 8. Violin Plot
# ==========================================

plt.figure(figsize=(6,4))
sns.violinplot(data=tips, x="day", y="total_bill")
plt.title("Violin Plot")
plt.savefig("violin_plot.png")
plt.show()

# ==========================================
# 9. Heatmap
# ==========================================

plt.figure(figsize=(6,5))
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()

# ==========================================
# 10. Pair Plot
# ==========================================

pair = sns.pairplot(tips)
pair.figure.suptitle("Pair Plot", y=1.02)
pair.savefig("pairplot.png")
plt.show()

print("\nSeaborn Practice Completed Successfully!")