from discord import Embed, Colour
import random

from discord.channel import TextChannel
from discord.webhook import RequestsWebhookAdapter


from voiceChannel import voiceChannel
from methods import get_category_by_name, get_tChannel_by_vChannel, get_vChannel_by_tChannel, isInt

publicVoiceChannels = []
privateVoiceChannels = []


# create Voice Channel
async def create_voice_channel(member, name, category):
    channel = await member.guild.create_voice_channel(name, category=category)
    return channel

# delete Voice Channel


async def delete_voice_channel(channelList):
    for i, e in enumerate(channelList):
        if not e.channel.members:  # voice channel is empty
            del channelList[i]
            await e.channel.delete()
            if e.textChannel:
                await e.textChannel.delete()

# create Text channel


async def create_text_channel(member, name, category):
    channel = await member.guild.create_text_channel(name, category=category)
    return channel


async def admin_channels(member, before, after):

    # create voice channels
    if after.channel is not None:

        if after.channel.name == "New Talk":
            await public_channel(member)

        if after.channel.name == "New private Talk":
            await private_channel(member)

    # delete voice channels
    await delete_voice_channel(publicVoiceChannels)
    await delete_voice_channel(privateVoiceChannels)

    # update text channel permission
    await update_text_channel_permisions(member, before, after)


# public voice channel
async def public_channel(member):

    name = f"Talk by {member.name}"  # TODO: give numbers in order
    category = get_category_by_name(member.guild, "Public")

    channel = await create_voice_channel(member, name, category)
    await member.move_to(channel)

    publicVoiceChannels.append(voiceChannel(name, member, channel, None))


# private voice channel
async def private_channel(member):

    channelNumber = random.randint(1, 100)
    name = f"Private Talk {channelNumber}"
    category = get_category_by_name(member.guild, "Private")

    # voice channel
    channel = await create_voice_channel(member, name, category)
    await member.move_to(channel)

    # text channel
    t_name = f"Channel {channelNumber} Administration"
    t_channel = await create_text_channel(member, t_name, category)

    # text channel permissions
    await t_channel.set_permissions(member.guild.default_role, view_channel=False)
    await t_channel.set_permissions(member, view_channel = True)


    privateVoiceChannels.append(voiceChannel(name, member, channel, t_channel))


# ------Edit voice_channel commands------

# change visibility for textchannel
async def control_voice_channel(message, member):
    # TODO: somehow later iterate through all lists
    if get_vChannel_by_tChannel(message.channel, privateVoiceChannels):

        voice_channel = get_vChannel_by_tChannel(message.channel, privateVoiceChannels)
        command = message.content.lower().replace(" ", "")

        if command.startswith("."):

            if command.startswith(".name="):
                await edit_name(message, voice_channel)
            if command.startswith(".userlimit="):
                await edit_user_limit(message, voice_channel)
            if command.startswith(".close"):
                await close(member, voice_channel)
            if command.startswith(".open"):
                await open(member, voice_channel)


# 1 info - Embed
async def voice_channel_info(message):
    embed = Embed(
        title="Voice channel commands",
        colour=Colour.orange(),
        discription='The following commands are only available for private voice channels')

    embed.set_author(name="Discord Bot")
    embed.add_field(name="Voice channel info",
                    value="```\n.info\n```", inline=False)
    embed.add_field(name='Name of voice channel',
                    value="```\n.name = \n```", inline=False)
    embed.add_field(name='Userlimit for voice channel',
                    value="```\n.userlimit = \n```")
    embed.add_field(name='Hide voice channel',
                    value="```\n.close\n```", inline=False)
    embed.add_field(name='Show voice channel',
                    value="```\n.open\n```", inline=False)

    await message.channel.send(embed=embed)


# 2 name
async def edit_name(message, channel):

    name = message.content.split("=")[1]
    
    if len(name)<1:
        await message.channel.send("Your name can´t be empty")
        return

    for i in privateVoiceChannels:
        if i.name == name:
            await message.channel.send("Name is already used, please pick another one")
            break
    else:
        # break wasn´t called -> no channel with same name
        for a in privateVoiceChannels:
            if a.channel == channel:
                a.name = name
                await channel.edit(name=name)
                await message.channel.edit(name=f"{name} Administration")


# 3 userlimit
async def edit_user_limit(message, channel):
    userLimit = message.content.split("=")[1]

    # TODO: acept user limit none...

    if isInt(userLimit):
        if int(userLimit) > 0 and int(userLimit) < 100:
            await channel.edit(user_limit=int(userLimit))
        else:
            await message.channel.send("Your User Limit has to be between 1 and 99")

    else:
        await message.channel.send("Please enter a valid number")


# 4 close
async def close(member, channel):
    await channel.set_permissions(member.guild.default_role, view_channel=False)
    # for i in channel.members:
    #     await channel.set_permissions(i, view_channel=True)

# 5 open
async def open(member, channel):
    await channel.set_permissions(member.guild.default_role, view_channel=True)


# 6 user list





# ------Edit text_channel commands------

async def update_text_channel_permisions(member, before, after):

    #for before channel
    if get_tChannel_by_vChannel(before.channel, privateVoiceChannels):
        
        t_channel = get_tChannel_by_vChannel(before.channel, privateVoiceChannels)
        await t_channel.set_permissions(member, view_channel=False)

    #for after channel
    if get_tChannel_by_vChannel(after.channel, privateVoiceChannels):

        t_channel = get_tChannel_by_vChannel(after.channel, privateVoiceChannels)
        await t_channel.set_permissions(member, view_channel=True)

