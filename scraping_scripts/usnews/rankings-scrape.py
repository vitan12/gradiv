import requests
from bs4 import BeautifulSoup
import requests
import json
import re

rankings_list = {}
rankings_list['rankings'] = []

# Will add options to take in a variable URL based on what rankings to sort by
# i.e. By tuition/field/acceptance rate. 
url = 'https://www.usnews.com/best-graduate-schools/top-engineering-schools/eng-rankings'
colleges = []

# Apparently this is necessary for USNews to not outright deny you
agent = {"User-Agent":"Mozilla/5.0"}

r = requests.get(url, headers=agent)
soup = BeautifulSoup(r.text)

rank = soup.findAll('div', attrs={'class': 'ranklist-ranked-item RankList__Rank-f42a47-2 fTNmZK'})
uni = soup.findAll('a', attrs={'class': 'Anchor-u1fur6-0 chvEFD'})
location = soup.findAll('p', attrs={'class': 'Paragraph-fqygwe-0 bstttc'})
tuition = soup.findAll('p', attrs={'class': 'fqygwe-0-Paragraph-hHEPzZ gscYiA'})
college_page = soup.findAll('a', attrs={'href': 'Anchor-u1fur6-0 chvEFD'})

print (rank)

for n in range (len(rank)):
    rankings_list['rankings'].append({
            #'University Name': uni[n].get_text(),
            'Rank': rank[n].get_text(),
            #'Location': location[n].get_text(),
            'Tuition': tuition[n].get_text(),
            #'USNews Website': college_page[n].get_text()
        })


filename = open('rankings.json', 'w')
json.dump(rankings_list, filename)

print("Finished.")

