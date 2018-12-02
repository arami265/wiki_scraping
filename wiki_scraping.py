import requests
from bs4 import BeautifulSoup
import visualization
import util

page = requests.get('https://en.wikipedia.org/wiki/United_States')

soup = BeautifulSoup(page.content.decode('utf8', 'ignore'), 'html.parser')

listen = soup.find('small')
references = soup.find_all('sup', {'class': 'reference'})
table = soup.find('table', {'class': 'infobox'})
stub = soup.find('span', {'id': 'coordinates'})

if listen is not None:
    listen.decompose()

if references is not None:
    for r in references:
        r.decompose()

if table is not None:
    table.decompose()

if stub is not None:
    stub.decompose()

for x in soup.find_all():
    if len(x.get_text().strip()) == 0:
        x.decompose()

paragraphs = soup.find_all('p')

sorted_dict = util.get_sorted_dict(paragraphs)

df = util.get_panda(sorted_dict)
visualization.bar_plot(df)
