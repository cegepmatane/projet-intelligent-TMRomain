from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chrome.exe", chrome_options=options)
url = "https://www.tutorialspoint.com/index.htm"
driver.get(url)