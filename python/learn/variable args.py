def mul(*num):
    prod = 1

    for i in num:
        prod = prod * i

    print("Product:",prod)

mul(3,3)
mul(1,2,4)
mul(2,2,6,7)
