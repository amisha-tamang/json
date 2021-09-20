# Q8.Tumhare pass four employes ki details hai list mai:- ab aapko 4 dictionaries create karni hai 
# jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,
# age and salary honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. 
# Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai. Output:-




import json

list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
emp1={}
emp2={}
emp3={}
emp4={}
key=["name"," Designation","age","salary"]
dict={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
for i in range(len(list1)):
    emp1.update({key[i]:list1[i]})
    emp2.update({key[i]:list2[i]})
    emp3.update({key[i]:list3[i]})
    emp4.update({key[i]:list4[i]})
with open("new_file.json","w") as file8:
    json.dump(dict,file8,indent=5)




