s1 = input(" enter first string = ")
s2 = input(" enter first string = ")
def check(s1 , s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
check(s1, s2)