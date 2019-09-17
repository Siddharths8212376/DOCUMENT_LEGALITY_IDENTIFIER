# import all the required libraries
import requests
from bs4 import BeautifulSoup
import urllib.request
import csv
# scrape the website
# docracy.com: An opensource website for legal document formats
# link : https://www.docracy.com/doc/showall?sortBy=4&page=1

# each page contains 50 documents, we'll click on each of those
# download them and add those to a folder
page_range = [x for x in range(1, 21)]

# with open('document_links.csv', mode='w') as doc_links_file:
#     link_writer = csv.writer(doc_links_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     link_writer.writerow(['LINKS'])
# print(page_range)
# initial_web_page = requests.get("https://www.docracy.com/doc/showall?sortBy=4&page=1")
for each_num in range(21, 31):
    # each_num = 1
    web_page = requests.get("https://www.docracy.com/doc/showall?sortBy=4&page=" + str(each_num))
    contents = web_page.content
    soup = BeautifulSoup(contents, 'html.parser')
    # print(soup.prettify())
    # find all the anchor tags and their hyperlinks
    doc_link_set = []
    # div_contents = soup.find('div', {'class': 'container'})
    document_set = soup.find_all('div', {'class': 'row'})
    # we see that all but 1 elements in div with class: row are documents
    for each_document in document_set[1:-2]:
        doc_anchor = each_document.find_all('a')[1]
        doc_href = doc_anchor['href']
        doc_link = 'https://www.docracy.com' + doc_href
        doc_landing_page = requests.get(doc_link)
        doc_link_set.append(doc_link)
        # print(doc_link)
    # print(doc_link_set, len(doc_link_set))
    # with open('document_links.txt', mode='w') as doc_links_file:
    #     for each_link in doc_link_set:
    #         doc_links_file.write(each_link + "\n")

    with open('document_links.csv', mode='a') as doc_links_file:
        link_writer = csv.writer(doc_links_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for each_link in doc_link_set:
            link_writer.writerow([each_link])
