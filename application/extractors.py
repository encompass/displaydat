# Perhaps we should grab from these...
# https://github.com/public-apis/public-apis
from datetime import datetime
import pytz
import requests


def the_time(local_timezone, debug):
    if debug:
        print("Starting: the_time")
    return(pytz.timezone(local_timezone).localize(datetime.now()).strftime("%H:%M"))

def weather(debug):
    """
    https://openweathermap.org/api
    """
    if debug:
        print("Starting: weather")
    message = "Not ready."
    return(message)

def trello_cards(api_key, api_token, list_id, width="1", height="1", debug=False):
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
    cards = response.json()
    context = {
        "width": width,
        "height": height,
        "cards": cards
        }
    return(context)


def html(text_content, width="1", height="1", debug=False):
    """
    A test widget that just shows what ever text you want on the screen.
    More for testing or using as a starter for your next widget.
    """
    if debug:
        print("html: " + text_content)
    context = {
        "width": width,
        "height": height,
        "text_content": text_content
    }
    return(context)
