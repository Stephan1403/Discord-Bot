from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import youtube_dl






async def music_bot_control(message, member, client):
    pass


async def join_channel():
    pass




#     bot_connection = member.guild.voice_client

#     command = message.content
    
#     if command.startswith("-play"):
#         if member.voice:
#             if member.voice.channel: 
#                 if bot_connection:
#                     if bot_connection.channel != member.voice.channel:
#                         await bot_connection.move_to(member.voice.channel)
#                 elif not bot_connection:
#                     await join_channel(member.voice.channel)

#                 await play_music(client.voice_clients[0], 'https://www.youtube.com/watch?v=vGrfFzagzHs')


# async def join_channel(channel):
#     if channel is not None:
#         await channel.connect()

    

# async def play_music(voice_client, link):

#     YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
#     FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
#     if not voice_client.is_playing():
#         with YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(link, download = False)	
#             # URL = info['formats'][0]['url']
#             # voice_client.play(FFmpegPCMAudio(executable='C:/Program Files/FFMPEG/ffmpeg.exe',source=URL, **FFMPEG_OPTIONS))
#             # voice_client.is_playing()
#     else:
#         print("is already playing")
#         #add to queue 
#         return



#remake

#conect bot

#get music

video_link = 'https://www.youtube.com/watch?v=mz5QjHX3pPs'

dl_opts = {'format': 'bestaudio'}
with YoutubeDL(dl_opts) as ydl:
    info = ydl.extract_info(video_link, download=False)
    print(info)
    Url = info['formats'][0]['url']
    print(Url)