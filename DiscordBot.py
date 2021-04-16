import os
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("logged in")



#-----------------cogs----------------------

for root, dirs, files in os.walk('./cogs'):
    for name in files:
        if name.endswith('.py'):
            try:

                root = root.replace("./", "").replace("\\", ".")
                client.load_extension(f'{root}.{name[:-3]}')
            
            except Exception as e:
                print(f"Failed at {name}\nError: {str(e)}")


client.run('ODAyMjcwMDMwMzM5MjQ0MDMz.YAsyMA.H74vF2_HVsOsW1wiB9gJYGCCGxM')