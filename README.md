# Multinational Retail Data Centralisation Project

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
   - [Objective](#objective)
   - [Technologies Used](#technologies-used)
3. [Module Overview](#module-overview)
   - [Database Connector (database_utils.py)](#database-connector-database_utilspy)
     - [DatabaseConnector.read_db_creds()](#databaseconnectorread_db_creds)
     - [DatabaseConnector.init_db_engine()](#databaseconnectorinit_db_engine)
     - [DatabaseConnector.list_db_tables()](#databaseconnectorlist_db_tables)
     - [DatabaseConnector.upload_to_db(df, table_name)](#databaseconnectorupload_to_dbdf-table_name)
   - [Data Extraction Module (data_extraction.py)](#data-extraction-module-data_extractionpy)
     - [DataExtractor.read_rds_table(table_name)](#dataextractorread_rds_tabletable_name)
     - [DataExtractor.retrieve_pdf_data(pdf_link)](#dataextractorretrieve_pdf_datapdf_link)
     - [DataExtractor.list_number_of_stores(endpoint, headers)](#dataextractorlist_number_of_storesendpoint-headers)
     - [DataExtractor.retrieve_stores_data(endpoint, headers, num_stores)](#dataextractorretrieve_stores_dataendpoint-headers-num_stores)
     - [DataExtractor.extract_from_s3(s3_address)](#dataextractorextract_from_s3s3_address)
   - [Data Cleaning (data_cleaning.py)](#data-cleaning-data_cleaningpy)
     - [DataCleaning.clean_user_data(df)](#datacleaningclean_user_datadf)
     - [DataCleaning.clean_store_data(df)](#datacleaningclean_store_datadf)
     - [DataCleaning.clean_card_data(df)](#datacleaningclean_card_datadf)


## Introduction
This project focuses on centralising data for a multinational retail company. It involves extracting, cleaning, and storing data from various sources like databases, APIs, and cloud storage.

## Project Overview

### Objective
The primary goal is to streamline data handling processes.

### Technologies Used
- Python
- PostgreSQL
- AWS (RDS, S3)
- Pandas
- SQLAlchemy

## Module Overview

### Database Connector (database_utils.py)
This module serves as the utility for database connections, such as reading credentials, establishing connections, listing tables, and uploading cleaned data into the database.

#### DatabaseConnector.read_db_creds()
This method reads database credentials from a configuration file.

#### DatabaseConnector.init_db_engine()
init_db_engine initializes a connection engine to the database. This method relies on the credentials obtained from read_db_creds(). It uses these credentials to create and return an SQLAlchemy engine object, which is used for connecting to the database.

#### DatabaseConnector.list_db_tables()
This method lists all the tables present in the connected database.

#### DatabaseConnector.upload_to_db(df, table_name)
upload_to_db uploads a pandas DataFrame to a specified table in the database. It takes two parameters: df, the pandas DataFrame to upload, and table_name, the name of the table in the database. The method uses SQLAlchemy to upload the DataFrame to the table, handling data types and potential conflicts like existing tables.

### Data Extraction Module (data_extraction.py)
The Data Extraction module is responsible for retrieving data from various sources. It includes methods for connecting to APIs, reading from AWS S3 buckets, and extracting data from AWS RDS.

#### DataExtractor.read_rds_table(table_name)
This method is designed to extract data from a specified table in an AWS RDS database.
The table_name parameter requires the name of the table to be extracted. The method assumes that a database connection is already established to execute a query and retrieve data from the specified table.

#### DataExtractor.retrieve_pdf_data(pdf_link)
The retrieve_pdf_data method extracts data from a PDF document located at a given URL.
It requires the pdf_link parameter, which is the URL to the PDF file. The method uses a PDF parsing library (like tabula-py) to read and convert the content of the PDF into a structured format, typically a pandas DataFrame.

#### DataExtractor.list_number_of_stores(endpoint, headers)
This method fetches the total number of retail stores from an API.
It takes two parameters: endpoint, the URL of the API providing the store count, and headers, which includes any required headers for the API request, such as authentication tokens or API keys.

#### DataExtractor.retrieve_stores_data(endpoint, headers, num_stores)
retrieve_stores_data is used to extract detailed information about each store from an API.
This method requires the endpoint for the API call, headers for any necessary request headers, and num_stores, which is the total number of stores to retrieve. It iteratively calls the API for each store and aggregates the data.

#### DataExtractor.extract_from_s3(s3_address)
This method downloads and extracts data from a file stored in an AWS S3 bucket.
The s3_address parameter is needed, which is the path to the file in the S3 bucket. The method uses the boto3 library to access the S3 bucket and retrieve the file, which is then read into a pandas DataFrame.


### Data Cleaning (data_cleaning.py)
This module is for standardizing data across various datasets, ensuring accuracy and consistency. This involves handling null values, correcting data formats, and validating data for user, store, and card-related data.

#### DataCleaning.clean_user_data(df)
This method is responsible for cleaning and preprocessing user-related data. It requires a pandas DataFrame (df) containing user data. The method removes rows with null values, converting date columns to a consistent format, validating data types for each column, and removing incorrect data.

#### DataCleaning.clean_store_data(df)
This method is responsible for cleaning data related to retail store locations. It requires a pandas DataFrame (df) containing store data. It standardizes text fields like addresses, numeric fields, and converting date columns to a consistent format.

#### DataCleaning.clean_card_data(df)
The clean_card_data method is tailored for cleaning data related to card transactions or details. It requires a DataFrame (df) with card-related data. The cleaning process involves removing rows with missing values, ensuring formatting consistency for card numbers and expiration dates, anonymizing sensitive data if necessary.