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

    for tag in soup.find('div', class_='tm-articles-list').find_all('article'):
        time_tag = tag.find('time')
        publication_date = time_tag.get('datetime')[:10]
        a_tag = tag.find('h2').find('a')
        article_link = habr + a_tag.get('href')
        article_title = a_tag.find('span').text.strip()

