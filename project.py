import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\radhi\\Desktop\\DATASETS.csv")
print(df)
print(df.shape)
print(df.head(10))
print(df.info())
print(pd.isnull(df).sum())
print(df.dropna(inplace=True))
print(df.shape)
print(df.columns)
df.to_csv("final_superstore.csv", index=False)
print(df.to_csv)

#Product Category
 # Sales by Region
ax = sns.barplot(data=df, x='Region', y='Sales', estimator=sum)

# Add labels on top of bars
for container in ax.containers:
    ax.bar_label(container)

plt.title("Total Sales by Region")
plt.show()



# total number of orders from top 10 city
# Step 1: Group by City and count orders
top_cities = df.groupby('City').size().reset_index(name='Orders')

# Step 2: Sort and take top 10
top_cities = top_cities.sort_values(by='Orders', ascending=False).head(10)

# Step 3: Plot
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_cities, x='City', y='Orders')
plt.title("Total Number of Orders from Top 10 Cities")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# total number of orders from top 10 states
# Step 1: Group by State and count orders
top_states = df.groupby('State').size().reset_index(name='Orders')

# Step 2: Sort and take top 10
top_states = top_states.sort_values(by='Orders', ascending=False).head(10)

# Step 3: Plot
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_states, x='State', y='Orders')
plt.title("Total Number of Orders from Top 10 States")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Top Category
# Step 1: Group by Category and count orders
top_category = df.groupby('Category').size().reset_index(name='Orders')

# Step 2: Sort (optional here, since there are usually few categories)
top_category = top_category.sort_values(by='Orders', ascending=False)

# Step 3: Plot
sns.set(rc={'figure.figsize': (10, 5)})
sns.barplot(data=top_category, x='Category', y='Orders')
plt.title("Total Number of Orders by Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#top 10 Sub-Categories
# Step 1: Group by Sub-Category and count orders
top_subcat = df.groupby('Sub-Category').size().reset_index(name='Orders')

# Step 2: Sort and take top 10
top_subcat = top_subcat.sort_values(by='Orders', ascending=False).head(10)

# Step 3: Plot
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=top_subcat, x='Sub-Category', y='Orders')
plt.title("Total Number of Orders from Top 10 Sub-Categories")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()







