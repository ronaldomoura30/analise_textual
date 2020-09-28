# -*- coding: utf-8 -*-
import csv
import re
import nltk
import string
import unicodedata
import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")

new_file = csv.reader(open('base_teste.csv', 'r', encoding="utf8"))

list_docs = []

list_label = []

for row in new_file:
    print(row[2])

def remove_stopwords(text):
    regex = re.compile('[%s]' %re.escape(string.punctuation))

    a = []

    palavras = text.split()
    for palavra in palavras:
        token = regex.sub(u'', palavra)
        if not token == u'':
            a.append(token)