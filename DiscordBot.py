from channelAdministration import admin_channels
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

    #on voice update
    async def on_voice_state_update(self, member, before, after):
        await admin_channels(member, after)
    


client = MyClient()
client.run('ODAyMjcwMDMwMzM5MjQ0MDMz.YAsyMA.H74vF2_HVsOsW1wiB9gJYGCCGxM')