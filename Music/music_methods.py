from youtube_search_requests import YoutubeSearch


def link_by_name(name):
    y = YoutubeSearch()
    return y.search_videos(name, max_results=1)[0]['url']

    #print(videos[0]['url'])