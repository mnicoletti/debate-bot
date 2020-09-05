import discord
import os
import sys

local_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append('%s/modules' % local_dir)
sys.path.append('%s/classes' % local_dir)

## Custom modules
import channel_messages

## Custom classes
from discord_data import DiscordJsonData

config_file = '%s/etc/discord.json' % os.path.dirname(os.path.realpath(__file__))

## Objects
discord_guild = DiscordJsonData(config_file)
client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == discord_guild.guild_name():
            break

    print(
        f'#########################################################\n'
        f'# {client.user} se conecto a guild:\t\t\t#\n'
        f'# {guild.name}(id: {guild.id})\t\t\t#\n'
        f'#########################################################\n'
    )

channel_messages.remember_perfect(client)

client.run(discord_guild.token())