from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL


async def music_bot_control(message, member, client):

    command = message.content
    
    if command.startswith("-play"):
        if member.voice:
            if member.voice.channel: 
                await join_channel(member.voice.channel)
                await play_music(client.voice_clients[0])


async def join_channel(channel):
    if channel is not None:
        await channel.connect()

    

async def play_music(voice_client):
    link = 'https://www.youtube.com/watch?v=SKpYiIn_icU'

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(link, download = False)	
            URL = info['formats'][0]['url']
            voice_client.play(FFmpegPCMAudio(executable='C:/Program Files/FFMPEG/ffmpeg.exe',source=URL, **FFMPEG_OPTIONS))
            voice_client.is_playing()
    else:
        print("is already playing")
        return

