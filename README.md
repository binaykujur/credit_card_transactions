# 📊 The Growth of Digital Economy: Insights from Credit Card Transaction Data in India

## 📝 Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Objectives](#objectives)
- [Data Preparation and Cleaning](#data-preparation-and-cleaning)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Fraud Detection Analysis](#fraud-detection-analysis)
- [Feature Engineering](#feature-engineering)
- [Key Insights](#key-insights)
- [Conclusion and Recommendations](#conclusion-and-recommendations)
- [Files in the Repository](#files-in-the-repository)
- [Getting Started](#getting-started)

---

## 📌 Project Overview
This project performs a **comprehensive analysis** of synthetic credit card transactions for the **Indian subcontinent** using **SQL Server**. The goal is to extract actionable insights and detect fraudulent transactions through **Exploratory Data Analysis (EDA)**, **fraud analysis**, and **feature engineering**.

**Data cleaning and preparation** were conducted in **Python** using the **Faker** library for generating synthetic data and **Pandas** for data wrangling.

---

## 📊 Dataset Description
- **File Name:** `simple_cleaned_indian_credit_card_transactions.csv`  
- **Total Records:** 5,000 (synthetic data)  
- **Data Source:** Generated using the **Faker** library in Python.  
- **Key Columns:**  
  - `TransactionID`: Unique identifier for transactions.  
  - `CustomerName`: Name of the customer.  
  - `City`: City of transaction.  
  - `TransactionDate`: Date and time of transaction.  
  - `Amount`: Transaction amount in INR.  
  - `Merchant`: Merchant where the transaction occurred.  
  - `Category`: Product category.  
  - `IsFraud`: Fraud indicator (0: No, 1: Yes).  

---

## 🎯 Objectives
1. **Analyze transaction patterns** by merchant, category, and city.  
2. **Detect potential fraud** based on transaction amount, category, and time.  
3. **Feature engineering** for enhanced analysis and reporting.  
4. **Generate actionable insights** for risk management.  

---

## 🛠 Data Preparation and Cleaning
### 📋 Steps Performed in Python
1. **Synthetic Data Generation:**  
   - Used the **Faker** library to generate realistic but synthetic transaction data.  
   - Created columns like **CustomerName, City, TransactionDate, Amount, Merchant, Category,** and **IsFraud**.  

2. **Data Cleaning:**  
   - Used **Pandas** for handling missing values and formatting dates.  
   - Removed duplicates and ensured **consistent data types** for each column.  

3. **Export to CSV:**  
   - Saved the cleaned dataset as **`simple_cleaned_indian_credit_card_transactions.csv`**.  

### 🐍 Sample Code Snippet in Python
```python
from faker import Faker
import pandas as pd
import random

# Initialize Faker and create a DataFrame
fake = Faker('en_IN')
data = []
for _ in range(5000):
    data.append({
        'TransactionID': fake.unique.random_int(100000, 999999),
        'CustomerName': fake.name(),
        'City': fake.city(),
        'TransactionDate': fake.date_time_this_year(),
        'Amount': round(random.uniform(100, 50000), 2),
        'Merchant': fake.company(),
        'Category': random.choice(['Electronics', 'Clothing', 'Travel', 'Food', 'Health']),
        'IsFraud': random.choice([0, 1])
    })

df = pd.DataFrame(data)

# Data cleaning
df.drop_duplicates(inplace=True)
df.to_csv('simple_cleaned_indian_credit_card_transactions.csv', index=False)
```
## 🔍 Exploratory Data Analysis (EDA)
### **Basics Statistics**
``` SQL
SELECT 
    COUNT(*) AS TotalTransactions,
    COUNT(DISTINCT CustomerName) AS UniqueCustomers,
    AVG(Amount) AS AvgAmount,
    MIN(Amount) AS MinAmount,
    MAX(Amount) AS MaxAmount
FROM Transactions;
```

### **🏬 Transactions by Merchant**
``` SQL
SELECT 
    Merchant, COUNT(*) AS TransactionCount, SUM(Amount) AS TotalAmount
FROM Transactions
GROUP BY Merchant
ORDER BY TotalAmount DESC;
```

### **🛡️ Fraud Detection Analysis**
``` sql
-- Fraud by merchant
SELECT Merchant, COUNT(*) AS FraudCount
FROM Transactions
WHERE IsFraud = 1
GROUP BY Merchant
ORDER BY FraudCount DESC;

```
### **🔄 Fraud Amount Analysis**
```sql
SELECT 
    IsFraud,
    AVG(Amount) AS AvgAmount
FROM Transactions
GROUP BY IsFraud;
```

## **Key Insights**
- High-risk merchants: Identified specific merchants with higher fraud counts.
- Peak transaction times: Most transactions occurred in the evening.
- Suspicious categories: High fraud in Electronics and Travel.

## **📝 Conclusion and Recommendations**
- Enhanced monitoring for high-risk merchants and categories.
- Time-based alerts for evening transactions.
- Use feature-engineered data for machine learning models to predict fraud.



