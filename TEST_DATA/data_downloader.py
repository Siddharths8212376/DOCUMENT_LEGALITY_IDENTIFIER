import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd 
import csv

with open('legal_file_names.csv', mode='w') as file_names:
    name_writer = csv.writer(file_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    name_writer.writerow(['FILE_NAMES'])
    
df_links = pd.read_csv('document_links.csv')
links_list = df_links['LINKS']
# print(list(links_list))
for each_link in list(links_list)[1001:1500]:
    web_page = requests.get(each_link)
    contents = web_page.content
    soup = BeautifulSoup(contents, 'html.parser')
    # print(soup.prettify())
    download_button = soup.find('button', {'class': 'btn btn-small dropdown-toggle'})
    download_list = soup.find('ul', {'class': 'pull-right dropdown-menu dropdown-right'})
    doc = download_list.find_all('a', {'rel':'nofollow'})
    # print(doc[1]['href'])
    href = doc[1]['href']
    # print(href)
    name = each_link.split('/')[-1] + '.doc'
    print(name)
    # name = href.split('/')[-1]
    # print(name)
    link = 'https://www.docracy.com' + href
    # declare the web_driver for scraping purposes
    # driver = webdriver.Chrome(executable_path=r'C:\Users\Siddharth\chromedriver.exe')
    # driver.get()
    # print('Beginning file download with urllib...')
    urllib.request.urlretrieve(link, 'D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\LEGAL_DOCUMENTS\\' + name )
    # file = requests.get(link)
    # print(file.content)
    with open('legal_file_names.csv', mode='a') as file_names:
        name_writer = csv.writer(file_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        name_writer.writerow([name])