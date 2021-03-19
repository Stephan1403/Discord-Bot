from discord import Embed, Colour
import random


from voiceChannel import voiceChannel
from methods import get_category_by_name, isInt

publicVoiceChannels = []
privateVoiceChannels = []


#create Voice Channel
async def create_voice_channel(member, name, category):
    channel = await member.guild.create_voice_channel(name, category=category)
    return channel

#delete Voice Channel
async def delete_voice_channel(channelList):
    for i, e in enumerate(channelList):
        if not e.channel.members:   #voice channel is empty
            del channelList[i]
            await e.channel.delete()

#create Text channel
async def create_text_channel(member, name, category):
    channel = await member.guild.create_text_channel(name, category=category)
    return channel



async def admin_channels(member, after):

    #create voice channels  
    if after.channel is not None:

        if after.channel.name == "New Talk":
            await public_channel(member)
            
        if after.channel.name == "New private Talk":
            await private_channel(member)

    #delete voice channels
    await delete_voice_channel(publicVoiceChannels)
    await delete_voice_channel(privateVoiceChannels)





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




# ------Edit voice_channel commands------


def editable_Channel(member):
    channel = None
    for i in privateVoiceChannels:
        if i.user == member and member.voice.channel is not None:
            if i.channel == member.voice.channel:
                channel = i.channel
    return channel


async def voice_channel_commands(message, member):
    if message.content.startswith(".info"):
        await voice_channel_info(message)

    if editable_Channel(member):       #user is in channel, allowance to edit
        channel = editable_Channel(member)

        command = message.content.lower().replace(" ", "")
        if command.startswith("."):
            if command.startswith(".name="):
                await edit_name(message, channel)
            if command.startswith(".userlimit="):
                await edit_user_limit(message, channel)
            if command.startswith(".close"):
                pass
            if command.startswith(".open"):
                pass 



#1 info - Embed
async def voice_channel_info(message):
    embed = Embed(
        title="Voice channel commands", 
        colour = Colour.orange(),
        discription = 'The following commands are only available for private voice channels')

    embed.set_author(name="Discord Bot")
    embed.add_field(name="Voice channel info", value="```\n.info\n```", inline=False)
    embed.add_field(name='Name of voice channel', value = "```\n.name = \n```", inline=False)
    embed.add_field(name='Userlimit for voice channel', value = "```\n.userlimit = \n```")
    embed.add_field(name='Hide voice channel', value = "```\n.close\n```", inline=False)
    embed.add_field(name='Show voice channel', value = "```\n.open\n```", inline=False)

    await message.channel.send(embed=embed)


#2 name
async def edit_name(message, channel):

    name = message.content.split("=")[1]

    for i in privateVoiceChannels:
        if i.name == name: 
            await message.channel.send("Name is already used, please pick another one")
            break
    else: 
        #break wasn´t called -> no channel with same name
        for a in privateVoiceChannels: 
            if a.channel == channel:
                a.name = name
                await channel.edit(name = name)


#3 userlimit
async def edit_user_limit(message, channel):
    userLimit = message.content.split("=")[1]
    
    #TODO: acept user limit none... 

    if isInt(userLimit):
        if int(userLimit) > 0 and int(userLimit) < 100: 
            await channel.edit(user_limit = int(userLimit))
        else: 
            await message.channel.send("Your User Limit has to be between 1 and 99")
            
    else:
        await message.channel.send("Please enter a valid number")