import requests
from bs4 import BeautifulSoup

website = requests.get('https://www.darkreading.com/attacks-breaches.asp')
soup = BeautifulSoup(website.content, 'html.parser')

print(soup.prettify())