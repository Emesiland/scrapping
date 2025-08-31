import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
habr = 'https://habr.com'

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
        
        response = requests.get(article_link, headers=headers)
        article_soup = BeautifulSoup(response.text, 'html.parser')
        article_text = article_soup.find('div', id='post-content-body').text.strip()
        
        for keyword in KEYWORDS:
            if keyword.lower() in article_title.lower() or keyword.lower() in article_text.lower():
                articles.append(f"{publication_date} - {article_title} - {article_link}")
                break
    
    return articles

if __name__ == '__main__':
    print(*get_articles(), sep='\n')