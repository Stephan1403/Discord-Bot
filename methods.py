def get_category_by_name(guild, categoryName):
    category = None
    for c in guild.categories:
        if c.name == categoryName:
            category = c
            break
    return category