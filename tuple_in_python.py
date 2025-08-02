#tuple:ordered,immutable,allows duplicate element
# mytuple=("ram",1,True)
# myt=("ram",)
# print(type(myt))

# mytuple=tuple(["ram",1,True])
# mytuple[0]="shyam" #will not support bcs tuple is immutable
# print(mytuple)

# mytuple=('a','b','b','x')
# print(mytuple.count('b'))#count a letter occuring
# print(mytuple.index('x'))

# mytuple=('a','b','b','x')
# my_list=list(mytuple)#convert in list
# mytuple2=tuple(my_list)#convert in tuple

#unpacking
# mytuple=("ram",28,"Ayodhaya")
# mytuple="ram",28,"Ayodhaya"
# name,age,city=mytuple
# print(name,age,city)

# mytuple=(0,1,2,3,4)
# a,*b,c=mytuple
# print(a)
# print(b)#will be a list
# print(c)


#byte comparision of list and tuple(conclusion:tuple more effective then list w.r.t size)
# import sys
# mylist=[1,2,3,"s",True]
# mytuple=(1,2,3,"s",True)
# print(sys.getsizeof(mylist),"list size in bytes")
# print(sys.getsizeof(mytuple),"tuple size in bytes")

#timeit comparision (working with tuple is more efficient then list)
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000))#more efficent way to do it
