import pandas as pd

class DataCleaning:
    def clean_user_data(self, df):
        # Remove rows where any of the columns are NULL
        df.dropna(inplace=True)

        # Convert date columns to datetime format and handle errors
        date_columns = ['date_of_birth', 'join_date']
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

        # Remove rows where date conversion failed (NaT)
        df.dropna(subset=date_columns, inplace=True)

        # Assuming 'phone_number' should be a string, remove any non-numeric characters
        df['phone_number'] = df['phone_number'].str.replace(r'\D', '', regex=True)

        return df

    
    def clean_card_data(self, df):
        # Remove rows where any of the columns are NULL
        df.dropna(inplace=True)

        # Assuming 'card_number' should be a string of 16 digits
        df['card_number'] = df['card_number'].astype(str)
        df = df[df['card_number'].str.match(r'^\d{16}$')]

        # Assuming 'expiry_date' should be in MM/YY format
        df['expiry_date'] = df['expiry_date'].astype(str)
        df = df[df['expiry_date'].str.match(r'^(0[1-9]|1[0-2])\/\d{2}$')]

        # Assuming 'cvv' should be a 3-digit number
        df['cvv'] = df['cvv'].astype(str)
        df = df[df['cvv'].str.match(r'^\d{3}$')]

        return df

    def clean_store_data(self, df):
        # Drop redundant 'index' column if it's not needed
        df.drop(columns=['index'], inplace=True, errors='ignore')

        # Drop unnecessary 'lat' column
        df.drop(columns=['lat'], inplace=True, errors='ignore')

        # Standardize text columns
        text_columns = ['address', 'locality', 'continent']
        for col in text_columns:
            df[col] = df[col].str.strip().str.title()

        # Ensure 'staff_numbers' is numeric
        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'], errors='coerce')
        df.dropna(subset=['staff_numbers'], inplace=True)

        # Convert 'opening_date' to datetime
        df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce')
        df.dropna(subset=['opening_date'], inplace=True)

        # Validate 'longitude' and 'latitude'
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df.dropna(subset=['longitude', 'latitude'], inplace=True)

        # Validate 'country_code'
        df = df[df['country_code'].str.match(r'^[A-Za-z]{2,3}$')]

        return df