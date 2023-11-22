import pandas as pd
import tabula
import requests
import boto3
from io import StringIO
from database_utils import DatabaseConnector

class DataExtractor:
    def read_rds_table(self, table_name):
        db_connector = DatabaseConnector()
        engine = db_connector.init_db_engine()
        df = pd.read_sql_table(table_name, engine)
        return df

    def retrieve_pdf_data(self, pdf_link):
        df_list = tabula.read_pdf(pdf_link, pages='all', multiple_tables=True)
        combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df


    def list_number_of_stores(self, endpoint, headers):
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            return response.json()['number_stores']
        else:
            return None

    def retrieve_stores_data(self, endpoint, headers, num_stores):
        store_data = []
        for i in range(1, num_stores + 1):
            response = requests.get(f"{endpoint}/{i}", headers=headers)
            if response.status_code == 200:
                store_data.append(response.json())
        return pd.DataFrame(store_data)

    def extract_from_s3(self, s3_address):
        s3_client = boto3.client('s3')
        s3_bucket, s3_key = s3_address.replace("s3://", "").split("/", 1)

        csv_obj = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
        body = csv_obj['Body'].read().decode('utf-8')

        return pd.read_csv(StringIO(body))
