import random


name=input("Enter your name : ")
print("Welcome ",name)
print("You have to guess no between 1 to 20")
s=0
for i in range(6):
    cn=random.randint(1,20)
    un=int(input("Enter the value you guess!!"))
    print("The random no is :",cn)
    if(cn<un):
        print("Guess is Bigger!  score =",s)
    elif(cn>un):
        print("Guess is Smaller!  score =",s) 
    elif(cn==un):
        s=s+5
        print("Perfect Guess !  score =",s)  
print('''

      Thanks for palying
      Your final score is : ''',s)