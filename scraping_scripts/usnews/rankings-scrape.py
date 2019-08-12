import requests
from bs4 import BeautifulSoup
import requests
import json
import re

rankings_list = {}
rankings_list['rankings'] = []

# Will add options to take in a variable URL based on what rankings to sort by
# i.e. By tuition/field/acceptance rate. 
url = 'https://www.usnews.com/best-graduate-schools/top-engineering-schools/eng-rankings?_mode=table'
colleges = []

# Apparently this is necessary for USNews to not outright deny you
agent = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers=agent)
soup = BeautifulSoup(r.text)

regex = '<a class="school-name" href="/best-colleges/(.+?)">[^.]*</a>'
pattern = re.compile(regex)

rank = soup.findAll('span', attrs={'class': 'ranklist-ranked-item RankList__Rank'})
uni = soup.findAll('a', attrs={'class': 'school-name'})
location = soup.findAll('p', attrs={'class': 'location'})
tuition = soup.findAll('span', attrs={'class': 'TuitionandFees'})
college_page = soup.findAll(pattern, soup)

print (uni)

for n in range (len(rank)):
    rankings_list['rankings'].append({
            'University': uni[n].get_text()
        })


filename = open('rankings.json', 'w')
json.dump(rankings_list, filename)

print("Finished.")

