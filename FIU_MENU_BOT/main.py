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
from botanke_googleshets import insert_phone_numbers
from botanke_googleshets import insert_messages


insert = insert_messages()
insert = insert_phone_numbers()

account_sid = "AC794240e46ce40abb27fa120c2f9d34fc"
auth_token = "be85b90959f26197eb0d8f7a6c9e04a4"
client = Client(account_sid, auth_token)


# LUNCH TEXT


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


@bot.event
async def on_ready():
    print("Function to send csv file is ready")


@commands.has_role("DEVS")
async def csv(ctx):
    await ctx.send("test")


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


# STORING DATA INTO JSON FILE


def write_json(data, filename="/Users/ethancastano/Desktop/c/FIU_MENU_BOT/rec.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=3)


with open("/Users/ethancastano/Desktop/c/FIU_MENU_BOT/rec.json") as json_file:
    data = json.load(json_file)
    temp = data["fiu_menu_bot"]
    y = {"phone_number": [message(975903281786281984)], "message": [lunch_text]}
    temp.append(y)

write_json(data)


# TEXTMESSAGING


def send_text_message(destination: str, message: str):
    message = client.messages.create(body=message, from_="+17655387616", to=destination)

    print(message.sid)


def main():
    send_text_message(retrieve_messages("975903281786281984"), lunch_text)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    schedule.every().day.at("10:00").do(send_text_message)
    while True:
        schedule.run_pending()
        time.sleep(1)


client_discord.run(discord_token)
