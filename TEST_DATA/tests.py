import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

web_page = requests.get("https://www.docracy.com/0rgkbvacolg/independent-contractor-agreement-template")
contents = web_page.content
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
download_button = soup.find('button', {'class': 'btn btn-small dropdown-toggle'})
download_list = soup.find('ul', {'class': 'pull-right dropdown-menu dropdown-right'})
doc = download_list.find_all('a', {'rel':'nofollow'})
# print(doc[1]['href'])
href = doc[1]['href']
print(href)
name = href.split('/')[-1]
print(name)
link = 'https://www.docracy.com' + href
# declare the web_driver for scraping purposes
# driver = webdriver.Chrome(executable_path=r'C:\Users\Siddharth\chromedriver.exe')
# driver.get()
print('Beginning file download with urllib...')
urllib.request.urlretrieve(link, 'D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\' + name )
# file = requests.get(link)
# print(file.content)
