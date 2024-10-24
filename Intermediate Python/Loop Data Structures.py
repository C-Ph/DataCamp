# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

# Iterate over europe
for i, j in europe.items():
    print("the capital of " + i + " is " + j) #europe is string


#----------------------------------------------------------------------------------------------

# Import numpy as np
import numpy as np

# For loop over np_height
for i in np_height:
    print( str(i) + " inches")

'''print(np_baseball)
[[ 74 180]
 [ 74 215]
 [ 72 210]
 ...
 [ 75 205]
 [ 75 190]
 [ 73 195]]'''
 
# For loop over np_baseball
for j in np.nditer(np_baseball):
    print(str(j))

#----------------------------------------------------------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Iterate over rows of cars
for i, j in cars.iterrows():
    print(i)
    print(j)
    
'''US
cars_per_cap              809
country         United States
drives_right             True
Name: US, dtype: object

AUS
cars_per_cap          731
country         Australia
drives_right        False
Name: AUS, dtype: object

JPN
cars_per_cap      588
country         Japan
drives_right    False
Name: JPN, dtype: object

IN
cars_per_cap       18
country         India
drives_right    False
Name: IN, dtype: object

RU
cars_per_cap       200
country         Russia
drives_right      True
Name: RU, dtype: object

MOR
cars_per_cap         70
country         Morocco
drives_right       True
Name: MOR, dtype: object

EG
cars_per_cap       45
country         Egypt
drives_right     True
Name: EG, dtype: object'''

#----------------------------------------------------------------------------------------------

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

'''US: 809
AUS: 731
JPN: 588
IN: 18
RU: 200
MOR: 70
EG: 45'''

#----------------------------------------------------------------------------------------------
'''- Use a `for` loop to add a new column, named `COUNTRY`, that contains a uppercase version of the country names in the
 `"country"` column. You can use the string method `upper()` for this.
- To see if your code worked, print out `cars`. Don't indent this code, so that it's not part of the `for` loop.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

'''<script.py> output:

         cars_per_cap        country  drives_right        COUNTRY
    US            809  United States          True  UNITED STATES
    AUS           731      Australia         False      AUSTRALIA
    JPN           588          Japan         False          JAPAN
    IN             18          India         False          INDIA
    RU            200         Russia          True         RUSSIA
    MOR            70        Morocco          True        MOROCCO
    EG             45          Egypt          True          EGYPT'''

#----------------------------------------------------------------------------------------------
'''Replace the `for` loop with a one-liner that uses `.apply(str.upper)`. The call should give the same result: 
a column `COUNTRY` should be added to `cars`, containing an uppercase version of the country names.
- As usual, print out `cars` to see the fruits of your hard labor'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

'''<script.py> output:

         cars_per_cap        country  drives_right        COUNTRY
    US            809  United States          True  UNITED STATES
    AUS           731      Australia         False      AUSTRALIA
    JPN           588          Japan         False          JAPAN
    IN             18          India         False          INDIA
    RU            200         Russia          True         RUSSIA
    MOR            70        Morocco          True        MOROCCO
    EG             45          Egypt          True          EGYPT'''

