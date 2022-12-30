my_num = int(input("Enter a number.. "))
my_dict = dict()

for elem in range(1,my_num+1):
   my_dict[elem] = elem*elem
print("The generated elements of the dictionary are : ")
print(my_dict)