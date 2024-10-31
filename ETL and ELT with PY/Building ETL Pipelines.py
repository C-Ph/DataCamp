import pandas as pd

# Read the sales data into a DataFrame
sales_data = pd.read_parquet("sales_data.parquet", engine="fastparquet")

# Check the data type of the columns of the DataFrames
print(sales_data.dtypes)

# Print the shape of the DataFrame, as well as the head
print(sales_data.shape)
print(sales_data.head())

#----------------------------------------------------------------------------------------------------

import sqlalchemy

# Create a connection to the sales database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")

# Query the sales table
raw_sales_data = pd.read_sql("SELECT * FROM sales", db_engine)
print(raw_sales_data)

#----------------------------------------------------------------------------------------------------

'''Use `pandas` to query the `sales` tables for all columns and records with `"quantity_ordered"` equal to 1.
'''
def extract():

    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    
    # Query the DataFrame to return all records with quantity_ordered equal to 1
    raw_sales_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)
    return raw_sales_data


'''Print the head of the DataFrame, and return the extracted data. Then, execute the `extract()` function.
'''
def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    raw_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)
    
    # Print the head of the DataFrame
    print(raw_data.head())
    
    # Return the extracted DataFrame
    return raw_data
    
# Call the extract() function
raw_sales_data = extract()

#----------------------------------------------------------------------------------------------------

# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data[raw_data["Quantity Ordered"] > 1]
    
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = clean_data[["Order Date", "Quantity Ordered", "Purchase Address"]]
    
    # Return the filtered DataFrame
    return clean_data
    
transform(raw_sales_data)

#----------------------------------------------------------------------------------------------------

raw_sales_data = extract("sales_data.csv")

def transform(raw_data):
    # Convert the "Order Date" column to type datetime
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    
    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    return clean_data

clean_sales_data = transform(raw_sales_data)

# Check the data types of each column
print(clean_sales_data.dtypes)

#----------------------------------------------------------------------------------------------------

'''Update the `extract()` function to read the **parquet** file stored in the `file_path` parameter into a DataFrame.
'''
def extract(file_path):
  	# Ingest the data to a DataFrame
    raw_data = pd.read_parquet(file_path)
    
    # Return the DataFrame
    return raw_data
  
raw_sales_data = extract("sales_data.parquet")


'''Update the `transform()` function to return the `"Order ID"`, `"Price Each"` and `"Quantity Ordered"` columns for all items with a `"Quantity Ordered"` equal to 1.
- Call the `transform()` function on the `raw_sales_data` DataFrame.'''

def extract(file_path):
    raw_data = pd.read_parquet(file_path)
    return raw_data

raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Filter rows and columns
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] == 1, ["Order ID", "Price Each", "Quantity Ordered"]]

    return clean_data

# Transform the raw_sales_data
clean_sales_data = transform(raw_sales_data)


'''What is the value of the price `"Price Each"` column of the two most expensive items in the transformed DataFrame?

The `clean_sales_data` DataFrame has been loaded for you, and you can use the console to explore it further.
'''

# Get the two most expensive items based on the "Price Each" column
most_expensive_items = clean_sales_data.nlargest(2, "Price Each")

# Extract the "Price Each" values
price_each_values = most_expensive_items["Price Each"]

print(price_each_values)


'''115    1700.0
137    1700.0
Name: Price Each, dtype: float64'''

#----------------------------------------------------------------------------------------------------

def transform(raw_data):
	# Find the items prices less than 25 dollars
	return raw_data.loc[raw_data["Price Each"] < 25, ["Order ID", "Product", "Price Each", "Order Date"]]

def load(clean_data):
	# Write the data to a CSV file without the index column
	clean_data.to_csv("transformed_sales_data.csv", index=False)


clean_sales_data = transform(raw_sales_data)

# Call the load function on the cleaned DataFrame
load(clean_sales_data)

#----------------------------------------------------------------------------------------------------

# Import the os library
import os

# Load the data to a csv file with the index, no header and pipe separated
def load(clean_data, path_to_write):
	clean_data.to_csv(path_to_write, header=False, sep="|")

load(clean_sales_data, "clean_sales_data.csv")

# Check that the file is present.
file_exists = os.path.exists("clean_sales_data.csv")
print(file_exists)

#----------------------------------------------------------------------------------------------------

def load(clean_data, file_path):
    # Write the data to a file
    clean_data.to_csv(file_path, header = False, index = False)

    # Check to make sure the file exists
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load(clean_sales_data, "transformed_sales_data.csv")

#----------------------------------------------------------------------------------------------------

def transform(raw_data):
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    
    # Create an info log regarding transformation
    logging.info("Transformed 'Order Date' column to type 'datetime'.")
    
    # Create debug-level logs for the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of the DataFrame after filtering: {clean_data.shape}")
    return clean_data
  
clean_sales_data = transform(raw_sales_data)

#----------------------------------------------------------------------------------------------------

def extract(file_path):
    return pd.read_parquet(file_path)

# Update the pipeline to include a try block
try:
	# Attempt to read in the file
    raw_sales_data = extract("sales_data.parquet")
	
# Catch the FileNotFoundError
except FileNotFoundError as file_not_found:
	# Write an error-level log
	logging.error(file_not_found)

#----------------------------------------------------------------------------------------------------
'''Create an info-level logging message to document success, and a warning-level logging message if the transformation fails.
'''
def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	# Attempt to transform DataFrame, log an info-level message
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")
	
except Exception:
	# Log a warning-level message
	logging.warning("Cannot filter DataFrame by 'Total Price'")


'''Update the `try`-`except` clause to catch a `KeyError`, and alias as `ke`.
- Change the warning-level log to include the error being thrown.'''
def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")
	
# Update the exception to be a KeyError, alias as ke
except KeyError as ke:
	# Log a warning-level message
	logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")



'''If a key error is thrown, create a column `"Total Price"` by multiplying the `"Price Each"` and `"Quantity Ordered"` columns.
'''
def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")

except KeyError as ke:
	logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")
	
	# Create the "Total Price" column, transform the updated DataFrame
	raw_sales_data["Total Price"] = raw_sales_data["Price Each"] * raw_sales_data["Quantity Ordered"]
	clean_sales_data = transform(raw_sales_data)

