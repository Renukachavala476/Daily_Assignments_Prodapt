import json,csv,pandas
myfile="diesel.csv"
mjson="diesel.json"
diesellist=[]
with open(myfile,'r',encoding='utf-8') as f:
    datareader=csv.reader(f)
    for data in datareader:
        diesellist.append(data)
diesel_list_json=json.dumps(diesellist)
with open(mjson,'w',encoding='utf-8') as f:
    f.write(diesel_list_json)


