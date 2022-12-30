#In this program we will learn about the string sliceing
name='ankitsw'
print(type(name))
print(name[0:3])
print(name[:3])#give the same o/p bcz it assumes it to be 0
print(name[2:])#assumes it to the last place

# negitive indeices are also used in python
print(name[-4:-1])






#slicing the string with skip value

print("slicing using skip value")
print(name[::3])  #[start:end:value of jump]
