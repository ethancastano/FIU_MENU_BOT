from pyexpat.errors import messages
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import pygsheets
import json
import pandas as pd
import json
import black

path = "/Users/ethancastano/Desktop/c/FIU_MENU_BOT/botanke_keys.json"
gc = pygsheets.authorize(service_account_file=path)


ticket = [
    "ticket_number",
    "date_time",
    "discord_name”,”status”,”phone_number",
    "selling_location",
    "date_time",
    "first_name",
    "last_name",
    "address_line1",
    "state_province",
    "postal_code",
    "country_code",
    "city_locality",
    "price_lock",
    "bank_account_number",
    "bank_routing",
]


def test_function():
    sh = gc.open("Botanke Discord")
    wks = sh.sheet1
    wks.append_table(
        values=[
            (ticket[0]),
            (ticket[1]),
            (ticket[2]),
            (ticket[3]),
            (ticket[4]),
            (ticket[5]),
            (ticket[6]),
            (ticket[7]),
            (ticket[8]),
            (ticket[9]),
            (ticket[10]),
            (ticket[11]),
            (ticket[12]),
            (ticket[13]),
            (ticket[14]),
        ]
    )


test_function()


# def write_json(
#     data, filename="/Users/ethancastano/Desktop/c/Botanke-Label-Bot/tickets.json"
# ):
#     with open(filename, "w") as f:
#         json.dump(data, f)

# with open("/Users/ethancastano/Desktop/c/Botanke-Label-Bot/tickets.json") as json_file:
#     data = json.load(json_file)
#     temp = data["botanke_sheets"]
#     y = [message(975903281786281984)], [lunch_text]
#     temp.append(y)

# write_json(data)
path = "/Users/ethancastano/Desktop/c/FIU_MENU_BOT/botanke_keys.json"
gc = pygsheets.authorize(service_account_file=path)
