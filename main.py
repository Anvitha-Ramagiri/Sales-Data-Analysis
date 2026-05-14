# -----------------------------
# SALES DATA ANALYSIS PROJECT
# -----------------------------

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("data/SampleSuperstore.csv", encoding='latin1')

# Display First 5 Rows
print("FIRST 5 ROWS")
print(df.head())

# -----------------------------
# DATA CLEANING
# -----------------------------

# Check Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Remove unnecessary columns
df.drop(columns=['Returns', 'ind1', 'ind2'], inplace=True)

# Rename corrupted column
df.rename(columns={'ï»¿Row ID+O6G3A1:R6': 'Row ID'}, inplace=True)

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Dataset Info
print("\nDATASET INFO")
print(df.info())

# -----------------------------
# BASIC ANALYSIS
# -----------------------------

# Total Sales
total_sales = df['Sales'].sum()
print("\nTOTAL SALES:", round(total_sales, 2))

# Total Profit
total_profit = df['Profit'].sum()
print("TOTAL PROFIT:", round(total_profit, 2))

# Total Orders
total_orders = df['Order ID'].nunique()
print("TOTAL ORDERS:", total_orders)

# Average Sales
average_sales = df['Sales'].mean()
print("AVERAGE SALES:", round(average_sales, 2))

# -----------------------------
# TOP SELLING PRODUCTS
# -----------------------------

top_products = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP SELLING PRODUCTS")
print(top_products.head(10))

# -----------------------------
# SALES BY REGION
# -----------------------------

region_sales = df.groupby('Region')['Sales'].sum()

print("\nSALES BY REGION")
print(region_sales)

# -----------------------------
# MONTHLY SALES TREND
# -----------------------------

monthly_sales = (
    df.groupby(df['Order Date'].dt.month)['Sales']
    .sum()
)

print("\nMONTHLY SALES")
print(monthly_sales)

# -----------------------------
# TOP STATES BY SALES
# -----------------------------

top_states = (
    df.groupby('State')['Sales']
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP STATES BY SALES")
print(top_states.head(10))

# -----------------------------
# CATEGORY WISE SALES
# -----------------------------

category_sales = df.groupby('Category')['Sales'].sum()

print("\nCATEGORY WISE SALES")
print(category_sales)

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

df.to_csv("output/cleaned_superstore_data.csv", index=False)

print("\nCleaned Data Saved Successfully!")

# -----------------------------
# DASHBOARD VISUALIZATION
# -----------------------------

fig, axes = plt.subplots(2, 3, figsize=(10, 6))

# -----------------------------
# 1. SALES BY REGION
# -----------------------------

region_sales.plot(
    kind='bar',
    ax=axes[0, 0],
    title='Sales by Region'
)

axes[0, 0].set_xlabel("Region", fontsize=8)
axes[0, 0].set_ylabel("Sales", fontsize=8)

axes[0, 0].tick_params(axis='x', labelsize=7)
axes[0, 0].tick_params(axis='y', labelsize=7)

# -----------------------------
# 2. TOP SELLING PRODUCTS
# -----------------------------

top_products.head(10).plot(
    kind='bar',
    ax=axes[0, 1],
    title='Top Products'
)

axes[0, 1].set_xlabel("Sub-Category", fontsize=8)
axes[0, 1].set_ylabel("Sales", fontsize=8)

axes[0, 1].tick_params(axis='x', labelsize=6)
axes[0, 1].tick_params(axis='y', labelsize=7)

# -----------------------------
# 3. MONTHLY SALES TREND
# -----------------------------

monthly_sales.plot(
    kind='line',
    marker='o',
    ax=axes[0, 2],
    title='Monthly Sales'
)

axes[0, 2].set_xlabel("Month", fontsize=8)
axes[0, 2].set_ylabel("Sales", fontsize=8)

axes[0, 2].tick_params(axis='x', labelsize=7)
axes[0, 2].tick_params(axis='y', labelsize=7)

# -----------------------------
# 4. CATEGORY WISE SALES
# -----------------------------

category_sales.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[1, 0],
    title='Category Sales'
)

axes[1, 0].set_ylabel("")

# -----------------------------
# 5. TOP STATES BY SALES
# -----------------------------

top_states.head(10).plot(
    kind='bar',
    ax=axes[1, 1],
    title='Top States'
)

axes[1, 1].set_xlabel("State", fontsize=8)
axes[1, 1].set_ylabel("Sales", fontsize=8)

axes[1, 1].tick_params(axis='x', labelsize=6)
axes[1, 1].tick_params(axis='y', labelsize=7)

# -----------------------------
# EMPTY SPACE
# -----------------------------

axes[1, 2].axis('off')

# -----------------------------
# DASHBOARD TITLE
# -----------------------------

fig.suptitle(
    "Sales Dashboard",
    fontsize=14,
    fontweight='bold'
)

# -----------------------------
# ADJUST LAYOUT
# -----------------------------

plt.tight_layout()

# -----------------------------
# SAVE DASHBOARD
# -----------------------------

plt.savefig(
    "output/sales_dashboard.png",
    dpi=300,
    bbox_inches='tight'
)

# -----------------------------
# SHOW DASHBOARD
# -----------------------------

plt.show()

print("\nPROJECT EXECUTED SUCCESSFULLY!")
print("Dashboard saved inside OUTPUT folder.")