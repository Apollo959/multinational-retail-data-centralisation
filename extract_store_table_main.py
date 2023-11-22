from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Classes
db_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaner = DataCleaning()

# API key
header = {'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

# Number of stores API connection details
store_number_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

# Extract and print the number of stores
number_of_stores = data_extractor.list_number_of_stores(store_number_endpoint, header)
# debug variable
# number_of_stores = 10
print(f'The number of stores is {number_of_stores}')

# Store Retrieval API Enpoint excluding number
store_details_endpoint = f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details'

# Retrieve the store data as a dataframe
store_df = data_extractor.retrieve_stores_data(store_details_endpoint, header, number_of_stores)
# print column names
print(list(store_df))

# Clean the store data
cleaned_store_data = data_cleaner.clean_store_data(store_df)
print(cleaned_store_data)

# upload to local database
db_connector.upload_to_db(cleaned_store_data, "dim_store_details")
