l=[]
while True:
    n=int(input('''
       1 Enqueue 
       2 Dequeue (first)
       3 First 
       4 Rear
       5 Display
       6 Exit
    '''))
    
    if n==1:
        a=input("Enter the value")
        l.append(a)
        print(l)
    elif n==2:
        if (len(l)==0):
            print("The queue is empty!")
        else:
            print(l[0])
            del l[0]
            print(l)
    elif n==3:
        print(l[0])
    elif n==4:
        print(l[-1])
    elif n==5:
        print(l)
    else:
        print("Invalid Operation ")
        break      