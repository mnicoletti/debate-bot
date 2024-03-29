import discord
import re
import random
from classes import perfect_data
from classes import database_mgmt
import logging

log = logging.getLogger(__name__)

def _match_perfect_mention(message):
    
    return False

def remember_perfect(discord_client: discord.Client, perfect_status: perfect_data.PerfectData, message):
    for guild in discord_client.guilds:
        perfect_guild_member = guild.get_member(int(perfect_status.id()))

    msg_author = message.author.mention

    try:
        lst_remember_msg = perfect_status.retrieve_perfect_message("remember_perfect")
        output_msg = random.choice(lst_remember_msg)
    
        if str(perfect_guild_member.status) != "offline":
            if perfect_guild_member.activity == None:
                lst_online_msg = [ x.format(perfect_guild_member.mention) for x in perfect_status.retrieve_perfect_message("perfect_online") ]
            elif perfect_guild_member.activity.name != None:
                if perfect_guild_member.activity.name in ["Apex", "apex", "Apex Legends"]:
                    lst_online_msg = [ x.format(perfect_guild_member.mention) for x in perfect_status.retrieve_perfect_message("perfect_apex") ]
                else:
                    lst_online_msg = [ x.format(perfect_guild_member.mention, perfect_guild_member.activity.name) for x in perfect_status.retrieve_perfect_message("perfect_activity") ]
                    
            output_msg += "\n{}".format(random.choice(lst_online_msg))
        elif str(perfect_guild_member.status) == "offline":
            offline_time = perfect_status.calculate_last_offline()
            lst_offline_msg = [ x.format(perfect_guild_member.mention, offline_time) for x in perfect_status.retrieve_perfect_message("perfect_offline") ]
            output_msg += f"\n{random.choice(lst_offline_msg)}"
    except AttributeError as er:
        log.critical("Unexpected type error: {}".format(er))
    except Exception as er:
        log.critical("Unexpected exception caught: {}".format(er))

    if message.author == discord_client.user:
        return

    if re.search(r'(^|\s|@)(perfect)(\s|\n|\?|\.|\,|$)', message.content, re.IGNORECASE):
        log.info(f"Perfect mention: {message.author.name}")
        return output_msg

def this_is_boca(discord_client: discord.Client, message):
    boquita = 'BOCA'.replace('O', 'O'*random.randrange(1,15),1).replace('A','A'*random.randrange(1,15),1)
    boquiten = 'BOKE'.replace('O', 'O'*random.randrange(1,15),1).replace('E','E'*random.randrange(1,15),1)
    random_boke = random.choice([boquita,boquiten])

    #lst_boca_msg = [
        #f"El mas grande, papá, {random_boke}!",
        #random_boke,
        #f"ESTO ES {boquita}",
        #"Todo muy lindo con boquita pero, ¿¡CUANDO ARRANCA EL MUNDIAL!?"
    #]
    lst_boca_msg = [
        "Para dramas ya está tu hermana. Ahora dejame dedicarme al mundial.",
        "¿Podés parar con boca? ¿CUANDO JUEGA LA SELECCIÓN?",
        random_boke,
        "Yo ahora quiero descansar. Comer asado, pasarla bien."
    ]

    output_message = random.choice(lst_boca_msg)

    if message.author == discord_client.user:
        return
        
    if re.search(r'(^|\s|@)B+O+[KC]+[AE]+(\s|\n|\?|\.|\,|\!|\"|$)', message.content, re.IGNORECASE) or re.search(r'(^|\s|@)(b+o+qui+t|b+o+ki+t)[A]+(\s|\n|\?|\.|\,|\!|\"|$)', message.content, re.IGNORECASE):
        log.info(f"Boquita mention: {message.author.name}")
        return output_message
