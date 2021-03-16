from voiceChannel import voiceChannel
import random

publicVoiceChannels = []


#create Voice Channel
async def create_voice_channel(member, name, category):   #channel info passed as own type
    channel = await member.guild.create_voice_channel(name, category = category)
    return channel

async def delete_voice_channel():
    pass


#user joined a voice channel
    #depending wich he joined call function

#public voice channel
async def public_channel(member):
    name =  f"Talk by {random.randint(1, 100)}"     #TODO: give numbers in order
    category = "General"

    channel = await create_voice_channel(member, name, category)
    public_channel.append(voiceChannel(name, channel, member))