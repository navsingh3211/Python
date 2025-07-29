#lists: ordered,mutable,allows duplicate elements
# mylist=["ram1",1,True]

# mylist[-1] #last item from array

# print(mylist[2])

# print(len(mylist))

# mylist.append("Shayam") #insert element at last
# print(mylist)

# mylist.insert(1,"data") #insert element at specific position
# print(mylist)

# popedItem = mylist.pop()#remove the last item from list
# print(popedItem)

# item = mylist.remove("ram1")#remove specific element
# print(mylist)

# mylist.clear()#empty the list
# print(mylist)

# for i in mylist: #loop the list
#     print(i);

# if "ram" in mylist:
#     print("yes")
# else:
#     print("No")


# mylist.reverse()
# mylist=mylist[::-1]#reverse the list

# mylist =[4,-1,3,-5,10,0]
# mylist.sort() #sort the entire list

# data = sorted(mylist) #get sorted listbut actual list(mylist) will not be sorted in heap
# print(mylist)
# print(data)



# mylist=[0]*5
# mylist2=[1,2,3]
# new_list  = mylist+mylist2; #concate two list directly
# print(new_list)

#slicing
# mylist=[1,2,3,4,5,6,7,8]
# a=mylist[1:5] #from[start:end]
# a=mylist[:5] #start from begining
# a=mylist[1:] #from start index to last
# a=mylist[::2] # 2 step
# a=mylist[::-1]#reverse the list

#copying a list
# mylist=[1,2,3,4,5,6,7,8]
# new_list=mylist.copy()#make actual copy
# new_list=list(mylist)#make actual copy
# new_list=mylist[:]#make actual copy
# new_list.pop()
# print(new_list)
# print(mylist)#original list not get impact but when we do copy by new_list=mylist then original lsit get impact

#copy by list comprehension
mylist=[1,2,3,4,5,6,7,8]
b=[i*i for i in mylist]
print(mylist)
print(b)
