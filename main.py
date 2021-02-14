import re
import requests
from bs4 import BeautifulSoup

# patternObj = re.compile('^[https://]{1}[.]*[d-id]{1}$[\d]+')
site = './darkreading/darkreading13022021.html'
links = []

# website = requests.get('https://www.darkreading.com/attacks-breaches.asp')
with open(site, 'rb') as site_content:
    soup = BeautifulSoup(site_content, 'html.parser')

# for element in soup.find_all('a'):
#     href = element.get('href')
#     if 'd-id' in href and '#msgs' not in href and href not in links:
#         links.append(href)

for match in soup.find_all('a', href=re.compile('^https://{1}.*d-id{1}/{1}\d+$')):
    href = match.get('href')
    if href not in links:
        links.append(href)

for link in enumerate(links, start=1):
    print(f"{link[0]}. {link[1]}")
