'''
 Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus: 
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] 

'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
p1=input("Enter your new password: ")
p2=input("Enter your new password again: ")
if p1==p2:
    if len(p1)>=8 and len(p1)<=12:
        if p1 not in BAD_PASSWORDS:
            print("Password Set")
        else:
            print("Password is too common")
    else:
        print("Password must be 8-12 charcters")