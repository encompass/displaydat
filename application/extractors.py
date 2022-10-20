## Perhaps we should grab from these...
## https://github.com/public-apis/public-apis
from datetime import datetime
import pytz
import requests

def the_time():
    return(pytz.timezone("Europe/Helsinki").localize(datetime.now()).strftime("%H:%M"))
    
def picture():
    return ("http://placekitten.com/100/100")

def weather():
    """
    https://openweathermap.org/api
    """
    message = "Not ready."
    return(message)

def inspiration():
    message = "Sadly, this one isn't ready yet."
    return(message)
    
def trello_cards():
    """
    https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-boardid-boardstars-get
    """
    message = "Sadly, this one isn't ready yet."
    return(message)