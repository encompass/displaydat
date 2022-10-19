from flask import Flask
from flask import render_template

#Import my extractors I want to use.
from extractors import the_time
from extractors import picture
#Start your engines...
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("digital_board_template.svg", time=the_time())
    

