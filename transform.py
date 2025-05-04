import pandas as pd

def clean_data(filename="trending_data.csv"):
    df = pd.read_csv(filename)
    df.dropna(inplace=True)
    df["view_count"] = df["view_count"].astype(int)
    df["like_count"] = df["like_count"].astype(int)
    df["comment_count"] = df["comment_count"].astype(int)
    return df
