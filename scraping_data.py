#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:01:19 2018

@author: jessicasaini
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.4icu.org/in/indian-universities.htm")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print(df[0])
df[0].to_csv("university.csv", sep='\t', encoding='utf-8')
