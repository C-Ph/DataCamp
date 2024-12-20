# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# View the tables in the database
print(engine.table_names())

#----------------------------------------------------------------------------------------------------

'''Use `read_sql()` to load the `hpd311calls` table by name, without any SQL.'''
# Load libraries
import pandas as pd
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///data.db')

# Load hpd311calls without any SQL
hpd_calls = pd.read_sql('hpd311calls', engine)


# View the first few rows of data
print(hpd_calls.head())



'''Use `read_sql()` and a `SELECT * ...` SQL query to load the entire `weather` table.'''

# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM weather;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())


#----------------------------------------------------------------------------------------------------
'''Create a database engine for `data.db`.
- Write a SQL query that `SELECT`s the `date`, `tmax`, and `tmin` columns from the `weather` table.
- Make a dataframe by passing the query and engine to `read_sql()` and assign the resulting dataframe to `temperatures`.'''

# Create database engine for data.db
engine = create_engine('sqlite:///data.db')

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Make a dataframe by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

# View the resulting dataframe
print(temperatures)

#----------------------------------------------------------------------------------------------------

# Create query to get hpd311calls records about safety
query = """
select *
from hpd311calls
where complaint_type = 'SAFETY';
"""

# Query the database and assign result to safety_calls
safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

#----------------------------------------------------------------------------------------------------

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  Where tmax <= 32
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query, engine)

# View summary stats about the temperatures
print(wintry_days.describe())

#----------------------------------------------------------------------------------------------------

# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  From hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)


#----------------------------------------------------------------------------------------------------

# Create query to get call counts by complaint_type
query = """
select complaint_type, 
     count(*)
  FROM hpd311calls
  group by complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()

#----------------------------------------------------------------------------------------------------

'''Create a query to pass to `read_sql()` that will get months and the `MAX` value of `tmax` by `month`from `weather`.'''

# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
  GROUP BY month;"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)



'''Modify the query to also get the `MIN` `tmin` value for each `month`.'''

# Create a query to get month, max tmax, and min tmin by month
query = """
SELECT month, 
	MAX(tmax), 
    MIN(tmin)
  FROM weather 
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)



'''- Modify the query to also get the total precipitation (`prcp`) for each `month`.'''

# Create query to get temperature and precipitation by month
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        sum(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

#----------------------------------------------------------------------------------------------------

import pandas as pd

# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather.head())



'''Complete `query` to get the `prcp` column in `weather` and join `weather` to `hpd311calls` on their `date` and `created_date` columns, respectively.
- Use `read_sql()` to load the results of the query into the `leak_calls` dataframe.'''

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN  weather
  ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())



'''Modify `query` to get only rows that have `'WATER LEAK'` as their `complaint_type'''

# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())



'''Complete the query to get `created_date` and counts of records whose `complaint_type` is `HEAT/HOT WATER` from `hpd311calls` by date.
- Create a dataframe,`df`, containing the results of the query.'''

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
  GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df =  pd.read_sql(query, engine)

# View first 5 records
print(df.head())



'''Modify the query to join `tmax` and `tmin` from the `weather` table. (There is only one record per date in `weather`, so we do not need SQL's `MAX` and `MIN` functions here.) Join the tables on `created_date` in `hpd311calls` and `date` in `weather`.'''

# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())



