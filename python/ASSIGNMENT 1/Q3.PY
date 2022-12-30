num = int(input("enter your number = "))
count = 0
while num != 0:
    num //= 10
    count = count + 1
print("total number of digits you entered : " + str(count))