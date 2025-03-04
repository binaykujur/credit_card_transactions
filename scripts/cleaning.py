import pandas as pd

# Load the dataset
csv_file = 'raw_data/indian_credit_card_transactions.csv'
df = pd.read_csv(csv_file)

print("Initial dataset loaded. First 5 rows:")
print(df.head())

# 1. 🔄 Simple Data Cleaning
# Remove duplicates
df = df.drop_duplicates()

# Check for missing values and drop if any
if df.isnull().sum().sum() > 0:
    df = df.dropna()

# Standardize phone numbers by removing special characters
df['PhoneNumber'] = df['PhoneNumber'].replace(r'\D', '', regex=True)

# Convert date to datetime format
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'], format='%Y-%m-%d %H:%M:%S')

# 2. 🔍 Simple Feature Selection
# Keep only relevant columns for basic analysis
selected_columns = [
    'TransactionID', 'CustomerName', 'City', 'TransactionDate', 'Amount',
    'Merchant', 'Category', 'IsFraud'
]
df = df[selected_columns]

print("\nDataset information after simple cleaning and feature selection:")
print(df.info())

# 3. 💾 Save Cleaned Data
cleaned_csv_file = 'cleaned_data/cleaned_transactions.csv'
df.to_csv(cleaned_csv_file, index=False)

print(f"\nSimple cleaned dataset saved as {cleaned_csv_file}. Here are the first 5 rows:")
print(df.head())

