# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())

#----------------------------------------------------------------------------------------------------

try:
    # Load the JSON without keyword arguments
    df = pd.read_json('dhs_report_reformatted.json')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

#----------------------------------------------------------------------------------------------------

try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient = 'split')
    
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
    
except ValueError:
    print("pandas could not parse the JSON.")

#----------------------------------------------------------------------------------------------------

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)

#----------------------------------------------------------------------------------------------------

# Create dictionary to query API for cafes in NYC

parameters = {'term' : "cafe",
          	  'location' : "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                headers = headers,
                params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())

#----------------------------------------------------------------------------------------------------

# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url, 
                headers=headers,
                params=params)


# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data['businesses'])
print(cafes.name)

#----------------------------------------------------------------------------------------------------

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep = '_')

# View data
print(cafes.head())

#----------------------------------------------------------------------------------------------------

# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates', 'latitude'], 
                          		  ['coordinates', 'longitude']],
                    		meta_prefix= 'biz_')


# View the data
print(flat_cafes.head())

#----------------------------------------------------------------------------------------------------

# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset" : 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Concatenate the results, setting ignore_index to renumber rows
cafes = pd.concat([top_50_cafes, next_50_cafes], ignore_index=True)

# Print shape of cafes
print(cafes.shape)

#----------------------------------------------------------------------------------------------------

# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk, left_on='location_zip_code', right_on='zipcode')

# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data, on='puma')

# View the data
print(cafes_with_pop.head())
