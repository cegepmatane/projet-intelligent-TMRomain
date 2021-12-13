from bs4 import BeautifulSoup
from urllib import request
my_HTML = request.urlopen("http://localhost:8000/snake.html")

soup = BeautifulSoup(my_HTML, 'html.parser')
info = soup.find("p", {"id": "score"})
print(info)