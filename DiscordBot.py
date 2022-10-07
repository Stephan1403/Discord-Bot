from methods import get_member_by_user
from channelAdministration import admin_channels, control_voice_channel, update_game_activity
from Covid.Covid import coronaInfoEmbed
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

        #Voice Channel Control
        await control_voice_channel(message, member)

        #corona
        await coronaInfoEmbed(message)

    #on voice update
    async def on_voice_state_update(self, member, before, after):

        #admin channels
        await admin_channels(member, before, after)

    #member update
    async def on_member_update(self, before, after):
        await update_game_activity(client.guilds[0], before, after)



client = MyClient()
client.run()
