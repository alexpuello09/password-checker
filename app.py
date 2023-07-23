

print("\nWelcome to the Password Strength Checker!")
print("\tWrite the word EXIT to leave of the program")

total = 0
symbols = 0
letters = 0
numbers = 0
total_num = 0
total_lett = 0
total_sym = 0
lower1 = 0
repeat = ""

import re
while repeat.lower() != "exit":
    password = input("\nEnter a password with at least eight to fifteen characters: ")
    repeat = password
    if repeat.lower() != "exit":
        if len(password) > 15:
            print("\nInvalid password enter a password with at least eight until fifteen characters ")
        else:

            #Regular expression for match symbols 

            pattern = re.compile(r'[-@!#$%()*+_]')
            symbols = pattern.findall(password)
            symbols = len(symbols)
            pattern = 0

            if symbols == 0:
                total_sym = 0
            elif symbols == 1:
                total_sym = 1
            elif symbols == 2:
                total_sym = 2
            elif symbols == 3 or symbols == 4:
                total_sym = 3
            elif symbols > 4 and symbols < 8:
                total_sym = 4
            else:
                total_sym = 5

            #Regular expression for match Letters
        
            pattern = re.compile(r"[a-zA-Z]")
            letters = pattern.findall(password)
            letters = len(letters)
            pattern = 0

            if letters == 0:
                total_lett = 0
            elif letters == 1:
                total_lett = 1
            elif letters == 2:
                total_lett = 2
            elif letters == 3 or letters == 4:
                total_lett = 3
            elif letters > 4 and letters < 8:
                total_lett = 4
            else:
                total_lett = 5


            #Regular expression for match numbers

            pattern  = re.compile(r"\d")
            numbers = pattern.findall(password)
            numbers = len(numbers)
            pattern = 0

            if numbers == 0:
                total_num = 0
            elif numbers == 1:
                total_num = 1
            elif numbers == 2:
                total_num = 2
            elif numbers == 3 or numbers == 4:
                total_num = 3
            elif numbers == 4 and numbers < 8:
                total_num = 4
            else:
                total_num = 5

            #Regular expression for match lower

            pattern = re.compile(r"[A-Z]")
            lower1 = pattern.findall(password)
            lower1 = len(lower1)

            if lower1 == 0:
                total_low = 0
            elif lower1 == 1:
                total_low = 1
            elif lower1 == 2:
                total_low = 2
            elif lower1 == 3 or lower1 == 4:
                total_low = 3
            elif lower1 > 4 and lower1 < 8:
                total_low = 4
            else:
                total_low = 5
            
            

            

            total =  total_lett + total_num + total_sym + total_low


            if total == 15  or total < 15:
                print(f"\nStrength Score: {total}/10")
                if total == 1:
                    print("Invalid password write a password of unless eight characters")
                if total > 7 and total < 15:
                    print("Password Strength: Strong")
                    print("Suggestions:Consider using a longer password\n")
                elif total > 4 and total < 8:
                    print("Password Strength: A little secure")
                    print("Suggestions: Use a longer password with a combination of uppercase letters, lowercase letters, numbers, and special characters.\n")
                elif total < 5 and total > 2:
                    print("Password Strength: Not secure")
                    print("Suggestions: Use a longer password\n")
            
                
    elif repeat.lower()=="exit":
        print("\nThank you for using the Password Strength Checker!")
