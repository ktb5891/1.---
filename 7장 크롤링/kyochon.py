import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 
from itertools import count 
from Get_URL import get_request_url

result = []
#for pageNum in count():

url = 'http://www.kyochon.com/shop/domestic.asp?sido1=1&sido2=1&txtsearch='
#response = urllib.request.urlopen(url)
#soupData = BeautifulSoup(response, 'html.parser')
rcv_data = get_request_url(url)
soupData = BeautifulSoup(rcv_data, 'html.parser')
spans = soupData.findAll('span', {'class':"store_item"})
for span in spans:
    span = list(span.strings)
    store = span[1]
    address = span[3].strip()
    sido_gungu = address.split()[:2]
    phone = span[5].strip()
    print([store] +sido_gungu+[address]+[phone])
    