from os import link
from youtube_search_requests import YoutubeSearch
from youtube_dl import YoutubeDL


def link_by_name(name):
    y = YoutubeSearch()
    return y.search_videos(name, max_results=1)[0]['url']

    #print(videos[0]['url'])




def get_link(name, url=True):



    link = 'https://www.youtube.com/watch?v=9iHM6X6uUH8'
    dl_opts = {'format': 'bestaudio'}       #best possible audio
    with YoutubeDL(dl_opts) as ydl:
        info = ydl.extract_info(link, download=False)   #dic with all infos
        Url = info['formats'][0]['url']                 #url to audio file of video


