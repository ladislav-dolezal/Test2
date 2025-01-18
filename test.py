import pandas as pd


data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32, 45]}

df = pd.DataFrame(data)
total_age = df['Age'].sum()
print("Total Age:", total_age)
print(df)