import pandas as pd

'''
This set of code is intended for the formatting of the Oklahoma monthly tornado incidence dataset (1950-2023)
The following code formats the table of year x month incidence into a single column incidence (csv file)
This makes it easier to treat the data as a time series during the regression predictive code

In the code, comments with '# #' represent a line of code that has been commented out
These lines of code have no effect on the overall code but are helpful for occasional reference

'REIR' in comments stand for 'reasoning explained in report' for instances where explaining concisely is not feasible
'''

# Importing of dataset from Excel spreadsheet (original data sourced from:
# https://www.weather.gov/oun/tornadodata-ok-monthlyannual)
df = pd.read_excel('Oklahoma Tornado Incidence Data (1950-2023).xlsx')

# Formatting of dataset to exclude unwanted variables (columns + rows)
df = df[:-4]
delete_columns = ['Year', 'Ann.']
df.drop(columns=delete_columns, inplace=True)
# #print(df.head())

# Flattening of dataset from table into single column + retitling column
single_column = df.values.flatten('C')
df_sc = pd.DataFrame(single_column, columns=['Count'])
# #print(df_sc.head())

# Adding of column representing month periods
date_range = pd.date_range(start='1950-01-01', end='2023-12-31', freq='MS')
date_col = date_range.strftime('%m.%Y')
df_sc['Date'] = date_col
# #print(df.head())

# Exporting to CSV file: includes newly created column
df_sc.to_csv('Tornado Incidence 1950-2023 Formatted.csv', index=False)
