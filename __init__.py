import discord
import os
import sys
import logging

## Custom modules
from modules import channel_messages
from modules import perfect_update
from modules import file_management

## Custom classes
from classes.discord_data import DiscordBotJsonData
from classes.perfect_data import PerfectData

config_file = '%s/etc/discord.json' % os.path.dirname(os.path.realpath(__file__))
perfect_file = '%s/etc/perfect.json' % os.path.dirname(os.path.realpath(__file__))

## Objects
client = discord.Client()
discord_guild = DiscordBotJsonData(config_file)
perfect_status = PerfectData(perfect_file)

## Logger setup
file_management.create_dir(discord_guild.log_path())
log_file_path="%s/%s.log" % (discord_guild.log_path(), discord_guild.log_file())
logging.basicConfig(filename=log_file_path, filemode='w', format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
logging.getLogger().setLevel(logging.INFO)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == discord_guild.guild_name():
            break

    startup_message = (
        f'#########################################################\n'
        f'# {client.user} se conecto a guild:\t\t\t#\n'
        f'# {guild.name}(id: {guild.id})\t\t\t#\n'
        f'#########################################################\n'
    )
    print('{}'.format(startup_message))
    logging.info(startup_message)

channel_messages.remember_perfect(client, perfect_status)
perfect_update.save_offline(client, perfect_status)
client.run(discord_guild.token())