# a legal data collection module using the python requests library

# import all the required libraries
import requests
from bs4 import BeautifulSoup
import re


# next step is to load the webpage in Python
# loading the Legal Terms Dictionary - State of Connecticut branch
web_page = requests.get("https://www.jud.ct.gov/legalterms.htm")


# getting all the contents
contents = web_page.content
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())


words_and_meanings = {}
all_paragraphs = soup.find_all('p', {'class': 'text'})
all_strong_words = []
all_corr_meanings = []
for each_paragraph in all_paragraphs:
    strong_words = each_paragraph.find('strong')
    words_meanings = each_paragraph.text.split(": ", 1)
    if strong_words is not None:
        all_strong_words.append(strong_words.text)
        all_corr_meanings.append(words_meanings)
# print(len(all_strong_words))
# print(all_corr_meanings)
# print(all_strong_words)


# # match_pattern = re.compile(r'')
# # we're using raw string to match the words
# for word in all_strong_words:
#     text = word.text
#     if len(text) > 1:
#         pattern = re.compile(r'[^\|0]')
#         if re.match(pattern, text) is not None:
#             legal_terms.append(word.text)
# print(legal_terms, "\n", len(legal_terms))

# now it's time to clean up the data
# we'll have to remove the \r\n\t, and escape sequences as such
unclean_terms = all_strong_words
legal_terms = []
for each_term in unclean_terms:
    removal_terms = ["\n", "\t", "\r", ":"]
    for term in removal_terms:
        if term in each_term:
            each_term = each_term.replace(term, "")
    if each_term != "A":
        legal_terms.append(each_term.strip())
        # stripping for removing all the leading and trailing spaces
    
# print(legal_terms, "\n", len(legal_terms))

# # add all the data into a csv file
import csv

# with open("legal_terms.csv", mode='w') as legal_terms_file:
#     legal_writer = csv.writer(legal_terms_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     legal_writer.writerow(['LEGAL_TERMS'])
#     for each_term in legal_terms:
#         legal_writer.writerow([each_term])

# for each_term, index in enumerate(legal_terms):
#     for each_set in all_corr_meanings:
#         if each_term in all_corr_meanings:
#             print(all_corr_meanings[index][1])

# we've got 303 legal terms from the legal terms dictionary successfully :)

meanings = []
for each_word_meaning in all_corr_meanings:
    if len(each_word_meaning) > 1:
        meanings.append(each_word_meaning[1])
        
# for meaning in meanings:
#     print(meaning)
with open('partial_definitions.txt', mode='w') as partial_def_file:
    def_writer = csv.writer(partial_def_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    def_writer.writerow(['Definitions '])
    for meaning in meanings:
        def_writer.writerow([meaning])
    