import pandas as pd

# Load your dataset into a DataFrame
df = pd.read_csv('movies_data.csv')

# Printing Data before its processed:
print("Dataset before its processed:")
print(df.head())

# Data Preprocessing

# Removing duplicates
df_no_duplicates = df.drop_duplicates()

# Display the DataFrame after removing duplicates
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

# Removing rows with missing values
df_no_missing = df.dropna()

# Display the DataFrame after removing rows with missing values
print("\nDataFrame after removing rows with missing values:")
print(df_no_missing)

# Remove rows with blank values in specific columns 
df = df.dropna(subset=['MOVIES'], how='all')
df = df.dropna(subset=['YEAR'], how='all')
df = df.dropna(subset=['GENRE'], how='all')
df = df.dropna(subset=['RATING'], how='all')
df = df.dropna(subset=['VOTES'], how='all')
df = df.dropna(subset=['RunTime'], how='all')

# Print the DataFrame after removing rows with blanks
print(df)

# Remove rows containing NaN values
df_cleaned = df.dropna()

# Print the cleaned DataFrame without rows containing NaN values
print(df_cleaned)

# Remove columns containing NaN values
df_cleaned = df.dropna(axis=1)

# Print the cleaned DataFrame without columns containing NaN values
print(df_cleaned)

# Feature Engineering

# Creating a New Feature (e.g., 'Count of Rating', 'Count of RunTime' etc)
# Generating summary statistics of numeric columns
print("\nSummary statistics of numeric columns:")
print(df.describe())

# Scaling Numeric Features (Min-Max Scaling)
numeric_columns = df.select_dtypes(include='number').columns

# Removing Unwanted Columns 
df = df.drop(['ONE-LINE'], axis=1)
df = df.drop(['STARS'], axis=1)
df = df.drop(['Gross'], axis=1)

# Print the data after removing unwanted columns
print("\nData after removing unwanted columns:")
print(df.head(100))

# Save the preprocessed and feature-engineered data to a new CSV file
df.to_csv('preprocessed_movies_data.csv', index=False)
