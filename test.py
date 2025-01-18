import pandas as pd


data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Pepo', 'lado', 'edo'],
    'Age': [28, 24, 35, 32, 45, 50, 47]}

df = pd.DataFrame(data)
total_age = df['Age'].sum()
print("Total Age:", total_age)
print(df)