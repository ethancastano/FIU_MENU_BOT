from ast import Break
from asyncore import write
from fileinput import filename
from tokenize import Token
import schedule
import requests
import time
from datetime import date, datetime
from twilio.rest import Client
import discord
from discord.ext import commands
import json
import asyncio
import os
from os import path
import pygsheets
import pandas as pd


def get_url(date):
    date = datetime.now().strftime("%Y/%m/%d")
    url = "https://api.dineoncampus.com/v1/location/5b64638f1178e90b8937224b/periods?platform=0&date={d}".format(
        d=date
    )
    file = requests.get(url)
    record = file.json()
    return record


# print(get_url(date))

food_name = get_url(date)["menu"]["periods"]["categories"]

item_name = food_name[0]["items"]
item_name_1 = item_name[0]["name"]

item_name = food_name[0]["items"]
item_name_2 = item_name[1]["name"]

item_name = food_name[0]["items"]
item_name_3 = item_name[2]["name"]

item_name = food_name[0]["items"]
item_name_4 = item_name[3]["name"]

item_name = food_name[0]["items"]
item_name_5 = item_name[4]["name"]


lunch_text = f"Good afternoon, on the lunch menu today is {item_name_1}, {item_name_2}, {item_name_3}, {item_name_4}, and {item_name_5}"

print(lunch_text)


# DISCORD DATA

discord_token = "OTc0NDg5NzczOTQ5NDc2ODY1.GU_gBw.8PEm3yajqbp72NtuLxz85R9AS-giRZ73yA75qI"
client_discord = discord.Client()


@client_discord.event
async def on_ready():
    print("FIU Bot Menu is ready to go!!")


bot = commands.Bot(command_prefix="-")


@client_discord.event
async def on_ready():
    print("{0.user} is online!".format(client_discord))


@client_discord.event
async def on_message(message):
    if message.author == client_discord.user:
        return


@client_discord.event
async def phone_number(message):
    if message.content.startswith("+"):
        return message.content

    print(phone_number(message))


def retrieve_messages(channelid):
    headers = {
        "authorization": "NzI0ODYzNzIzNjE2ODYyMjU5.GO52wN.LNo9Kg67n-UvY_9RPSPUW8a8DmmC6zdGkshOYk"
    }
    r = requests.get(
        f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers
    )
    jsonn = json.loads(r.text)
    for value in jsonn:
        return value["content"]


message = retrieve_messages
print(message(975903281786281984))


# GOOGLE SHEETS UPDATE


def write_json(
    data, filename="/Users/ethancastano/Desktop/c/FIU_MENU_BOT/fiugsheets.json"
):
    with open(filename, "w") as f:
        json.dump(data, f)


with open("/Users/ethancastano/Desktop/c/FIU_MENU_BOT/fiugsheets.json") as json_file:
    data = json.load(json_file)
    temp = data["fiu_menu_bot"]
    y = [message(975903281786281984)], [lunch_text]
    temp.append(y)

write_json(data)
