# displaydat
This is a, not functioning yet, simple display board we are making to see if we can make something interesting.  I have old screens that are begging for something like this in my home.

# Installation instructions
Get the computer you want to install it on, and dust it off.  It should be running in such a way to display something on the screen.  I suppose you could set this up with a tablet as well with a computer hosting the site.
I used advise from:
* https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

Make sure you have python installed.
Clone the application to where you want to run it.

    git clone git@github.com:encompass/displaydat.git

Go into the directory

    cd displaydat

Setup your virtual environment

    python -m venv env

Connect your your virtual environment

    source env/bin/activate

Install the required packages

    pip install -r requirements.txt

Copy the .env_template to your own. You may need to edit some of .env to get all the features working.

    cp .env_template .env

Run the environment
    python dashboard.py

Have fun.  

# Initial Plans
* Create limiter on the API calls so that I can use free accounts without billings.
* Display the weather
* Display pictures from a folder or something
* Display quotes from a public api
* Display calender
* Display Trello Cards

# Frequently asked questions:
## Why don't you just use \<insert tool here\>?
Because I want to learn how to do it myself.
## How can I help?
Clone, improve and we will take a look.  Happy to have more people contribute.

