import csv
import json
myfile='F:\day13\student.csv'
jsonfilepath='student.json'
student_list=[]
# converting csv to list
with open(myfile,'r',encoding='utf-8') as f:
    datareader=csv.reader(f)
    #print(datareader)
    for data in datareader:
        student_list.append(data)
#convert list to json
student_list_json=json.dumps(student_list)
with open(jsonfilepath,'w+',encoding='utf-8') as f:
    f.write(student_list_json)
    