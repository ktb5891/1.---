import bs4
#from bs4 import BeautifulSoup
htm_str = "<html><div>hello</div></html>"
result = bs4.BeautifulSoup(htm_str, 'html.parser')

print(result.find('div').text)