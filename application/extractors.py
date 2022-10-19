#Find the time of day.
from datetime import datetime
import pytz
def the_time():
    return(pytz.timezone("Europe/Helsinki").localize(datetime.now()).strftime("%H:%M"))
    
def picture():
    return ("http://placekitten.com/100/100")
