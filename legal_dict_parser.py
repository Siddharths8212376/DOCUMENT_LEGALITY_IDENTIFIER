# a legal dictionary parser module using python requests library
# parsing the words and definitions from 
# Law.com legal dictionary
# link : https://dictionary.law.com/Default.aspx?letter=A

# we need to change the web_page for each alphabet 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# open the file for writing the first row for assigning column names
# further inside the loop we'll append to the file
# import csv libarary
import csv

with open("complete_legal_dictionary.csv", mode='w') as legal_dictionary:
    legal_writer = csv.writer(legal_dictionary, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    legal_writer.writerow(['TERMS', 'MEANINGS'])

# importing all the required libraries
import requests
from bs4 import BeautifulSoup
import re

# for each letter in alphabets, scrape the website for all the words
# and add them to a csv file

# now we'll implement the complele dictionary, at least I hope so

for each_letter in alphabets:
    web_page = requests.get("https://dictionary.law.com/Default.aspx?letter=" + each_letter)

    # get all the contents
    contents = web_page.content
    soup = BeautifulSoup(contents, 'html.parser')
    # print(soup.prettify())

    # now parsing the contents we need, ie, words and definitions
    all_words = soup.find_all('span', {'class': 'word'})
    all_meanings = soup.find_all('span', {'class': 'definition'})
    # print(len(all_words), " ", len(all_meanings))
    words_meanings = {}
    for word, meaning in zip(all_words, all_meanings):
        word_val = word.a.text
        meaning_val = meaning.text
        del_vals = ["\r", "\n", "\t"]
        for val in del_vals:
            if val in word_val:
                word_val = word_val.replace(val, "")
            if val in meaning_val:
                meaning_val = meaning_val.replace(val, "")
        word_val = word_val.strip()
        meaning_val = meaning_val.strip()
        words_meanings[word_val] = meaning_val
    # there are 209 legal terms starting with A 
    # print(words_meanings)
    # for word in words_meanings:
    #     print(word + " : " + words_meanings[word])

    # add it to a csv file in append mode

    with open("complete_legal_dictionary.csv", mode='a') as legal_dictionary:
        legal_writer = csv.writer(legal_dictionary, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for each_word in words_meanings:
            legal_writer.writerow([each_word, words_meanings[each_word]])

