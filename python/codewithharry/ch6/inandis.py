#it this program we will learn about in and is   
a=input("Enter the 1 no :")
b=input("Enter the 2 no :")
c=input("Enter the 3 no :")
d=input("Enter the 4 no :")
if(a>b and a>c and a>d):
    print(a,"is the biggest of all ")
elif(b>a and b>c and b>d):
    print(b,"is the biggest of all ")
elif(c>a and c>b and c>d):
    print(c,"is the biggest of all ")
elif(d>a and d>c and d>b):
    print(d,"is the biggest of all ")
else:
    print("no comaparision")