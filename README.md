# Custom-NER-Spacy
To build custom NER using Space library in Python and implement pseudorehersal techniques. The natural entity recognisers built are used to recognise universities, cgpa and degrees.

## Scraping the Data
a) The data is scraped from the website "https://www.4icu.org/in/indian-universities.htm". the code for scraping the data is given in the file scraping_data.py
b) After the data is scraped, a new csv file with the name university.csv is generated.
Similarly, the data can be scraped for different degrees also. 

## Creating dataset
A few guidelines have to be kept in mind when creating high-quality datasets for training.
a) The columns should be of the format Name, Sentence and Length
b) The sentence length should be of 80-300 words.
c) For more information, please check the document for creating dataset.
