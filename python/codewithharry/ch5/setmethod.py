#this program is to learn about set method

a=set()

#ADD
a.add(10)
a.add(101)
a.add(10)
a.add(1000)
a.add((3,4,5)) #tuples can be added to a set but not list and dictionary
print(a)



#LEN
print(len(a)) 
#prints the length of the set

#REMOVE
a.remove(1000)
print(a)
#this method removes the given value from the set

#POP
print(a)
print(a.pop())
print(a)
#removes any arbitary value from the set 



#CLEAR

a.clear()
print(a)
#clears all the values of the set 

#UNION
a.union({101,102})
