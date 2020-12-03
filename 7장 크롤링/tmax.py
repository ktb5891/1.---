from selenium import webdriver
import time 
from bs4 import BeautifulSoup
import requests
import urllib.request


driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://115.85.183.228:8081/')

time.sleep(0.5)

driver.find_element_by_name('Email').send_keys('tmax11@tmax.co.kr')

time.sleep(0.5)

driver.find_element_by_name('password').send_keys('tmax')

time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="kt_login_v2"]/div[2]/div/div[1]/div/form/div[3]/button').click()

time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="kt_login_v2"]/div[2]/div[1]/div/div[2]/div[1]/ul/li/a').click()

time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="kt_table_1_wrapper"]/div[2]/div/table/tbody/tr[1]/td[9]/button').click()

time.sleep(1)

url = driver.current_url
print(url)
soup = BeautifulSoup(requests.get(url).content, "html.parser")
print(soup)
list_title = []
for news_title in soup.find_all("div", class_="word _utterance"): 
    list_title.append(news_title.get_text())

print(list_title)
#response = urllib.request.urlopen(url)
#soupData = BeautifulSoup(response, 'html.parser')
# source = requests.get(url).text
# print(source)
# soupData = BeautifulSoup(source, 'html.parser')

# spans = soupData.select("div.word_utterance")

