import pandas as pd
import matplotlib.pyplot as plt

# retail data analysis project

df = pd.read_csv("retail_data.csv")

# first look at the data
print(df.head(20))
print(df.tail(10))

print("shape:", df.shape)
print("columns:", df.columns.tolist())
print("dtypes:\n", df.dtypes)

# fat content column has messy values like 'LF' and 'low fat'
# they all mean the same thing so clean them up
print("before:", df['Item Fat Content'].unique())

df['Item Fat Content'] = df['Item Fat Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})

print("after:", df['Item Fat Content'].unique())

# calculate the main KPIs
total_sales = df['Sales'].sum()
avg_sales = df['Sales'].mean()
no_items_sold = df['Sales'].count()
avg_rating = df['Rating'].mean()

print(f"\ntotal sales: ${total_sales:,.0f}")
print(f"average sales: ${avg_sales:,.2f}")
print(f"items sold: {no_items_sold:,}")
print(f"average rating: {avg_rating:.2f}")

# pie chart - sales split by fat content
sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(sales_by_fat, labels=sales_by_fat.index, autopct='%.1f%%', startangle=90)
ax.set_title('Total Sales by Fat Content')
plt.tight_layout()
plt.savefig("images/sales_by_fat_content.png")
plt.show()