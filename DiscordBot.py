from Music.MusicBot import music_bot_control
from methods import get_member_by_user
from channelAdministration import admin_channels, control_voice_channel, update_game_activity
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

        #music bot
        await music_bot_control(message, member, client)
        

    #on voice update
    async def on_voice_state_update(self, member, before, after):

        #admin channels
        await admin_channels(member, before, after)

    #member update
    async def on_member_update(self, before, after):
        await update_game_activity(client.guilds[0], before, after)



client = MyClient()
client.run()
