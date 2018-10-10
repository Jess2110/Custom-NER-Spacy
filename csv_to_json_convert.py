#Degree_Dataset.csv
#University_dataset.csv
#CGPA_Dataset.csv
import csv, json
import os 
dir_path = os.getcwd()
print(dir_path)
csvpath=dir_path+"/"+ input("Enter the name of the file")
csvfile = open(csvpath, 'r')
csv_reader=csv.reader(csvfile)
out_path="Enter the output path here"
jsonpath=out_path+input("enter the name of json file")
jsonfile = open(jsonpath, 'w')
jsonlist=[]
reader = csv.DictReader(csvfile)
for row in reader:
    jsonlist.append(row)
    #json.dump(row, jsonfile)
json.dump(jsonlist, jsonfile)    
jsonfile.close()
print("The file is present in"+ dir_path)

