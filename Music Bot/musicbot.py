import sys

from discord.ext import commands

class MusicBot(commands.Bot):

    async def on_ready(self):
        print("Music bot online")

    async def on_message(self, message):
        print("new message")

