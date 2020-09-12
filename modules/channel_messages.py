import discord
import re
import random
from classes import perfect_data

def remember_perfect(discord_client: discord.Client, perfect_status: perfect_data.PerfectData):
    @discord_client.event
    async def on_message(message):
        for guild in discord_client.guilds:
            perfect_guild_member = guild.get_member(int(perfect_status.id()))

        msg_author = message.author.mention

        lst_remember_msg = [
            "Te acordás de Perfect, %s?" % msg_author,
            "Do you remember about Perfect, %s?" % msg_author,
            "Alguno se acuerda de Perfect, @everyone?",
            "Che, te acordás de Perfect?",
            "Che, te acordás de Perfect, %s?" % msg_author
        ]

        output_msg = random.choice(lst_remember_msg)

        if str(perfect_guild_member.status) != "offline":
            if perfect_guild_member.activity.name == None:
                lst_online_msg = [
                    "Pará, %s está online. Te debe estar ignorando." % perfect_guild_member.mention,
                    "Estás ahí, %s? Te buscan." % perfect_guild_member.mention,
                    "Se olvidó Discord abierto, pero %s está online." % perfect_guild_member,
                    "Ahí lo tenés a %s." % perfect_guild_member.mention
                ]
            elif perfect_guild_member.activity.name != None:
                lst_online_msg = [
                    "Ahí lo tenés a %s, con %s." % (perfect_guild_member.mention, perfect_guild_member.activity.name),
                    "Eu, está jugando a %s este %s." % (perfect_guild_member.activity.name,perfect_guild_member.mention),
                    "Te fijaste que %s está en %s? Capaz está en el otro Discord. Con sus amigos de verdad." % (perfect_guild_member.mention, perfect_guild_member.activity.name),
                    "Chequea la lista de usuarios, %s está jugando %s." % (perfect_guild_member.mention, perfect_guild_member.activity.name),
                    "Te buscan %s, largá el %s." % (perfect_guild_member.mention, perfect_guild_member.activity.name)
                ]
            output_msg += "\n%s" % random.choice(lst_online_msg)
        elif str(perfect_guild_member.status) == "offline":
            offline_time = perfect_status.calculate_last_offline()
            lst_offline_msg = [
                "Riperino el Perfectino. %s lleva offline %s." % (perfect_guild_member.mention, offline_time),
                "Se nos fue. RIP. %s la quedó hace %s." % (perfect_guild_member.mention, offline_time),
                "El %s nos dejó hace más o menos %s." % (perfect_guild_member.mention, offline_time),
                "%s se borró del Discord hace unos %s." % (perfect_guild_member.mention, offline_time),
                "Nos quedamos sin %s hace %s." % (perfect_guild_member.mention, offline_time),
                "Hace %s que la quedó %s." % (offline_time, perfect_guild_member.mention),
                "Se dieron cuenta que hace %s que no tenemos un %s entre nosotros?" % (offline_time, perfect_guild_member.mention),
                "Yo creo que ya fue. Ya pasaron %s desde la última vez que tuvimos noticias de %s." % (offline_time, perfect_guild_member.mention),
                "A %s le cayó una amiga hace alrededor de %s." % (perfect_guild_member.mention, offline_time),
                "No lo jodas a %s que lleva %s sacando la comida del horno. No sea cosa que se le queme." % (perfect_guild_member.mention, offline_time)
            ]
            output_msg += "\n%s" % random.choice(lst_offline_msg)

        if message.author == discord_client.user:
            return

        if re.search(r'(^|\s)(perfect)(\s|\n|$)', message.content, re.IGNORECASE):
            await message.channel.send(output_msg)
            return True