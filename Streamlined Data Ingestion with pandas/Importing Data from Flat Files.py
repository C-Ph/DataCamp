# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv', sep = '\t')

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

#----------------------------------------------------------------------------------------------------

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

#----------------------------------------------------------------------------------------------------

# Create dataframe of next 500 rows with labeled columns
import pandas as pd

column_names = list(vt_data_first500.columns)

vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header = None,
                       		  names = column_names)

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

#----------------------------------------------------------------------------------------------------

# Create dict specifying data types for agi_stub and zipcode
data_types = {
    'agi_stub': 'category',  
    'zipcode': 'str'     
}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

#----------------------------------------------------------------------------------------------------

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

#----------------------------------------------------------------------------------------------------
'''Try to import the file `vt_tax_data_2016_corrupt.csv` without any keyword arguments.'''
try:
  # Import the CSV without any keyword arguments
  data = pd.read_csv('vt_tax_data_2016_corrupt.csv')
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

#----------------------------------------------------------------------------------------------------

'''Import `vt_tax_data_2016_corrupt.csv` with the `error_bad_lines` parameter set to skip bad records.
'''

try:
  # Import CSV with error_bad_lines set to skip bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines = False)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")


#----------------------------------------------------------------------------------------------------
'''Update the import with the `warn_bad_lines` parameter set to issue a warning whenever a bad record is skipped.'''
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines = False, 
                     warn_bad_lines = True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
