import discord
from discord.ext import commands

class music_bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def cleara(self, ctx, amount=5):
        #test if author = mod or higher
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(music_bot(client))


