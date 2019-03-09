from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# x = "http://www.wikipedia.org"
x = "http://www.wallpaperscraft.com"
# x = "https://unsplash.com/search/photos/wallpaper"
# x = "https://unsplash.com/search/photos/wallpaper"
# x = "https://www.facebook.com"
# x = "https://wallpaperscraft.com/wallpaper/bubbles_circles_dark_136091"
# x = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-750744.jpg"

hdr = {'User-Agent': 'Chrome/72.0 (Windows NT 10) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = Request(x, headers=hdr)
webpage = urlopen(req).read()


# req = Request(x, headers={'User-Agent': 'Mozilla/5.0'})
#
# html_page = urlopen(req)

soup = BeautifulSoup(webpage, "html.parser")

datalist = []
urllist = []

for link in soup.findAll('a'):
    datalist.append(link.get('href'))

print(datalist)

for i in range(len(datalist)):
    a = x + datalist[i][1:]
    urllist.append(a)

print(urllist)
