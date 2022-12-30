def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

num = 5
print("The factorial of", num, "is", fact(num))
