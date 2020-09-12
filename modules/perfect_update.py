import discord
from classes.perfect_data import PerfectData

def save_offline(discord_client: discord.Client(), perfect_info: PerfectData):
    @discord_client.event
    async def on_member_update(before, after):
        try:
            if after.name == perfect_info.nickname() and str(after.status) == "offline":
                perfect_info.update_offline_date()
        except AttributeError as er:
            print("Unexpected type error: {}".format(er))
        except Exception as er:
            print("Unexpected exception caught: {}".format(er))