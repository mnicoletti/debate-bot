import discord
import logging
from enums import url_data
from discord.ext import commands

log = logging.getLogger(__name__)
class ApexMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       
        self.color = 0x008f34

    @commands.command(aliases=["h"])
    @commands.bot_has_permissions(manage_messages=True, add_reactions=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Ayuda de comandos desactivados", colour=discord.Colour(0x8f34), url="https://github.com/mnicoletti/debate-bot", description="Podés revisar [codigo fuente y documentacion](https://github.com/mnicoletti/debate-bot)\nSi querés darme una colaboración, vení y chupame un huevo. O mandá plata.")

        embed.set_thumbnail(url=url_data.URLData.TOTO_LOGO)
        embed.set_author(name="Debate Bot", icon_url=url_data.URLData.TOTO_LOGO)
        embed.set_footer(text="Hecho gratis hasta que Perfect se ponga a streamear y nos llenemos de plata.", 
        icon_url=url_data.URLData.PREDATOR_LOGO)

        embed.add_field(name="**Ayuda**", 
        value="""**`<apex!help | apex!h>`**: Esta pantalla de ayuda.""",
        inline=False)
        embed.add_field(name="**Mapas**", 
        value="""**`<apex!rotation | apex!maps>`**: Muestra el mapa actual en juego, su duración y el próximo mapa en rotación.\n
        **`<apex!rotation | apex!maps> pois`**: Muestra un listado de PoIs para el mapa en curso.\n
        **`<apex!rotation | apex!maps> <cantidad>`**: Muestra el mapa en curso y una <cantidad> de rotaciones futuras, con un máximo de 5.\n
        """,
        inline=False)
        embed.add_field(name="**Perfiles (No implementados)**", 
        value="""**`<apex!perfil | apex!profile>`**: Muestra el perfil registrado de usuario.\n
        **`<apex!perfil | apex!profile> save [Origin ID]`**: Crea un vinculo entre tu cuenta de Discord y tu perfil de Apex.\n
        **`<apex!perfil | apex!profile> display`**: Muestra el perfil vinculado a esta cuenta de Discord.\n
        **`<apex!perfil | apex!profile> ranked`**: Muestra el rango actual y puntos acumulados para el split en juego.\n
        **`<apex!perfil | apex!profile> lastmatch`**: Resultados de la última partida.\n
        """,
        inline=False)
        embed.add_field(name="**Challenges (No implementados)**", 
        value="""**`apex!challenge poi`**: Elige un PoI al azar para el mapa en curso.\n
        **`apex!challenge legend`**: Selecciona una leyenda al azar para la próxima partida.\n
        **`apex!challenge team`**: Armar una comp aleatoria para la próxima partida.\n
        """,
        inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ApexMessages(bot))