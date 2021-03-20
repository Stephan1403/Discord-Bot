from methods import get_member_by_user
from channelAdministration import admin_channels, control_voice_channel, update_text_channel_permisions
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

        #call control voice channel
        await control_voice_channel(message, member)
        

    #on voice update
    async def on_voice_state_update(self, member, before, after):

        #admin channels
        await admin_channels(member, before, after)



client = MyClient()
client.run('ODAyMjcwMDMwMzM5MjQ0MDMz.YAsyMA.H74vF2_HVsOsW1wiB9gJYGCCGxM')
