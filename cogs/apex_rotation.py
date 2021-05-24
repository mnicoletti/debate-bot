import discord
import re
import random
from classes import apex_maps
from enums import file_data, url_data
from discord.ext import commands
from datetime import datetime, timedelta
from modules import fences_url
import logging

log = logging.getLogger(__name__)

class ApexRotations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__apex_maps = apex_maps.ApexMaps()
       
        self.color = 0xd0021b

    def __error_message(self, error_type="default"):
        thumb_url = fences_url.obtain_fence_url("Angry")
        embed = discord.Embed(title="That's an angry Fence", 
        colour=discord.Colour(0xd0021b), 
        description="""Esta no es la manera de tratar a tu bot.\n
        Si te estoy mostrando esto es porque pediste alguna función que no puedo interpretar.\n\n
        `**apex!help**` te puede dar toda la ayuda que necesitás.""")

        embed.set_thumbnail(url=thumb_url)
        embed.set_author(name="Debate Bot", 
        url="https://github.com/mnicoletti/debate-bot", 
        icon_url=url_data.URLData.TOTO_LOGO)
        embed.set_footer(text="Debate Bot | La cagaste", 
        icon_url=url_data.URLData.PREDATOR_LOGO)

        if error_type == "bad_type":
            embed.add_field(name="Error de opciones",value="Tenes que ingresar una opción correcta.")

        return embed

    def __select_map_image(self, current_map, type="battle_royale"):
        if type == "battle_royale":
            map_img_seq = random.choice(["01","02","03"])
            if current_map == "World's Edge":
                img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_WORLDSEDGE, map_img_seq)
            elif current_map == "Kings Canyon":
                img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_KINGSCANYON, map_img_seq)
            else:
                img_map_file = "{0}{1}.png".format(url_data.URLData.IMG_OLYMPUS, map_img_seq)
        elif type == "arenas":
            if current_map == "Party crasher":
                img_map_file = "{0}/PartyCrasher01.jpg".format(url_data.URLData.IMG_ARENAS)
            elif current_map == "Phase runner":
                img_map_file = "{0}/PhaseRunner01.jpg".format(url_data.URLData.IMG_ARENAS)
            else:
                img_map_file = "{0}/RotatingMaps01.jpg".format(url_data.URLData.IMG_ARENAS)

        return img_map_file

    @commands.command(aliases=["rotation"])
    async def maps(self, ctx, *args):
        msg_mode = "apex_map"
        map_type = "battle_royale"
        error_type = "default"
        ## Cantidad de argumentos pasados
        try:
            if len(args) == 0:
                msg_mode = "apex_map"
            elif len(args) == 1:
                if args[0] in ["pois"]:
                    msg_mode = "apex_pois"
                elif args[0] in ["arenas"]:
                    map_type = "arenas"
            else:
                    msg_mode = "error"
                    error_type = "bad_type"
        except ValueError as err:
            msg_mode = "error"

        if msg_mode == "error":
            embed = self.__error_message(error_type=error_type)
            await ctx.send(embed=embed)
            return

        (current_map,list_next_maps) = self.__apex_maps.obtain_map_rotation(type=map_type)
        img_map_file = self.__select_map_image(current_map['map'], type=map_type)
        embed = discord.Embed(title="Rotación de mapas", colour=discord.Colour(self.color))

        embed.set_image(url=img_map_file)
        embed.set_author(name="Debate Bot", url="https://github.com/mnicoletti/debate-bot", icon_url=url_data.URLData.TOTO_LOGO)
        embed.set_footer(text="Debate Bot", icon_url=url_data.URLData.PREDATOR_LOGO)

        embed.add_field(name="Mapa Actual", value="Se está jugando **{0}** por los próximos **{1} minutos**.".format(current_map['map'], current_map['remaining']), inline=False)

        if msg_mode == "apex_map":
            next_map_date_arg = datetime.strftime(list_next_maps['start'] - timedelta(hours=3), "%X")    
            embed.add_field(name="Próximo mapa", value="El próximo mapa a jugar es **{0}**, comienza a las *{1}* y tendrá una duración de *{2}* minutos.".format(list_next_maps['map'], next_map_date_arg, list_next_maps['duration']), inline=False)
        elif msg_mode == "apex_pois" and map_type == "battle_royale":
            lst_pois = self.__apex_maps.obtain_pois_from_current(current_map['map'])
            if lst_pois is None:
                logging.critical("Imposible obtener pois para {}".format(current_map['map']))
            str_pois = "\n- ".join(lst_pois)
            embed.add_field(name="Points of Interest", value="- {0}".format(str_pois), inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ApexRotations(bot))