from voiceChannel import voiceChannel
from methods import get_category_by_name
import random

publicVoiceChannels = []
privateVoiceChannels = []


#create Voice Channel
async def create_voice_channel(member, name, category):
    channel = await member.guild.create_voice_channel(name, category=category)
    return channel

async def delete_voice_channel(channelList):
    for i, e in enumerate(channelList):
        if not e.channel.members:   #voice channel is empty
            del publicVoiceChannels[i]
            await e.channel.delete()


async def admin_channels(member, after):

    #create voice channels  
    if after.channel is not None:

        if after.channel.name == "New Talk":
            await public_channel(member)
            
    
        if after.channel.name == "New private Talk":
            pass

    #delete voice channels
    await delete_voice_channel(publicVoiceChannels)





#public voice channel
async def public_channel(member):

    name =  f"Talk by {member.name}"     #TODO: give numbers in order
    category = get_category_by_name(member.guild, "Public")

    channel = await create_voice_channel(member, name, category)
    await member.move_to(channel)

    publicVoiceChannels.append(voiceChannel(name, member, channel))


#private voice channel
async def private_channel(member):

    name = f"Private Talk {random.randint(1, 100)}"
    category = get_category_by_name(member.guild, "Private")

    channel = await create_voice_channel(member, name, category)
    await member.move_to(channel)

    privateVoiceChannels.append(voiceChannel(name, member, channel))