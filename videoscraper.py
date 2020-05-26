import re
import videolist
from description_downloader import scrape_video_data

def getVideoList(channel_id, api_key):
    return videolist.get_all_video_in_channel(channel_id,api_key)

def getVideoDescription(video_url):
    return scrape_video_data(video_url)

def scrapeVideos(channel_id,api_key):
    links = getVideoList(channel_id,api_key)
    videos = []

    for link in links:
        response = getVideoDescription(link)

        if ('title' not in response or 'description' not in response):
            continue 

        videos.append((response['title'],response['description']))

    return videos