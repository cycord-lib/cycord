import discord

print(dir(discord.Asset))
exit()
print(dir(discord.User))

discord.Asset.BASE

class Asset(object):
    BASE:str = "https://cdn.discordapp.com"

class User(object):
    accent_color
