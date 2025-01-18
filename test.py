import pandas as pd


data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Pepo', 'bado'],
    'Age': [28, 24, 35, 32, 45, 50]}

df = pd.DataFrame(data)
total_age = df['Age'].sum()
print("Total Age:", total_age)
print(df)