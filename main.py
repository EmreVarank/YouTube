from googleapiclient.discovery import build

API_KEY = ""  # Fill in the blank with your own YouTube API KEY

key_words = ("Türkiye")

# Create a YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

# Perform a search on YouTube using the keyword
response = youtube.search().list(
    q=key_words,
    part="snippet",
    type="video",
    maxResults=10,
    order="viewCount"
).execute()

# Print titles and links
print("----> Found YouTube Videos:")
for item in response["items"]:
    video_title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    print(f"- {video_title} -> {video_link}")
