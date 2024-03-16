import pandas as pd

# Read the CSV file with semicolon delimiter, skipping the first row (header)
df = pd.read_csv('water_data.csv', delimiter=';', skiprows=[0], names=['user.key', 'datetime', 'meter.reading', 'diff'])

print(df)
# TODO: Iterate through each row and convert 'datetime' column to datetime format
df['datetime'] = pd.to_datetime(df['datetime'], format="mixed")
	
# Set 'datetime' column as the index
df.set_index('datetime', inplace=True)

# Print the first few rows of the DataFrame to verify the changes
print("DataFrame after converting 'datetime' column to datetime format:")
print(df.head())

# Resample data into 5-minute intervals and sum the values
df_aggregated = df.resample('5T').sum()

# Reset index to make 'datetime' column a column again
df_aggregated.reset_index(inplace=True)

# Print the first few rows of the aggregated DataFrame
print("Aggregated DataFrame:")
print(df_aggregated.head())

# Write aggregated data to a new CSV file
df_aggregated.to_csv('output_aggregated_5min.csv', index=False)
print("Aggregated data saved to 'output_aggregated_5min.csv'")
