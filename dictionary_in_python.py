#Dictionary:key-Value pair,Unordered,Mutable
# mydict={"name":"ram","age":45,"city":"ayodhaya"}
# mydict["email"]="xyz#gmail.com"
# print(mydict)

# mydict2=dict(name="ram",age=27,city="Ayodhaya")
# print(mydict2)

# value=mydict["name"]
# print(value)

# del mydict["name"] #delete the name key
# removed_age_data=mydict.pop("age")#remove age key avlue and return the corresponding value of the key
# mydict.popitem()#remove last item
# print(mydict)


#try catch
# try:
#     print(mydict["lastname"])
# except:
#     print("error")


#key in dictionary
# for key in mydict:
#     print(key)

# for a in mydict.keys(): #mydict.keys()--> get all the key of the list
#     print(a)

#get key value together
# for key,value in mydict.items():
#     print(key,value)

#copy dictionary to another variable
# mydict_cpy=mydict.copy()#copy dictionary
# mydict_cpy=dict(mydict)#copy dictionary
# mydict_cpy["role"]="xyz"
# print(mydict_cpy)


#update method in python #overide the existing key
# mydict={"name":"Max","age":27,"email":"xyz@gmail.com"}
# mydict2=dict(name="Ram",age=1000,city="Ayodhaya")
# mydict.update(mydict2);
# print(mydict)

# mydict={3:4,4:16,6:36,7:49}
# print(mydict[3])

#using tuple as key
mytuple=(8,7)
mydict={mytuple:15}
print(mydict)