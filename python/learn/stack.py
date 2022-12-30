l=[]
while True:
    n=int(input('''
       1 push 
       2 pop 
       3 peek 
       4 display
       5 exit
    '''))
    
    if n==1:
        a=input("Enter the value")
        l.append(a)
        print(l)
    elif n==2:
        if (len(l)==0):
            print("The stack is empty!")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif n==3:
        print(l[-1])
    elif n==4:
        print(l)
    elif n==5:
        break
    else:
        print("Invalid Operation ")
        break      