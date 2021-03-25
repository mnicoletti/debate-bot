import discord
import re
import random
import logging
from enums import url_data
from classes import database_mgmt
from enums import file_data

log = logging.getLogger(__name__)

class ApexMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0x008f34
        self.__images_url = ""
        self.__images_uri_path = ""
        try:
            self.__apex_db = database_mgmt.DatabaseManager(str(file_data.ConfigFiles.DB_CONFIG))
        except Exception as err:
            logging.critical("Unexpected error ocurred while setting up Help message: {}".format(err))
    
    def __renew_url_values(self):
        str_fields = ["images_url", "images_uri_path"]
        str_table = "apex_data_config"

        try:
            dict_result = self.__apex_db.select_fields(str_fields, str_table)
            self.__image_url, self.__image_uri_path = dict_result[0]["images_url"], dict_result[0]["images_uri_path"]
        except Exception as err:
            logging.critical("Unexpected error ocurred: {}".format(err))

    @commands.command(aliases=["help","h"])
    async def help(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(
            title="Debate Bot - Ayuda",
            description="[codigo fuente y documentacion](https://github.com/mnicoletti/debate-bot)\n"
            "Si querés darme una colaboración, vení y chupame un huevo. O mandá plata.",
            color=self.color
            )
        embed.add_field(name='**Comandos Activos**',
        value="""**`<apex!help | apex!h>`** - Esta pantalla de ayuda.\n
        **`<apex!rotation | apex!maps>`** - Muestra el mapa actual en juego, su duración y el próximo mapa en rotación.\n
        \n""")
        embed.add_field(name='**Comandos no implementados**',
        value="""**Mapas**\n
        **====**\n
        **`<apex!rotation | apex!maps> pois`** - Muestra un listado de PoIs para el mapa en curso.\n
        **`<apex!rotation | apex!maps> <cantidad>`** - Muestra el mapa en curso y una <cantidad> de rotaciones futuras.\n
        \n
        **Perfiles**\n
        **======**\n
        **`<apex!perfil | apex!profile>`** - Muestra el perfil registrado de usuario.\n
        **`<apex!perfil | apex!profile> save [Origin ID]`** - Crea un vinculo entre tu cuenta de Discord y tu perfil de Apex.\n
        **`<apex!perfil | apex!profile> display`** - Muestra el perfil vinculado a esta cuenta de Discord.\n
        **`<apex!perfil | apex!profile> ranked`** - Muestra el rango actual y puntos acumulados para el split en juego.\n
        **`<apex!perfil | apex!profile> lastmatch`** - Resultados de la última partida.\n
        \n
        **Challenges**\n
        **====**\n
        **`apex!challenge poi`** - Elige un PoI al azar para el mapa en curso.\n
        **`apex!challenge legend`** - Selecciona una leyenda al azar para la próxima partida.\n
        **`apex!challenge team`** - Armar una comp aleatoria para la próxima partida.\n""")
        embed.set_image(url=str(url_data.URLData.PREDATOR_LOGO))
        embed.set_footer("Hecho gratis hasta que Perfect se ponga a streamear y nos llenemos de plata.")
        await ctx.send(embed)