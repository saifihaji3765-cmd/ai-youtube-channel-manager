import requests

YOUTUBE_API_KEY = "PASTE_YOUTUBE_API_KEY"
YOUTUBE_BASE_URL = "https://www.googleapis.com/youtube/v3"


def search_youtube(query, max_results=5):
    url = f"{YOUTUBE_BASE_URL}/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("items", []):
        results.append({
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"]
        })

    return results


def get_video_stats(video_ids):
    url = f"{YOUTUBE_BASE_URL}/videos"
    params = {
        "part": "statistics,snippet",
        "id": ",".join(video_ids),
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    stats = []
    for item in data.get("items", []):
        stats.append({
            "video_id": item["id"],
            "title": item["snippet"]["title"],
            "views": item["statistics"].get("viewCount"),
            "likes": item["statistics"].get("likeCount"),
            "comments": item["statistics"].get("commentCount")
        })

    return stats
