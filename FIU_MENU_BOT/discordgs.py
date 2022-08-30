import pygsheets
import json
import pandas as pd
import json
import black

path = "/Users/ethancastano/Desktop/c/FIU_MENU_BOT/botanke_keys.json"
gc = pygsheets.authorize(service_account_file=path)


def test_function():
    sh = gc.open("Botanke Discord")
    wks = sh.sheet1
    wks.update_value("A2", "hello")
    wks.update_value("B2", "world")


test_function()
