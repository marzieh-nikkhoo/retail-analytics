#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#DATA ANALYSIS PYTHON PROJECT-RETAIL

df=pd.read_csv("retail_data.csv")

##sample

df.head(20)

##sample

df.tail(10)

##size of data

print("size of data",df.shape)

##field info

print("name of column",df.columns)

##data types

print("name of column",df.dtypes)

##data cleaning

print(df['Item Fat Content'].unique())
df['Item Fat Content']=df['Item Fat Content'].replace({'LF':'Low Fat','low fat':'Low Fat','reg':'Regular'})
print(df['Item Fat Content'].unique())

##business requirments

###KPI's requirments

#1-total sales
total_sales=df['Sales'].sum()

#2-average sales
avg_sales=df['Sales'].mean()

#3-no of item sold
no_of_item_sold=df['Sales'].count()
 
#4-average ratings
avg_ratings=df['Rating'].mean()

#5_display
print(f"total sales:${total_sales:,.0f}")
print(f"average sales:${avg_sales:,.0f}")
print(f"no of item sold:{no_of_item_sold:,.0f}")
print(f"average ratings:{avg_ratings:,.0f}")

###CHART's requirments

#1_total sales by fat content
sales_by_fat=df.groupby('Item Fat Content')['Sales'].sum()
plt.pie(sales_by_fat,labels= sales_by_fat.index,
                   autopct='%.1f%%',
                startangle=90)
plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()
