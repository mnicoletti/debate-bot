import discord
import re
import random
from classes import apex_maps
from enums import file_data, url_data
from discord.ext import commands
from datetime import datetime, timedelta
import logging

log = logging.getLogger(__name__)

class ApexRotations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__apex_maps = apex_maps.ApexMaps()
       
        self.color = 0xd0021b

    @commands.command(aliases=["rotation","maps"])
    async def apex_map_rotation(self, ctx):
        map_img_seq = random.choice(["01","02","03"])
        (current_map,list_next_maps) = self.__apex_maps.obtain_map_rotation()
        if current_map['map'] == "World's Edge":
            img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_WORLDSEDGE, map_img_seq)
        elif current_map['map'] == "KingsCanyon":
            img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_KINGSCANYON, map_img_seq)
        else:
            img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_OLYMPUS, map_img_seq)

        embed = discord.Embed(title="Rotación de mapas", colour=discord.Colour(self.color))

        embed.set_image(url=img_map_file)
        embed.set_author(name="Debate Bot", url="https://github.com/mnicoletti/debate-bot", icon_url=url_data.URLData.TOTO_LOGO)
        embed.set_footer(text="Debate Bot", icon_url=url_data.URLData.PREDATOR_LOGO)

        embed.add_field(name="Mapa Actual", value="Se está jugando **{0}** por los próximos **{1} minutos**.".format(current_map['map'], current_map['remaining']), inline=False)

        next_map_date_arg = datetime.strftime(list_next_maps[0]['start'] - timedelta(hours=3), "%X")

        embed.add_field(name="Próximos mapas", value="El próximo mapa a jugar es *{0}*, comienza a las *{1}* y tendrá una duración de *{2}* minutos.".format(list_next_maps[0]['map'], next_map_date_arg, list_next_maps[0]['duration']), inline=False)

        if len(list_next_maps) > 1:
            list_next_maps.remove(list_next_maps[0])
            for next_map in list_next_maps:
                next_map_date_arg = datetime.strftime(next_map['start'] - timedelta(hours=3), "%X")
                text_next_maps = """**{0}**\n**Duración**: {1}\n**Comienza**: {2}""".format(next_map['map'], next_map['duration'], next_map_date_arg)

            embed.add_field(name="Siguientes rotaciones", value=text_next_maps, inline=False)    
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ApexRotations(bot))