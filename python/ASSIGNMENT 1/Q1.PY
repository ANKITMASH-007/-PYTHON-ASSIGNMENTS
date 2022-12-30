string = str(input("enter your string"))
half = int(len(string) / 2)
 
if len(string) % 2 == 0:
    first_str = string[:half]
    second_str = string[half:]
else:
    first_str = string[:half]
    second_str = string[half+1:]
if first_str == second_str:
    print(string, 'string is symmertical')
else:
    print(string, 'string is not symmertical')
if first_str == second_str[::-1]:
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')