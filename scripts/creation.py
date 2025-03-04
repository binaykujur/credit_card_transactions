import pandas as pd
import random
from faker import Faker

# Initialize Faker with Indian locale
fake = Faker('en_IN')  # 'en_IN' locale generates Indian names, addresses, and phone numbers
Faker.seed(42)
random.seed(42)

# Define dataset parameters
num_records = 5000  # Number of transactions
fraud_ratio = 0.05  # 5% of transactions will be fraudulent

# Define Indian-specific merchants and categories
merchants = [
    'Amazon India', 'Flipkart', 'Big Bazaar', 'Reliance Digital', 'Myntra',
    'Zomato', 'Swiggy', 'Paytm Mall', 'Tata Cliq', 'Snapdeal'
]
categories = [
    'Groceries', 'Electronics', 'Clothing', 'Transport', 'Entertainment',
    'Food & Dining', 'Health & Wellness', 'Travel', 'Utilities', 'Recharge & Bills'
]

# Helper functions
def generate_card_number():
    return fake.credit_card_number(card_type='visa')

def generate_transaction_date():
    return fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')

def generate_amount():
    return round(random.uniform(100.0, 50000.0), 2)  # INR range for transactions

def generate_merchant_and_category():
    merchant = random.choice(merchants)
    category = random.choice(categories)
    return merchant, category

def is_fraud():
    return 1 if random.random() < fraud_ratio else 0

# Generate dataset
data = []
for i in range(1, num_records + 1):
    card_number = generate_card_number()
    transaction_date = generate_transaction_date()
    amount = generate_amount()
    merchant, category = generate_merchant_and_category()
    fraud = is_fraud()

    # Generate Indian-specific information
    name = fake.name()
    phone_number = fake.phone_number()
    city = fake.city()

    data.append([
        i,  # Transaction ID
        name,
        phone_number,
        city,
        card_number,
        transaction_date,
        amount,
        merchant,
        category,
        fraud
    ])

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    'TransactionID', 'CustomerName', 'PhoneNumber', 'City', 'CardNumber',
    'TransactionDate', 'Amount', 'Merchant', 'Category', 'IsFraud'
])

# Save to CSV
csv_file = 'raw_data/indian_credit_card_transactions.csv'
df.to_csv(csv_file, index=False)

print(f"Synthetic dataset generated and saved as {csv_file}. Here are the first 5 rows:")
print(df.head())
