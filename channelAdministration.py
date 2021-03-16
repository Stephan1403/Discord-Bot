

publicVoiceChannels = []


#create Voice Channel
async def create_voice_channel(member, voiceChannel):   #channel info passed as own type
    channel = await member.guild.create_voice_channel(voiceChannel.name, category = voiceChannel.category, user_limit = voiceChannel.user_limit)
    return channel


