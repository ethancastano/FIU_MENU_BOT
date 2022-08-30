from cgitb import text
from unittest import result
import requests
from bs4 import BeautifulSoup
import pandas as pd
from discord.ext import commands
import discord
import json
from csv import reader
import pandas as pd
import pandas as pd


# #DISCORD


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
searchterm = (message(986386997281181729)).replace(" ", "+")


# URL


def get_data(searchterm):
    url = f"https://www.ebay.com/sch/i.html?_fsrp=1&rt=nc&_from=R40&_nkw={searchterm}&LH_Complete=1&LH_Sold=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def parse(soup):
    results = soup.find_all("div", {"class": "s-item__info clearfix"})
    for item in results:
        product = {
            "title": item.find(
                "h3", {"class": "s-item__title s-item__title--has-tags"}
            ),
            "soldprice": float(
                item.find("span", {"class": "s-item__price"})
                .text.replace("$", "")
                .replace(",", "")
                .strip()
            ),
            #'solddate': item.find('span', {'class': 's-item__title--tagblock '}).find('span', {'class':'POSITIVE'}),
            "link": item.find("a", {"class": "s-item__link"})["href"],
        }
        print(product)
    return
