from discord import channel
from discord.ext.commands.core import command
from discord.message import implement_partial_methods
from methods import get_member_by_user
from channelAdministration import admin_channels, control_voice_channel, update_game_activity
from Covid.Covid import coronaInfoEmbed
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!')          #General Bot commands
musicBot = commands.Bot(command_prefix='-')     #Music Bot Commands
channelBot = command.Bot(command_prefix='.')    #channel Bot Commands


class MyClient(discord.Client):

    def __init__(self):
        super().__init__(
            intents=intents.all()
        )


    #on log in
    async def on_ready(self):
        print("looged in")


    @bot.command








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
client.run('ODAyMjcwMDMwMzM5MjQ0MDMz.YAsyMA.H74vF2_HVsOsW1wiB9gJYGCCGxM')
