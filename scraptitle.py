import requests
from bs4 import BeautifulSoup
import csv
   
URL = "https://www.espncricinfo.com/team"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html.parser')
res = soup.title
print(res.text)
   
