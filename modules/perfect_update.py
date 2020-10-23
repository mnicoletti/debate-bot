import discord
from classes.perfect_data import PerfectData
import logging

log = logging.getLogger(__name__)

def save_offline(discord_client: discord.Client(), perfect_info: PerfectData, before, after):
    try:
        if after.name == perfect_info.nickname() and str(after.status) == "offline":
            perfect_info.update_offline_date()
        if after.name == perfect_info.nickname() and str(before.status) == "offline" and str(after.status) == "online":
            log.info("Perfect se puso online.")
    except AttributeError as er:
        log.critical("Unexpected type error: {}".format(er))
    except Exception as er:
        log.critical("Unexpected exception caught: {}".format(er))