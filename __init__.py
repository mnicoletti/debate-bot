import discord
import os
import sys
import logging
from discord.ext import commands

## Custom modules
from modules import channel_messages
from modules import perfect_update
from modules import file_management
from modules import helper

from enums import file_data

## Custom classes
from classes.discord_data import DiscordBotJsonData
from classes.perfect_data import PerfectData

## Intents Setup
intents = discord.Intents.default()
intents.presences = True
intents.members = True

## Objects
client = commands.Bot(command_prefix=commands.when_mentioned_or("apex!"),
            activity=discord.Game(name="Apex Legends"),
            status=discord.Status('dnd'),
            intents=intents,
            help_command=None)
discord_guild = DiscordBotJsonData(str(file_data.ConfigFiles.DISCORD_CONFIG))
perfect_status = PerfectData(str(file_data.ConfigFiles.DB_CONFIG))

## Logger setup
file_management.create_dir(discord_guild.log_path())
log_file_path="{0}/{1}.log".format(discord_guild.log_path(), discord_guild.log_file())
logging.basicConfig(level=helper.set_logging_level("INFO"), filename=log_file_path, filemode='a', format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
logging.getLogger().setLevel(logging.INFO)

for filename in os.listdir('{0}/cogs'.format(discord_guild["install_path"])):
    if filename.endswith('.py'):
        logging.info("Loading cog: {}".format(filename[:-3]))
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        logging.info("Unable to load cog: {}".format(filename[:-3]))

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

#### Channel message actions
########
@client.event
async def on_message(message):
    output_msg = []
    perfect_msg = channel_messages.remember_perfect(client, perfect_status, message)
    boke_msg = channel_messages.this_is_boca(client, message)

    if perfect_msg:
        output_msg.append(perfect_msg)
    if boke_msg:
        output_msg.append(boke_msg)

    if len(output_msg) > 0:
        output_msg = '\n'.join(map(str,output_msg))
        await message.reply(output_msg)
    
    await client.process_commands(message)

#### Member update actions
########
@client.event
async def on_member_update(before, after):
    perfect_update.save_offline(client, perfect_status, before, after)

#### Commands
########
@client.command(name="")
async def apex_help(ctx):
    await ctx.message.delete()

client.run(discord_guild.token())
