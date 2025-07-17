from googleapiclient.discovery import build
import pandas as pd

API_KEY = 'YOUR_API_KEY_HERE'
YOUTUBE_API_SERVICENAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICENAME, YOUTUBE_API_VERSION, 
                developerKey='AIzaSyCDlrK7o1oPVEiCp7ItKrAwbtLqWc01IUo')


def get_video_details(query, max_results=50):
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        published_at = item['snippet']['publishedAt']

        stats_request = youtube.videos().list(
            part='statistics',
            id=video_id
        )
        stats_response = stats_request.execute()
        stats = stats_response['items'][0]['statistics']

        videos.append({
            'Video Title': title,
            'Published At': published_at,
            'Views': int(stats.get('viewCount', 0)),
            'Likes': int(stats.get('likeCount', 0)),
            'Comments': int(stats.get('commentCount', 0))
        })

    return pd.DataFrame(videos)
