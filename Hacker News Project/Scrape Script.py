import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

links = soup.select('.titleline a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def get_links(links):
    page1 = soup.select('.titleline a')
    page2 = soup.find()
def sort_stories_by_points(hacker_news_list):
    return sorted(hacker_news_list, key= lambda k:k['Votes'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news = []
    for indx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        if indx < len(subtext):
            vote = subtext[indx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hacker_news.append({'Title': title, 'Link': href, 'Votes': points})

    return sort_stories_by_points(hacker_news)

pprint.pprint(create_custom_hacker_news(mega_links, mega_subtext))
