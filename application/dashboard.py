from cmath import pi
from flask import Flask
from flask import render_template

# Import my extractors I want to use.
import extractors

# Load out personal display settings
from personal_display_settings import display_settings

# Start your engines...
app = Flask(__name__)
app.config.from_object('config.DevConfig')
debug = app.config["DEBUG"]

@app.route("/")
def dashboard():
    """
    Gathers up all the methods we need for the dashboard and 
    templates it in to the svg file.
    """
    styles = set()
    for widget in display_settings["widgets"]:
        widget_name = widget["name"]
        arguments = widget["arguments"]
        widget_template = "widgets/" + widget["name"] + ".html"
        widget_size = widget["size"]
        extractor = getattr(extractors, widget_name)
        widget["rendered"] = render_template(widget_template, c = extractor(**arguments, **widget_size))
        styles.add(widget_name)
    print(styles)
    context = dict(
        styles = styles,
        widgets = display_settings["widgets"],
        display_style = display_settings["display_style"]
        )
    return render_template("base.html", c=context)

@app.route("/tool/<tool_name>")
def render_tool(tool_name):
    content=""
    return render_template("widgets/" + tool + ".html", context = context)


if __name__ == "__main__":
    app.run()