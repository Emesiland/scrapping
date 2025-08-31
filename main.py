import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
habr = 'https://habr.com/ru/articles/'

def get_articles(url='https://habr.com/ru/articles'):
    headers = Headers(headers=True).generate()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []