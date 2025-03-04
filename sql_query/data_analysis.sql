-- Create a new database
CREATE DATABASE CreditCardAnalysis;


-- Use the new database
USE CreditCardAnalysis;


-- Create a table to store transaction data
DROP TABLE IF EXISTS Transactions;
CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    TransactionDate DATETIME,
    Amount DECIMAL(18, 2),
    Merchant VARCHAR(50),
    Category VARCHAR(50),
    IsFraud BIT
);
GO

-- Bulk inserting the data from the source file to csv
BULK INSERT Transactions
FROM 'D:\c_transaction\cleaned_data\cleaned_transactions.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- Summary statistics for the Amount column
SELECT 
    COUNT(*) AS TotalTransactions,
    COUNT(DISTINCT CustomerName) AS UniqueCustomers,
    AVG(Amount) AS AvgAmount,
    MIN(Amount) AS MinAmount,
    MAX(Amount) AS MaxAmount
FROM Transactions;


-- Top 5 merchants by transaction volume
SELECT TOP 5 Merchant, COUNT(*) AS TransactionCount, SUM(Amount) AS TotalAmount
FROM Transactions
GROUP BY Merchant
ORDER BY TotalAmount DESC;


-- Transactions by category
SELECT Category, COUNT(*) AS TransactionCount, SUM(Amount) AS TotalAmount
FROM Transactions
GROUP BY Category
ORDER BY TotalAmount DESC;

-- Extract hour from TransactionDate
SELECT 
    DATEPART(HOUR, TransactionDate) AS TransactionHour, 
    COUNT(*) AS TransactionCount
FROM Transactions
GROUP BY DATEPART(HOUR, TransactionDate)
ORDER BY TransactionCount DESC;

-- Fraud by merchant
SELECT Merchant, COUNT(*) AS FraudCount
FROM Transactions
WHERE IsFraud = 1
GROUP BY Merchant
ORDER BY FraudCount DESC;

-- Fraud by category
SELECT Category, COUNT(*) AS FraudCount
FROM Transactions
WHERE IsFraud = 1
GROUP BY Category
ORDER BY FraudCount DESC;


-- Average amount for fraudulent vs non-fraudulent transactions
SELECT 
    IsFraud,
    COUNT(*) AS TransactionCount,
    AVG(Amount) AS AvgAmount
FROM Transactions
GROUP BY IsFraud;

-- Total frauds per city
SELECT City, COUNT(*) AS FraudCount
FROM Transactions
WHERE IsFraud = 1
GROUP BY City
ORDER BY FraudCount DESC;

-- Average transaction per category
SELECT Category, AVG(Amount) AS AvgAmount
FROM Transactions
GROUP BY Category
ORDER BY AvgAmount DESC;







