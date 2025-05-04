import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from transform import clean_data

load_dotenv()

# DB connection details
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

def load_data_to_db(df):
    df.to_sql("trending_videos", engine, if_exists="replace", index=False)
    print("✅ Data loaded into database")

if __name__ == "__main__":
    df = clean_data()
    load_data_to_db(df)
