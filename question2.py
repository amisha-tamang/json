# Python object ko json data main convert karne ka program likho? 


import json
dict={"name": "David", "class":"I", "age": 6}
with open("type.json","w") as file:
    json.dump(dict,file,indent=4)
    # print(dict)

