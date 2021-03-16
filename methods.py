def get_category_by_name(guild, categoryName):
    category = None
    for c in guild.categories:
        if c.name == categoryName:
            category = c
            break
    return category



    #test varibales
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False