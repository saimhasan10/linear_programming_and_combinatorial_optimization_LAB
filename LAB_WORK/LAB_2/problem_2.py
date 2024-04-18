"""
    2. Write a code if the last 3 digits of your ID is greater than 500 then it prints 
    "My ID is more than 500" 
    Otherwise the code prints 
    “My ID is not more than 500"
"""
"""
id = input("Enter your ID: ")

last_three_digits = id[-3:]

print("last_three_digits:", last_three_digits)

"""

id = int(input("Enter your ID: "))

last_three_digits = id % 1000

if(last_three_digits > 500):
    print("My ID is more than 500")
else:
    print("My ID is not more than 500")
