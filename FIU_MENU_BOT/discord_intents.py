import discord
import black


def set_intents():
    "Setting Intents for the bot."
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    return intents
