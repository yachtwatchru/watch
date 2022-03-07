import requests
from bs4 import BeautifulSoup, SoupStrainer

url="https://www.vesselfinder.com/de/vessels/DILBAR-IMO-9661792-MMSI-319094900"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print("scrape of page %s results in HTTP %s" % (url,page.status_code))

soup = BeautifulSoup(page.text, "lxml")

# extract coordinates
coords = soup.find('div', {'class': 'mmlpc'})
flx = coords.find('div', {'class': 'flx'})
lon = flx.find('div', {'class': 'coordinate lon'}).text
lat = flx.find('div', {'class': 'coordinate lat'}).text

# extract date
time = soup.find("td", {"id": "lastrep"})['data-title']

# extract name
header = soup.find('div', {'class': 'page-header'})
name = header.find('h1', {'class': 'title'}).text


print("last Position of %s was LON: %s Lat: %s at %s" % (name,lon,lat, time))

# write to file
file_object = open('history.csv', 'a')
file_object.write("%s;%s;%s;%s\n" % (name,lon,lat, time))
file_object.close()
