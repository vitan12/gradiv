# scrapes data from thegradcafe.com
import requests
import json

from bs4 import BeautifulSoup

req_url = 'https://www.thegradcafe.com/survey/index.php?q='
# in the future, allow script to feed in requested parameters to gradcafe
# for now I'm leaving this part as is to test the scraping successfully
university = 'Princeton+University'

response = requests.get(req_url + university)
html = response.content
grad_soup = BeautifulSoup(html, "html.parser")

grad_json = {}
grad_json['posts'] = []

uni = grad_soup.find_all('td', attrs={'class': 'tcol1'})
type = grad_soup.find_all('td', attrs={'class': 'tcol2'})
decision = grad_soup.find_all('td', attrs={'class': 'tcol3'})
app_type = grad_soup.find_all('td', attrs={'class': 'tcol4'})
dates = grad_soup.find_all('td', attrs={'class': 'tcol5'})
comment = grad_soup.find_all('td', attrs={'class': 'tcol6'})

for index in range(len(dates)):
	grad_json['posts'].append(
	{
		'institution': uni[index].get_text(),
		'program': type[index].get_text(),
		'result': decision[index].get_text(),
		'applicant_type': app_type[index].get_text(),
		'date': dates[index].get_text(),
		'comments': comment[index].get_text()
	}
	)

with open('gradcafe.json', 'w') as outfile:
	json.dump(grad_json, outfile)

print("done!")
