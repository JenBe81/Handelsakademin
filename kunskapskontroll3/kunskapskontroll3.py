# Kunskapskontroll 3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This method takes a data frame and a column. Then defines the first quantile, Q1, and the third quantile, Q3.
# 50% of the data will be inbetween Q1 and Q3, define this portion as IQR. Outliers is defined as any data point below
# Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR (not my definition, I found this description). Then the final step is to only
# include values that falls in between lower_bound and upper_bound and then returning the data frame again.
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    return df

# This method takes a data frame and a list of columns. For each column, it calls the remove_outliers method to
# clean away the outliers for the column. Once all the columns have been iterated the data frame should be clear
# of the outliers.
def remove_outliers_from_dataframe(df, columns):
    # First, check the data set before removing any outliers
    #for column in columns:
    #    plt.figure(figsize=(8, 6))
    #    sns.boxplot(data=df[column])
    #    plt.title(f"Box plot for {column}")
    #    plt.show()

    df_no_outliers = df.copy()
    
    for column in columns:
        df_no_outliers = remove_outliers(df_no_outliers, column)

    # Display the box plots for each numeric column to verify the outliers have been successfully removed.
    #for column in numeric_columns:
    #    plt.figure(figsize=(8, 6))
    #    sns.boxplot(data=df_no_outliers[column])
    #    plt.title(f"Box plot for {column}")
    #    plt.show()

    return df_no_outliers

#============================================================================
#                          GETTING THE DATA
#============================================================================
# Load CSV file into a pandas DataFrame
df = pd.read_csv("housing.csv", sep=",")

# Display the first few rows of the DataFrame
print(df.head())

#============================================================================
#                          CLEANING THE DATA
#============================================================================
# Check how many entries are missing in the DataFrame
print(df.isnull().sum())

# Check for duplicate rows
duplicate_count = df.duplicated().sum()
print(f'Number of duplicate rows: {duplicate_count}')

# Output shows that only total_bedrooms colum is missing entries, 207 entries missing
# No duplicates were found.

# Cleaning the dataset by removing rows with missing entries
df_cleaned = df.dropna(subset=['total_bedrooms'])

# Just to be sure, display how many missing entries remain after cleanup (should be 0)
print(df_cleaned.isnull().sum())

# Outliers are individual data points that are way off compared to all the other data points. They may be erronous
# entries and can potentially mess with the result (for instance significantly changing a mean value). So, check 
# the data set for outliers by using the box-and-whisker plots for each column containing numbers.
numeric_columns = df_cleaned.select_dtypes(include=['number']).columns.tolist()
df_no_outliers = remove_outliers_from_dataframe(df_cleaned, numeric_columns)

# There are just 5 INLAND houses so remove these as well as they are too few for reliable statistics
df_cleaned = df_no_outliers[df_no_outliers['ocean_proximity']!= 'ISLAND']

#============================================================================
#                          ANALYZING THE DATA
#============================================================================
# Create a new DataFrame without the 'ocean_proximity' column
numeric_df = df_cleaned.drop('ocean_proximity', axis=1)

# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
# corr() method can only handle numeric values and therefore this column is dropped when plotting the heatmap.
# From the heatmap you can see that median income is strongly correlated with house value.
# One can also see that total rooms/total bedrooms are correlated to the poulation
# Maybe a bit of correlation between median income and number of rooms but not super convincing
# Weak correlation between median age and housing value, a bit surprising. Maybe because median age seems
# rather uniform throughout the dataset. 

# Create scatter plots for most promising columns to further explore relationships
plt.figure(figsize=(10, 8))
sns.scatterplot(x='median_income', y='median_house_value', hue='ocean_proximity', data=df_cleaned)
plt.title("Median House Value vs. Median Income by Ocean Proximity")
plt.show()
# This is a cool plot where it is clearly shown that housing values definitely depends on ocean proximity
# Also in this plot you can see that house value depends on median income.

# Add the following lines at the end of your script to create the desired scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='latitude', y='longitude', hue='median_house_value', palette='coolwarm', data=df_cleaned)
plt.title("House Value by Position")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()

#============================================================================
#                          PLAYING AROUND
#============================================================================
import folium
from branca.colormap import LinearColormap

# Create a color map based on median_house_value
color_map = LinearColormap(['blue', 'green', 'yellow', 'red'], vmin=df_cleaned['median_house_value'].min(),
                           vmax=df_cleaned['median_house_value'].max(), caption='House Value')

# Calculate the mean of latitude and longitude for setting the map center
latitude_center = df_cleaned['latitude'].mean()
longitude_center = df_cleaned['longitude'].mean()

# Create the folium Map object
housing_map = folium.Map(location=[latitude_center, longitude_center], zoom_start=6)

# Add data points to the map
for index, row in df_cleaned.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=3,
        color=color_map(row['median_house_value']),
        fill=True,
        fill_opacity=0.7,
    ).add_to(housing_map)

# Add the color map legend to the map
housing_map.add_child(color_map)

# Save the map to an HTML file
housing_map.save("housing_map.html")
