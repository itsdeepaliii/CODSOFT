import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits="0123456789"
symbols="(){}[],.:;-_/\\?+*#"
upper,lower,nums,syms = True,True,True,True
all =""
if upper:
    all+=uppercase_letters
if lower:
    all+= lowercase_letters
if nums:
    all+=digits
if syms:
    all +=symbols
#length = 20
amount = 1

for x in range(amount):
    length=int(input("Enter the length of the password: "))
    password = "".join(random.sample(all,length))
    
    print("Password: ")
    print(password)