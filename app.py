import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection setup
def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# Function to load data from the database
def load_data():
    engine = get_engine()
    query = "SELECT * FROM trending_videos"
    return pd.read_sql(query, engine)

# Streamlit App UI
st.set_page_config(page_title="YouTube Trending Dashboard", layout="wide")
st.title("📈 YouTube Trending Videos Dashboard")

# Refresh button
if st.button("🔁 Refresh Data"):
    st.info("Refreshing data...")
    os.system("python extract.py")
    os.system("python load.py")
    st.success("✅ Data refreshed successfully!")

# Load and display data
try:
    df = load_data()
    st.subheader("Top Trending Videos")
    st.dataframe(df.head(10))
except Exception as e:
    st.error(f"❌ Failed to load data: {e}")
