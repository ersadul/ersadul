# # Importing Flat Files From the Web ( 1 )
# from urllib.request import urlretrieve

# url = ' http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

# urlretrieve(url, 'winequality-white.csv')
# print(urlretrieve(url, 'winequality-white.csv')) # retrive as object


# # HTTP Requests to Import Files from Web ( 2 )
# send request using urllib package
# from urllib.request import urlopen, Request

# url = 'https://www.wikipedia.org/'

# request = Request(url)
# response = urlopen(request)
# html = response.read()
# response.close()

# print(html)

#send request using requests package
# import requests

# url = 'https://www.wikipedia.org/'

# r = requests.get(url)
# text = r.text

# print(text)


# # Scraping the Web in Python ( 3 )
# from bs4 import BeautifulSoup
# import requests

# url = "https://www.crummy.com/software/BeautifulSoup/"
# r = requests.get(url)
# html_doc = r.text
# soup = BeautifulSoup(html_doc, features='html.parser')

# scrape title website
# print(soup.title)

# scrape text inside the website
# print(soup.get_text())

# for link in soup.find_all('a'):
#     print(link.get('href'))


# # Introduction to APIs and JSONs ( 4 )
# extracting data from json 
# import json

# path = 'D:/learning and code/python/niomic/Importing Data In Python (Part 2)/snakes-on-plane.json'
# with open(path, 'r') as file:
#     data = json.load(file)

# for key, val in data.items():
#     print(key + ':', val)


# # APIs and Interacting with the World Wide Web (WWW) ( 5 )
import requests

url = 'http://www.omdbapi.com/?apikey=e4246b0c&t=The Father'
r = requests.get(url)
json_data = r.json()

for key, val in json_data.items():
    print(key + ':', val)