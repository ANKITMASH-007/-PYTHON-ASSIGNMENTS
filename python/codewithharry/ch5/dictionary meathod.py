# this program is to learn about dictionary methods 
dict={
       "ankit":"is a good coder",
       "amit" :"he is a good friend",
       "last" :"this is the last element",
        101 :1000,
        102 :"this is the last element now",
        "dicts" :{ "this" :'this is another dictionary'}

     }
print(dict[102])


print(list(dict.keys()))# printing the keys as a list 

#KEYS 
print(dict.keys())
#this method prints the keys of the dictionary in the form of a list

#VALUES
print(dict.values())
#this method prints the values of the dictionary


#ITEM
print(dict.items())
# this method gives the key value pairs of the dictionary

#UPDATE
print(dict.items())
di={
    "an":"this is the best case"
}
dict.update(di)
print(dict.items())
#add the new value in the dictionary 

#GET
print(dict["ankit"])#print the value of the key
print(dict.get("ankit"))#prints the value of the key



print(dict["ankit2"])#returns none if the key is not present in the dictionary 
print(dict.get("ankit2"))#throws an error if the key is not present






