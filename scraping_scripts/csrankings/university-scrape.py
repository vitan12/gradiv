import requests
from bs4 import BeautifulSoup
import requests
import json
import re

rankings_list = {}
rankings_list['rankings'] = []

# Will add options to take in a variable URL based on what rankings to sort by
# i.e. By tuition/field/acceptance rate.
url = 'http://csrankings.org/#/index?all'
colleges = []

# Apparently this is necessary for USNews to not outright deny you
agent = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers=agent)
soup = BeautifulSoup(r.text)

rank = soup.findAll('td', attrs={'class': 'rank'})
uni = soup.findAll('td', attrs={'class': 'name'})

print (len(uni))

for n in range (len(uni)):
    rankings_list['rankings'].append({
            'University Name': uni[n].get_text(),
            'Rank': rank[n].get_text(),
        })


filename = open('rankings.json', 'w')
json.dump(rankings_list, filename)

print("Finished.")
