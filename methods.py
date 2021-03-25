#category by name
def get_category_by_name(guild, categoryName):
    category = None
    for c in guild.categories:
        if c.name == categoryName:
            category = c
            break
    return category

def get_tChannel_by_name(guild, channelName):
    channel = None
    for c in guild.channels:
        if c.name == channelName:
            channel = c 
            break
    return channel

#member by user
def get_member_by_user(guild, user):
    member = None
    for c in guild.members:
        if c.name == user.name:
            member = c
            break
    return member

#channel in channelList
def in_channelList(channel, channelList):
    for i in channelList:
        if i.channel == channel:
            return True
    return False
    

#voice channel by text channel
def get_vChannel_by_tChannel(tChannel, listA):
    
    for i, e in enumerate(listA):
        if e.textChannel == tChannel:
            if listA[i].channel:
                return listA[i].channel
    
#text channel by voice channel
def get_tChannel_by_vChannel(vChannel, listA):
    
    for i, e in enumerate(listA):
        if e.channel == vChannel:
            if listA[i].textChannel:
                return listA[i].textChannel


#test varibales
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

