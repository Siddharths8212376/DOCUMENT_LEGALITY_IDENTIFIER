# parsing out the set of most commonly used
# english words, we're taking the 3000 most commonly used words
# source-link : https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/

# making it a reference for prediction of our model
# importing the required libraries
import requests
from bs4 import BeautifulSoup
import csv

web_page = requests.get("https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/")
# parse out all the contents
contents = web_page.content
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
word_div = soup.find('div', {'class': 'field-item even'})
set_paragraphs = word_div.find_all('p')
all_words = set_paragraphs[1]
# print(type(all_words.text))
# print(all_words.text)
# with open('test_words.txt', mode='w') as test_file:
#     test_file.write(all_words.text)

set_of_words = all_words.text.split()
# print(set_of_words)
# the given list of words is clean and consistent data
# so we'll just directly add it to a csv file
with open("most_common_words.csv", mode='w') as common_words:
    common_writer = csv.writer(common_words, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    common_writer.writerow(['COMMON WORDS'])
    for word in set_of_words:
        common_writer.writerow([word])
    
