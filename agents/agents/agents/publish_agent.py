import google_auth_oauthlib.flow
import googleapiclient.discovery
from settings import YOUTUBE_API_SCOPES

def upload_video(video_path, title, description):
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", YOUTUBE_API_SCOPES
    )
    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", credentials=credentials
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["AI", "business", "money"],
                "categoryId": "22"
            },
            "status": {"privacyStatus": "public"}
        },
        media_body=video_path
    )

    request.execute()
