# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?


import json
dict={}
file="text.txt"
with open(file) as file7:
    for i in file7:
        command,discription=i.strip().split(None,1)
        dict[command]=discription.strip()
out_file=open("text1.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()