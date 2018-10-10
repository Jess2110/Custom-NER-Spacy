#FileNames
#University_dataset.json
#Degree_Dataset.json
#CGPA_Dataset.json

import re
import sys
import json
import pickle
import os 
dir_path = os.getcwd()
print(dir_path)
diction = dict()
dict_ner=list()
name_of_file=input("Enter the file name")
filename = dir_path+"/"+name_of_file
job_titles_cleaned = json.load(open(filename, 'r'))
json_filename = job_titles_cleaned

if(name_of_file=="University_dataset.json"):
    for i in range(len(json_filename)):
        a=json_filename[i]['University']
        b=json_filename[i]['Sentence']
        print(a,b)
        start_index = re.search(a.lower(), b.lower())
        if start_index:
            start_string=start_index.group(0)
            start_index,end_index=start_index.span()
            diction['entities'] = [(start_index,end_index,'UNIVERSITY')]
            dict_ner.append((json_filename[i]['University'],diction.copy()))
        else:
            print("ERROR!!")
    print(dict_ner)
if(name_of_file=="Degree_Dataset.json"):
    for i in range(len(json_filename)):
        a=json_filename[i]['Degree']
        b=json_filename[i]['Sentence']
        print(a,b)
        start_index=b.find(a)
        end_index=start_index+len(a)
        if (start_index!=-1):
            diction['entities'] = [(start_index,end_index,'DEGREE')]
            dict_ner.append((json_filename[i]['Degree'],diction.copy()))
        else:
            print("ERROR!!")
    print(dict_ner)

if(name_of_file=="CGPA_Dataset.json"):
    for i in range(len(json_filename)):
        a=json_filename[i]["CGPA"]
        b=json_filename[i]["Sentence"]
        print(a,b)
        start_index=b.find(a)
        end_index=start_index+len(a)
        if (start_index!=-1):
            diction['entities'] = [(start_index,end_index,'CGPA')]
            dict_ner.append((json_filename[i]['Sentence'],diction.copy()))
        else:
            print("ERROR!!")
    print(dict_ner)

picklisedfile=name_of_file+"_pickl.txt"
with open(picklisedfile, 'wb') as fp:
    pickle.dump(dict_ner, fp)
print("Picklised file is created in the directory"+ dir_path)

