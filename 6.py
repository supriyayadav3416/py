import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("customer_transactions.csv")
df = df.dropna().drop_duplicates()

print(df.describe())

df.hist(figsize=(5,4))
plt.show()

sns.boxplot(data=df.select_dtypes('number'))
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
