import json,csv,pandas
myfile="petrol.csv"
mjson="petrol.json"
petrollist=[]
with open(myfile,'r',encoding='utf-8') as f:
    datareader=csv.DictReader(f)
    for data in datareader:
        petrollist.append(data)
petrol_list_json=json.dumps(petrollist)
with open(mjson,'w+',encoding='utf-8') as f:
    f.write(petrol_list_json)
