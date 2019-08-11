# scrapes data from thegradcafe.com
import requests

from bs4 import BeautifulSoup

req_url = 'https://www.thegradcafe.com/survey/index.php?q='
# in the future, allow script to feed in requested parameters to gradcafe
# for now I'm leaving this part as is to test the scraping successfully
university = 'Princeton+University'

response = requests.get(req_url + university)
html = response.content
grad_soup = BeautifulSoup(html, "html.parser")

print(len(grad_soup.find_all('td', attrs={'class':'tcol5'})))
