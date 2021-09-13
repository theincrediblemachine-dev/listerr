import requests
import re
import os
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from flask import Flask

# Set Variables
load_dotenv()
portNumber = int(os.getenv('PORT_NUMBER',-1))

# Create Flask App
app = Flask(__name__)

# Routes
@app.route("/")
def base():
    return 'The Incredible Machine'

@app.route("/cf-horror")
def rtcfhorror():
    URL = "https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=70&maxTomato=100&certified=true&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=10&sortBy=release"
    page = requests.get(URL)
    scrapedata = re.findall(r'\[\{"id.+\}\]',page.text)
    for element in scrapedata:
        return element


@app.route("/cf-dvd-streaming-all")
def rtcf():
    URL = "https://www.rottentomatoes.com/browse/cf-dvd-streaming-all/"
    page = requests.get(URL)
    scrapedata = re.findall(r'\[\{"id.+\}\]',page.text)
    for element in scrapedata:
        return element

if __name__ == "__main__":  # There is an error on this line
    app.run(debug=True, host='0.0.0.0',port=portNumber)
