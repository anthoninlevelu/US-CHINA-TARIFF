import pandas as pd
import numpy as np
import os
import re
import locale
import nltk
import operator
import glob

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import SnowballStemmer
from string import digits, punctuation

#QUESTION 5.a
os.chdir('/Users/applemacintosh/Documents/Kiel Institute ASP 2020-2021 - Anthonin Levelu/Research Assistance/US-China/US_Tariff')

Exclusions = glob.glob('/Users/applemacintosh/Documents/Kiel Institute ASP 2020-2021 - Anthonin Levelu/Research Assistance/US-China/US_Tariff/*.rtf')
List_of_exclusions = []

for file in Exclusions:
    with open(file) as file1:
        file1 = file1.read()
        print(file1)
        file1 = re.findall('\d{4}[.]\d{2}[.]\d{4}', file1)
        List_of_exclusions.append(file1)

List_of_exclusions = pd.DataFrame(List_of_exclusions)
List_of_exclusions = List_of_exclusions.T
List_of_exclusions.to_excel("List_of_exclusions_regex.xlsx")



