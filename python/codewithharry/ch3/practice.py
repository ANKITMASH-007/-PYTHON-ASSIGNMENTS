# practice question 


#good afternoon
print("greeting a person")
greet= "Good afternoon,"
name=input("enter the name")
print(greet+name) 

#letter template
print("letter template")
letter=''' Dear <|name|>
  You are selected!
  <|date|>'''
name=input("Enter the name")
date=input("Enter the date ")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)


