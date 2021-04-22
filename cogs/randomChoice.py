#user has to be in channel 
#channes has to contain at least 2 users 
#somehow not only return numbers but also given values 
#TODO: only for certain people
#TODO: amout of arguments for each user
#TODO: active or deactivate to change the users name - other command

import random
from discord.ext import commands

class randomChoice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    
    @commands.command()
    async def random(self, ctx, *args):  #Problem: not updating the voice state
        if ctx.author.voice:
            print(ctx.author.voice.channel.name)
        else:
            print("not in channel apparently")

        if ctx.author.voice:
            if args:
                
                matches =  assignArguments(ctx, args, "none")

                for i in matches:
                    await ctx.channel.send(str(i[0]) + ":   " + str(i[1]))

                
            else:
                await ctx.channel.send("Please pass a argument")

        else:
            await ctx.channel.send("You have to be in a voice channel to use this command")



    @commands.command()
    async def randomNick(self, ctx, *args):
        if ctx.author.voice:
            if args:

                matches = assignArguments(ctx, args, "")
                for i in matches:
                    pass
                    

            else:
                await ctx.channel.send("Please pass a argument")
        else:
            await ctx.channel.send("You have to be in a voice channel to use this command")
        



def setup(client):
    client.add_cog(randomChoice(client))


def assignArguments(ctx, args, default):
    #takes arg puts it into arguments appends it to matches list
    arguments = []
    matches = []
    members = ctx.author.voice.channel.members

    for i in args:
        arguments.append(i)

    random.shuffle(arguments)   #args in random order

    for i, mem in enumerate(members):
        if i >= len(arguments):     #no more arguments to asign for a user
            matches.append([ mem.name, default, mem ])   #asign a default 
        else:
            matches.append([ mem.name, arguments[i], mem ]) #member name, a random argument, the member as object
        
    return matches


