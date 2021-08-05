import json
studentlist=[{"name":"renuka","rollno":476},{"name":"dharu","rollno":477}]
print(studentlist)
myjson=json.dumps(studentlist)
with open('test.json','w',encoding='UTF-8') as f:
    f.write(myjson)
