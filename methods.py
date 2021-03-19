#category by name
def get_category_by_name(guild, categoryName):
    category = None
    for c in guild.categories:
        if c.name == categoryName:
            category = c
            break
    return category

#member by user
def get_member_by_user(guild, user):
    member = None
    for c in guild.members:
        if c.name == user.name:
            member = c
            break
    return member

#voice channel by text channel
def get_vChannel_by_tChannel(tChannel, listA):
    
    for i, e in enumerate(listA):
        if e.textChannel == tChannel:
            if listA[i].channel:
                return listA[i].channel
    
            


#test varibales
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

