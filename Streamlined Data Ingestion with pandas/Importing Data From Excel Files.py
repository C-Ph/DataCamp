# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')

# View the head of the dataframe
print(survey_responses.head())

#----------------------------------------------------------------------------------------------------

# Create string of lettered columns to load
col_string = 'AD, AW, BA'

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows = 2, 
                        usecols = 'AD, AW:BA')

# View the names of the columns selected
print(survey_responses.columns)

#----------------------------------------------------------------------------------------------------
'''Create a dataframe from the second workbook sheet by passing the sheet's position to `sheet_name`.'''
# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = 1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

'''Create a dataframe from the `2017` sheet by providing the sheet's name to `read_excel()`.'''

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = '2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

#----------------------------------------------------------------------------------------------------
'''Load both the `2016` and `2017` sheets by name with a list and one call to `read_excel()`.'''
# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = ['2016', '2017'])

# View the data type of all_survey_data
print(type(all_survey_data))

'''Load the `2016` sheet by its position (`0`) and `2017` by name. Note the sheet names in the result.'''
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = [0, '2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())

'''Load all sheets in the Excel file without listing them all.'''
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name = None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())

#----------------------------------------------------------------------------------------------------

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

#----------------------------------------------------------------------------------------------------

# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

'''Set `read_excel()`'s `dtype` argument to load the `HasDebt` column as Boolean data.
- Supply the Boolean column name to the print statement to view financial burdens by group.'''

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype = {'HasDebt' : bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

#----------------------------------------------------------------------------------------------------

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values = ['Yes'],
                              false_values = ['No'])

# View the data
print(survey_subset.head())

#----------------------------------------------------------------------------------------------------

# Load file, with Part1StartTime parsed as datetime data
date_cols = ['Part1StartTime'] 

survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=date_cols)

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())


'''<script.py> output:
    0   2016-03-29 21:23:13
    1   2016-03-29 21:24:59
    2   2016-03-29 21:25:37
    3   2016-03-29 21:21:37
    4   2016-03-29 21:26:22
    Name: Part1StartTime, dtype: datetime64[ns]'''

#----------------------------------------------------------------------------------------------------

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ['Part2StartDate', 'Part2StartTime']}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

'''<script.py> output:
    count                    1000
    unique                    985
    top       2016-03-30 07:27:25
    freq                        2
    first     2016-03-29 21:24:57
    last      2016-03-30 09:08:18
    Name: Part2Start, dtype: object'''


#----------------------------------------------------------------------------------------------------
'''Parse `Part2EndTime` using `pd.to_datetime()`, the `format` keyword argument, and the format string you just identified. Assign the result back to the `Part2EndTime` column.'''
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], format='%m%d%Y %H:%M:%S')

''' time data '03292016 21:27:25'''

'''- Print the head of `Part2EndTime` to confirm the column now contains datetime values.'''
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], format="%m%d%Y %H:%M:%S")

# Print first few values of Part2EndTime
print(survey_data.Part2EndTime.head())


