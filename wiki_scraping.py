import sys
import visualization
import util

# Checks if optional URL argument has been passed in
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = 'https://en.wikipedia.org/wiki/United_States'

soup = util.get_soup_from_url(url)

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

# Removes empty strings before visualizing
for x in soup.find_all():
    if len(x.get_text().strip()) == 0:
        x.decompose()

paragraphs = soup.find_all('p')

sorted_dict = util.get_sorted_dict(paragraphs)

df = util.get_panda(sorted_dict)
visualization.bar_plot(df, url)
