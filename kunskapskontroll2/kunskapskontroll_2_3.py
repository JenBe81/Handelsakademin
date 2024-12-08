# kunskapskontroll_2_3.py

import pandas as pd
import numpy as np

print("Task: Explain what CSV file is")
print("CSV stands for Comma-Separated Values and is a plain text file that stored tabular data where each value is separated with a comma character")

cars = pd.read_csv("cars_data.csv")

print("\nTask: Print the first 10 rows of the data")
print(cars.head(10))

print("\nTask: Print the last 5 rows of the data")
print(cars.tail())

print("\nTask: By using the info method, check how many non-null rows each column have.")
print(cars.info())

print("\nTask: If any column has missing value, drop the entire row. Notice, the operation should be inplace meaning you change the dataframe itself.")
print("First check how many rows have missing values")
print(cars.isnull().sum())
print("Then remove rows with empty values using dropna() method")
cars.dropna(inplace=True)
print("Then check again how many rows have missing values")
print(cars.isnull().sum())

print("\nTask: Calculate the mean aof each numeric column.")
#numeric_columns = cars.select_dtypes(include=['numeric'])
numeric_columns = cars.select_dtypes(include=['int64', 'float64'])
column_means = numeric_columns.mean()
print(column_means)

print("\nTask: Select the rows where column 'company' is equal to 'honda'")
honda_cars = cars.loc[cars['company'] == 'honda']
print(honda_cars)

print("\nTask: Sort the data set by price in descending order. This should not be an inplace operation")
sorted_cars = cars.sort_values(by='price', ascending=False)
print(sorted_cars)

print("\nTask: Select the rows where column 'company' is equal to any of the values 'audi', 'bmw', 'porsche'")
#high_brand_cars = cars.loc[(cars['company'] == 'audi') or (cars['company'] == 'bmw') or (cars['company'] == 'porsche')]
#print(high_brand_cars)
# The above did not work because cars['company'] == 'xyz' returns a boolean series and doing or operation on series is ambiguous.
# So, try instead to iterate over the each brand of interest

interesting_car_brands = ['audi', 'bmw', 'porsche']
high_brand_cars = pd.DataFrame(columns=cars.columns) # Create an empty DataFrame with the same columns as the cars DataFrame
for car in interesting_car_brands:
    selected_cars = cars.loc[cars['company'] == car]
    high_brand_cars = pd.concat([high_brand_cars, selected_cars], ignore_index=True)
    # At first I made a print statement here print each brand for each iteration. But the printout did not looks so nice
    # since a header row was included for each print statement. That is what I thought it was better to do a concat operation instead.

print(high_brand_cars)

print("\nTask: Find hte number of cars, rows, for each company")
company_counts = cars['company'].value_counts()
print(company_counts)

print("\nFind the maximum price for each company")
max_prices = cars.groupby('company')['price'].max()
print(max_prices.sort_values(ascending=True))
      