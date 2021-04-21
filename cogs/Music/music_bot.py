from discord.ext import commands

#Music Bot imports
from discord import FFmpegPCMAudio, client
from youtube_search_requests import YoutubeSearch
from youtube_dl import YoutubeDL



class music_bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(client.Guild)


    @commands.command()
    async def play(self, ctx, arg): #TODO: take 
        print(get_link(arg, url=True))

        voice = await join_channel(ctx.author.voice.channel)

        await play_music(voice, arg)



def setup(client):
    client.add_cog(music_bot(client))



#Music Bot methods
async def play_music(voice, name):





    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = get_link(name, url=True)
    await voice.play(FFmpegPCMAudio(executable='C:/Program Files/FFMPEG/ffmpeg.exe', source=URL, **FFMPEG_OPTIONS))





async def join_channel(channel):
    #TODO: check if user is in voice channel, if bot is already connected, ...
    return await channel.connect()
    


def Link_with_name(name):
    y = YoutubeSearch()
    
    vid = y.search_videos(name, max_results=1)[0]['url']
    print(vid)

def get_link(name, url=True):
    
    #link
    if not url:
        link = Link_with_name(name)
    else: 
        link = name         #ToDo Check validation

    dl_opts = {'format': 'bestaudio'}       #best possible audio
    with YoutubeDL(dl_opts) as ydl:
        info = ydl.extract_info(link, download=False)   #dictonary with all infos
        return info['formats'][0]['url']             #url to audio file of video

Link_with_name("hallo")