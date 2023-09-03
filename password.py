import re
import random
def random_pasword_generator():
    #password requirements
    upperchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerchar = upperchar.lower()
    number = "0123456789"
    special = "@!#$%^&*(){}[]"
    allchars= lowerchar + upperchar+ number + special

    length = 10
    amount = 20
    for i in range (int(amount)):
        random_password = "".join(random.sample(allchars,length))
        print(random_password)
random_pasword_generator()                 

def password_generation(password):

    #must given length of the password
            
            
    if len(password) < 8:
        return "password should contains 8 letters"
    #uppercase
    if not re.search(r'[A-Z]', password):  #re.search() searches for that particular pattern within the string
        return "Password must contain at least one uppercase letter"
    #lowercase
    if not re.search(r'[a-z]', password):
        return "password must contain at least one lower letter"
    #numbers
    if not re.search(r'\d', password):
        return "password must contain at least one decimal"
    #special charector
    if not re.search(r'[\W]', password):
        return "password must contain at least one charector"
    return "strong password"
    
password = input("enter your password:")
result = (password_generation(password))
print(result)



