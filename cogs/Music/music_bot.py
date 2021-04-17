import discord
from discord.ext import commands

#Music Bot imports
from os import link
from youtube_search_requests import YoutubeSearch
from youtube_dl import YoutubeDL



class music_bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def join(self, ctx):
        #TODO: check if user is in voice channel, if bot is already connected, ...
        pass
        

    @commands.command()
    async def play(self, ctx, arg):
        pass



def setup(client):
    client.add_cog(music_bot(client))



#Music Bot methods
async def join_channel(channel):
    pass



def Link_with_name(name):
    y = YoutubeSearch()
    return y.search_videos(name, max_results=1)[0]['url']


def get_link(name, url=True):
    
    #link
    if not url:
        link = Link_with_name(name)
    else: 
        link = name         #ToDo Check validation

    link = 'https://www.youtube.com/watch?v=9iHM6X6uUH8'
    dl_opts = {'format': 'bestaudio'}       #best possible audio
    with YoutubeDL(dl_opts) as ydl:
        info = ydl.extract_info(link, download=False)   #dictonary with all infos
        return info['formats'][0]['url']                 #url to audio file of video