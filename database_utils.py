import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector:
    def read_db_creds(self):
        with open("db_creds.yaml", 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def init_db_engine(self):
        db_creds = self.read_db_creds()
        engine = create_engine(f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}")
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        return inspector.get_table_names()

    def upload_to_db(self, df, table_name):
        local_db_user = "postgres"
        local_db_password = "password123"
        local_db_host = "localhost"
        local_db_port = "5432"
        local_db_name = "sales_data"
        local_engine = create_engine(f"postgresql://{local_db_user}:{local_db_password}@{local_db_host}:{local_db_port}/{local_db_name}")
        df.to_sql(table_name, local_engine, if_exists='replace')
