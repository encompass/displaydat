from cmath import pi
from flask import Flask
from flask import render_template

# Import my extractors I want to use.
from extractors import the_time
from extractors import picture
from extractors import inspiration

# Start your engines...
app = Flask(__name__)
app.config.from_object('config.DevConfig')


@app.route("/")
def dashboard():
    """
    Gathers up all the methods we need for the dashboard and 
    templates it in to the svg file.
    """
    context = dict(
        time=the_time(),
        picture=picture(),
        inspiration=inspiration()
    )
    return render_template("digital_board_template.svg", c=context)


if __name__ == "__main__":
    app.run()
