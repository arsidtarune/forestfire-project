# 📈 YouTube Trending Data ETL Pipeline

A fully automated ETL pipeline that extracts trending YouTube video data daily using Python, and PostgreSQL.  
Data is visualized using a custom-built Streamlit dashboard.

## 🚀 Features
- Daily data extraction via YouTube Data API
- ETL pipeline: extract, transform,and load data
- PostgreSQL database storage
- Interactive dashboard with Streamlit
- Professional modular project structure

## 🛠️ Tech Stack
- Python 
- PostgreSQL
- Streamlit
- YouTube Data API
- SQLAlchemy
- Pandas


## 📂 Project Structure
/Project
│
│── trending_data.csv
├── .venv/
├── extract.py
├── transform.py
├── load.py
├── app.py
├── requirements.txt
├── README.md


## 🧠 Author
Arsid Tarune(www.linkedin.com/in/arsid-tarune-14506b2b8)

NOTE : You have to put your API key to extract data, here are the following steps to extract the API key
Following changes should be made in .env

General Steps:

    Have an Account: Most API providers require you to have an account with them before they'll allow you to generate an API key. 

Log In: Log in to your account on the API provider's website. 
Navigate to API/Credentials: Locate the section dedicated to API keys, credentials, or tokens within your account. 
Create or Generate: Follow the instructions on the page to create or generate a new API key. 
Save the Key: Once created, you'll be shown the key, which you'll need to copy and store securely, as you won't be able to view it again after closing the page.  

