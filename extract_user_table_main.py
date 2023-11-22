from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# Initialize classes
db_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaner = DataCleaning()

# PDF source link
pdf_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"

# Concatinate tables from PDF as dataframe
card_data_df = data_extractor.retrieve_pdf_data(pdf_link)

# Clean the data
#cleaned_card_data = data_cleaner.clean_card_data(card_data_df)
