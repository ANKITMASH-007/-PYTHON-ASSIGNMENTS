#write a lambdda function to calculat eproduct of elements of the list
from functools import reduce
def mutiple_list(nums):
    result =  reduce(lambda x, y: x*y, nums)
    return result
nums = [4, 3, 2, 2, 1, 5]
print ("Original list: ")
print(nums)
print("Mmultiply all the numbers of the said list:",mutiple_list(nums))
