# this is to perform a union operation on the folowing two sets

print("this is a example of a set unioin !!!!")
A={1,2,3,4,5,6,21,23}
B={5,6,7,8}
print(A|B)
print(A.union(B))


#this is to perform set intersection

print("This is the set intersection")
print(A&B)
inter=A.intersection(B)
print(type(inter))
print(inter)



# this is to perform set diffrence
print("This is the set diffrence")
print(A-B)
print(A.difference(B))
print(B-A)
print(B.difference(A))

# this is to peroform  symetric diffrence 
print("This is the symmetric diffrence")
print(A^B)
print(A.symmetric_difference(B))



