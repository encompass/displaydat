# Perhaps we should grab from these...
# https://github.com/public-apis/public-apis
from datetime import datetime
import pytz
import requests


def the_time(local_timezone, debug):
    if debug:
        print("Starting: the_time")
    return(pytz.timezone(local_timezone).localize(datetime.now()).strftime("%H:%M"))


def picture(debug):
    if debug:
        print("Starting: picture")
    return ("http://placekitten.com/100/100")


def weather(debug):
    """
    https://openweathermap.org/api
    """
    if debug:
        print("Starting: weather")
    message = "Not ready."
    return(message)


def inspiration(debug):
    if debug:
        print("Starting: inspiration")
    message = "Sadly, this one isn't ready yet."
    return(message)


def trello_cards(api_key, api_token, list_id, debug):
    """
    https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-boardid-boardstars-get
    """
    if debug:
        print("Starting: trello_cards")
    
    url = "https://api.trello.com/1/lists/" + list_id + "/cards"
    query = {
        'key': api_key,
        'token': api_token
    }

    response = requests.request(
        "GET",
        url,
        params=query
    )
    message = "Your Active tasks:\n"
    for item in response.json():
        message += "✔" + item["name"] + "\n"
    return(message)
