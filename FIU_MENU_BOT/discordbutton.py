from email.policy import default
from select import select
from tokenize import Token
import black
import discord
from decouple import config
from discord.ext import commands
from discord.ui import View
from discord.ui import Select
from discord.ui import Button
from discord_intents import set_intents
import psycopg2


bot = commands.Bot(commands.when_mentioned_or("-"), intents=set_intents())

discord_token = "OTc0NDg5NzczOTQ5NDc2ODY1.GbR9JU.VcwBq3Z8o-xH3wkK5yhtJLES22i4smM2RSOp5I"


@bot.command
async def menu(ctx):
    select = Select(
        min_values=1,
        max_values=3,
        placeholder="Please Select Menu Type",
        options=[
            discord.SelectOption(
                label="Breakfast Menu",
                emoji="🌅",
                description="Breakfast Menu",
            ),
            discord.SelectOption(
                label="Lunch Menu", emoji="🏙", descriptions="Lunch Menu"
            ),
            discord.SelectOption(
                label="Dinner Menu", emoji="🌃", descriptions="Dinner Menu"
            ),
        ],
        row=2,
    )
    view = View()
    view.add_item(select)

    await ctx.send("Menu Type", view=view)


bot.run(discord_token)


# async def menu_selection(channel_id):
#     "Function to select menu type"
#     breakfast_button = Button(
#         label='Breakfast', style=discord.ButtonStyle.orange, emoji='🌅'
#     )
#     lunch_button = Button(
#         label='Lunch', style=discord.ButtonStyle.blue, emoji='🏙'
#     )
#     dinner_button = Button(
#         label='Dinner', style=discord.ButtonStyle.purple, emoji='🌃'
#     )
#     view=View()
#     view.add_item(breakfast_button)
#     view.add_item(lunch_button)
#     view.add_item(dinner_button)
#     channel = bot.get_channel(int(channel_id))
#     await channel.send(
#             "`Click one of the buttons below to open up an automated ticket.`", view=view
#         )

# async def breakfast_callback(interaction):
