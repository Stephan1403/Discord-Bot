#user has to be in channel 
#channes has to contain at least 2 users 
#somehow not only return numbers but also given values 
#TODO: only for certain people

import random
from discord.ext import commands

class randomChoice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def random(self, ctx, *number):
        if ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            if len(channel.members) > 1:    #returning empty list try fixing with intents
                print(number)
            else:
                print(channel.members)
                await ctx.channel.send("This command needs at least two users in your voice channel")

        else:
            await ctx.channel.send("You have to be in a channel to use this command")
        



def setup(client):
    client.add_cog(randomChoice(client))


