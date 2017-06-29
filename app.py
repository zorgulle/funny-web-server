import requests
import webbrowser
from random import randrange
from bs4 import BeautifulSoup

from flask import Flask
from flask import request


app = Flask(__name__)


def extract_content(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    player = soup.find(id='html5video').a['href']
    webbrowser.open(player)


def make_request(search_terms):
    url = ''
    page = randrange(1, 10)

    params = {'k': search_terms, 'p': page}
    response = requests.get(url, params=params)
    print(response.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    videos = soup.find_all('div', class_='thumb-block')

    link = videos[0].p.a['href']

    return url + link

@app.route('/', methods=['GET', 'POST'])
def extract():
    search = request.args.get('search')

    url = make_request(search)

    extract_content(url)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
