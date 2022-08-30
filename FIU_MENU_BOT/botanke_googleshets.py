from pyexpat.errors import messages
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import pygsheets
import json
import pandas as pd
import json
import black

path = "/Users/ethancastano/Desktop/c/FIU_MENU_BOT/botanke_keys.json"
gc = pygsheets.authorize(service_account_file=path)


List = [
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
print(List[0])


def test_function():
    sh = gc.open("Botanke Discord")
    wks = sh.sheet1
    wks.append_table(
        values=[
            (List[0]),
            (List[1]),
            (List[2]),
            (List[3]),
            (List[4]),
            (List[5]),
            (List[6]),
            (List[7]),
            (List[8]),
            (List[9]),
            (List[10]),
            (List[11]),
            (List[12]),
            (List[13]),
            (List[14]),
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
