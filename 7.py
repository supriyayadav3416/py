import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'Month': ['Jan','Feb','Mar','Apr','May','Jun'],
        'Sales': [150,200,180,220,240,210]}

df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'], marker='o')
plt.title("Sales Line Graph")
plt.show()

sns.barplot(x='Month', y='Sales', data=df)
plt.title("Sales Bar Chart")
plt.show()

plt.hist(df['Sales'], bins=5, color='skyblue', edgecolor='black')
plt.title("Sales Histogram")
plt.show()
