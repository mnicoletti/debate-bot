import discord
import re
import random

def remember_perfect(discord_client: discord.Client):
    @discord_client.event
    async def on_message(message):
        msg_author = message.author.mention
        lst_perfect_msg = [
            "Te acordás de Perfect, %s?" % msg_author,
            "Do you remember about Perfect, %s?" % msg_author,
            "Alguno se acuerda de Perfect, @everyone?",
            "Che, te acordás de Perfect?",
            "Che, te acordás de Perfect, %s?" % msg_author
        ]
        perfect_msg = random.choice(lst_perfect_msg)
        if message.author == discord_client.user:
            return
        if re.search(r'(^|\s)(perfect)(\s|\n|$)', message.content, re.IGNORECASE):
            await message.channel.send(perfect_msg)
            return True