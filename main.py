import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/elaine-zheng/summer2020internships"
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table') # find only the stuff inside the html element table

#------------------------------------------------
# Part 1: scraping with BS4
# we noticed everything is in a thead tag.. so
columns = []
table_headers = table.find('thead')
table_header = table_headers.find_all('tr')

for tr in table_header:
    th = tr.find_all('th') # will find ever th in this row
    row = [i.text for i in th]
    row.append("Applied?")
    columns = row

jobs = []
table_body = table.find('tbody')
table_rows = table_body.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td') # will find ever th in this row
    row = [i.text for i in td]
    row.append("")
    jobs.append(row)

#------------------------------------------------
# Part 2: Using the dataframe
# writing the code to a file
df = pd.DataFrame(jobs)
df.columns = columns

df.to_csv('jobs.csv')

# could make a twitter bot?