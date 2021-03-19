from discord.flags import MemberCacheFlags
from methods import get_member_by_user
from channelAdministration import admin_channels, voice_channel_commands
import discord


intents = discord.Intents.default()
intents.members = True


class MyClient(discord.Client):


    def __init__(self):
        super().__init__(
            intents=intents.all()
        )


    #on log in
    async def on_ready(self):
        print("looged in")

    #on message
    async def on_message(self, message):

        #get member
        member = get_member_by_user(client.guilds[0], message.author)

        #call voice_channel_commands
        await voice_channel_commands(message, member)


    #on voice update
    async def on_voice_state_update(self, member, before, after):
        await admin_channels(member, after)


client = MyClient()
client.run('ODAyMjcwMDMwMzM5MjQ0MDMz.YAsyMA.H74vF2_HVsOsW1wiB9gJYGCCGxM')
