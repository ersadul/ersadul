from bs4 import BeautifulSoup
import requests
import pandas as pd


columns = {
    'headline':[],
    'summary':[],
    'video':[]
}
df = pd.DataFrame(columns)
source = requests.get('http://coreyms.com').text

# get request from website and using lxml parser
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

# article = soup.find('article')
for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    # find class with tag 
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        video_id = video_src.split('/')[4].split('?')[0]
        link = f'https://www.youtube.com/watch?v={video_id}'
    except:
        link = None

    print(link)
    print()
    df.loc[len(df.index)] = [headline, summary, link]

df.to_csv('scrape.csv')