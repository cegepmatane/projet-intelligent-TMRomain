from bs4 import BeautifulSoup
import re
# import urllib2

url = "snake.html"
page = open(url)
soup = BeautifulSoup(page.read())

cities = soup.find_all('p', {'id' : 'score'})

for city in cities:
    print(city)