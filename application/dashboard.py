from cmath import pi
from flask import Flask
from flask import render_template
from pyfiglet import figlet_format

# Import my extractors I want to use.
from extractors import the_time
from extractors import picture
from extractors import inspiration
from extractors import trello_cards

# Start your engines...
app = Flask(__name__)
app.config.from_object('config.DevConfig')
print(figlet_format("DisplayDat"))
debug = app.config["DEBUG"]


@app.route("/")
def dashboard():
    """
    Gathers up all the methods we need for the dashboard and 
    templates it in to the svg file.
    """
    c_the_time = the_time(app.config['LOCAL_TIMEZONE'], debug)

    c_trello = trello_cards(
        app.config['TRELLO_API_KEY'],
        app.config['TRELLO_API_TOKEN'],
        app.config['TRELLO_LIST_ID'], debug
    )

    c_picture = picture(debug),
    c_inspiration = inspiration(debug),

    context = dict(
        the_time=c_the_time,
        picture=c_picture,
        inspiration=c_inspiration,
        trello=c_trello
    )
    return render_template("base.html", c=context)


if __name__ == "__main__":
    app.run()