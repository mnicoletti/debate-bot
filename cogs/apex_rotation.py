import discord
import re
import random
from classes import apex_maps
import logging

log = logging.getLogger(__name__)

@commands.command(aliases=["rotation","maps"])
def apex_map_rotation(discord_client: discord.Client, apex_map_status: apex_maps.ApexMaps, message):
    return