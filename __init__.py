import discord
import os
import sys

## Custom modules
from modules import channel_messages
from modules import perfect_update

## Custom classes
from classes.discord_data import DiscordJsonData
from classes.perfect_data import PerfectData

config_file = '%s/etc/discord.json' % os.path.dirname(os.path.realpath(__file__))
perfect_file = '%s/etc/perfect.json' % os.path.dirname(os.path.realpath(__file__))

## Objects
client = discord.Client()
discord_guild = DiscordJsonData(config_file)
perfect_status = PerfectData(perfect_file)

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

channel_messages.remember_perfect(client, perfect_status)
perfect_update.save_offline(client, perfect_status)
client.run(discord_guild.token())