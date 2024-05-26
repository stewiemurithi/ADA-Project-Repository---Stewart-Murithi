import pandas as pd

"""
The following lines of code are designed to sort the dataset of Oklahoma's tornadoes (1950-2023)
The dataset (as formatted in the Excel spreadsheet) had to be synthesised manually from the source website

In the code, comments with '# #' represent a line of code that has been commented out
These lines of code have no effect on the overall code but are helpful for occasional reference

'REIR' in comments stand for 'reasoning explained in report' for instances where explaining concisely is not feasible 
"""


def filter_data_month_year_ranges(df, start_month, end_month, start_year, end_year, filename):
    # Function to divide dataset according to determined month and year ranges
    # Filtering of dataset according to month and year ranges (reasoning explained in full report (REIR))
    # Debug: Print the types of df and Date column
    print(f"Type of df: {type(df)}")
    print(f"Type of df['Date']: {df['Date'].dtype}")
    # Filter the DataFrame based on the month and year ranges
    filtered_df = df[(df['Date'].dt.month >= start_month) & (df['Date'].dt.month <= end_month) &
                     (df['Date'].dt.year >= start_year) & (df['Date'].dt.year <= end_year)]
    # Debug: Ensure filtered_df is a DataFrame
    print(f"Type of filtered_df: {type(filtered_df)}")

    # Save the filtered DataFrame to a CSV file
    filtered_df.to_csv(filename, index=False)
    print(f"Saved {filename}")


# Excel dataset includes tornado data on Oklahoma state from 1950 to 2023
# Importing unedited file as Excel spreadsheet
OKLAsetEx = 'Oklahoma 1950-2023.xlsx'
df = pd.read_excel(OKLAsetEx)

# Deleting unneeded columns
delete_columns = ['Time (CST)', 'Length of Path (miles)', 'Width of Path (yards)', 'Killed', 'Injured', 'Location']
df.drop(columns=delete_columns, inplace=True)

# Replacing 'F?' and 'EF?' in 'F-Scale' column
df['F-Scale'] = df['F-Scale'].replace({'F?': 'Unrated1', 'EF?': 'Unrated2'})

# 'Date' column formatting + defining the month and year ranges
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
save_full = df.to_excel('1950-2023 A.xlsx')

# Month and year ranges
month_ranges = [
    (1, 3, 'Jan-Mar'),
    (4, 6, 'Apr-Jun'),
    (7, 12, 'Jul-Dec')
]

year_ranges = [
    (1950, 2006, '1950-2006'),
    (2007, 2023, '2007-2023')
]

# Iterating over the months and years
for start_month, end_month, month_label in month_ranges:
    for start_year, end_year, year_label in year_ranges:
        filename = f'{month_label}-{year_label}.csv'
        filter_data_month_year_ranges(df, start_month, end_month, start_year, end_year, filename)


def calculate_percentage_occurrences(filename, scale_values):
    # Read the CSV file into a DataFrame
    df_p = pd.read_csv(filename)

    # Calculate the percentage occurrence of each scale value
    total_count = len(df_p)
    percentages = {}
    for value in scale_values:
        count = len(df_p[df_p['F-Scale'] == value])
        percentage = (count / total_count) * 100
        percentages[value] = percentage

    return percentages


def main():
    # Defining the files and corresponding scale values
    files_scales = {
        'Jan-Mar-1950-2006.csv': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'Unrated1'],
        'Apr-Jun-1950-2006.csv': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'Unrated1'],
        'Jul-Dec-1950-2006.csv': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'Unrated1'],
        'Jan-Mar-2007-2023.csv': ['EF0', 'EF1', 'EF2', 'EF3', 'EF4', 'EF5', 'Unrated2'],
        'Apr-Jun-2007-2023.csv': ['EF0', 'EF1', 'EF2', 'EF3', 'EF4', 'EF5', 'Unrated2'],
        'Jul-Dec-2007-2023.csv': ['EF0', 'EF1', 'EF2', 'EF3', 'EF4', 'EF5', 'Unrated2']
    }

    # Initializing dataframe to store results
    results_df = pd.DataFrame()

    # Processing each file and calculating the percentages
    for filename, scale_values in files_scales.items():
        percentages = calculate_percentage_occurrences(filename, scale_values)
        # Adding the percentages to the results dataframe
        results_df = results_df._append(pd.Series(percentages, name=filename))

    # Saving the results to a CSV file
    results_df.to_csv('F-Scale_Percentages.csv')


# Running the main function
if __name__ == "__main__":
    main()


# Confirmation code
print("Code executed")
