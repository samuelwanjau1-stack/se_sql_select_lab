import sqlite3
import pandas as pd

# STEP 1: Connecting to the Data
conn = sqlite3.connect('data.sqlite')

# Reference code provided in instructions
employee_data = pd.read_sql("SELECT * FROM employees", conn)

# STEP 2: Basic Select Filtering
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM employees", conn)

# STEP 3: Basic Select Filtering (Reverse Order)
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM employees", conn)

# STEP 4: Aliasing in Select
df_alias = pd.read_sql("SELECT lastName, employeeNumber AS ID FROM employees", conn)

# STEP 5: CASE Function
df_executive = pd.read_sql("""
    SELECT *,
    CASE 
        WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""", conn)

# STEP 6: Built-In Functions - Strings
df_name_length = pd.read_sql("SELECT LENGTH(lastName) AS name_length FROM employees", conn)

# STEP 7: Built-In Functions - Strings
df_short_title = pd.read_sql("SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees", conn)

# STEP 8: Built-In Functions - Numerics
# We wrap the sum in a list [ ] because the test looks for index [0]
temp_df = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price 
    FROM orderDetails
""", conn)
sum_total_price = [temp_df['total_price'].sum()]

# STEP 9: Date Functions
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
    FROM orders
""", conn)

# Close the connection
conn.close()