import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION = "IN"
MAX_RESULTS = 50

def fetch_trending_videos():
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&chart=mostPopular&regionCode={REGION}&maxResults={MAX_RESULTS}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    videos = []
    for item in data.get("items", []):
        snippet = item["snippet"]
        stats = item["statistics"]
        videos.append({
            "video_id": item["id"],
            "title": snippet["title"],
            "channel_title": snippet["channelTitle"],
            "category_id": snippet["categoryId"],
            "publish_time": snippet["publishedAt"],
            "view_count": stats.get("viewCount", 0),
            "like_count": stats.get("likeCount", 0),
            "comment_count": stats.get("commentCount", 0)
        })
    return pd.DataFrame(videos)

if __name__ == "__main__":
    df = fetch_trending_videos()
    df.to_csv("trending_data.csv", index=False)
    print("✅ Trending data saved to trending_data.csv")
