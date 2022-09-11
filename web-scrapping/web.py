import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text , 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links , subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href' , None)
        votes = subtext[idx].select('.score')
        if len(vote):
            points = int(votes[0].getText().replace(' points', ''))
            print(points)
            hn.append({'title': title, 'link': href})
    return hn


create_custom_hn(links, subtext)

