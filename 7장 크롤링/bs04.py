import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.naver.com'
html = urllib.request.urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

#li = bs.find_all("li", {'class':'nav_item'})
li = bs.find_all('a',  {'class':'nav'})
#li2 = li.find_all('a',  {'class':'nav'})
for ele in li:
    print(ele.text)


