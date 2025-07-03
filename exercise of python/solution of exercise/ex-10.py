# Exercise 10: Password Checker (while + if)
# Set a correct password (e.g., "python123").

# Ask the user to enter a password in a loop.

# If correct, print "Access granted!" and exit.

# If wrong, keep asking (limit to 3 attempts).

correct_password="python123"
attempts=3
while True:
    password=input("enter the password: ")
    if password==correct_password:
        print("Access granted!")
        break
        
    else:
        print("wrong try agin !!")
        attempts-=1
        print(f"attemps left is  {attempts}")
        if attempts==0:
            break
        else:
            continue

