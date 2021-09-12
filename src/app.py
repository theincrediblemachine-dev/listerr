import requests
import re
import json
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/cf-dvd-streaming-all")
def rt():
    URL = "https://www.rottentomatoes.com/browse/cf-dvd-streaming-all/"
    page = requests.get(URL)
    scrapedata = re.findall(r'\[\{"id.+\}\]',page.text)
    for element in scrapedata:
        return element

if __name__ == "__main__":  # There is an error on this line
    app.run(debug=True, host='0.0.0.0',port=8089)
