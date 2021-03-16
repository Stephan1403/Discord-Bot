from voiceChannel import voiceChannel
import random

publicVoiceChannels = []


#create Voice Channel
async def create_voice_channel(member, name, category_name):
    channel = await member.guild.create_voice_channel(name, category_name = category_name)
    return channel

async def delete_voice_channel(channelList):
    for i, e in enumerate(channelList):
        if not e.channel.members:   #voice channel is empty
            del publicVoiceChannels[i]
            await e.channel.delete()


#user joined a voice channel
    #depending wich he joined call function
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

    name =  f"Talk {random.randint(1, 100)}"     #TODO: give numbers in order
    category_name = "GENERAL"

    channel = await create_voice_channel(member, name, category_name)
    await member.move_to(channel)

    publicVoiceChannels.append(voiceChannel(name, member, channel))

    