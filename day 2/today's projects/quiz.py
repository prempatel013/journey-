

# questions = [
#     ("What is 2+2?", "4"),
#     ("Capital of india?", "Delhi"),
#     ("Python is interpreted or compiled?", "interpreted")
# ]
# so in  this project we  will create an quiz game :
# so in first line we will anousefor quiz and ask for want to play this game or not :
score=0
ask=input("Do you want to play this game? (yes/no): ")


if ask!="yes":
    quit()            
            
que1=input('What is 2+2? ')
            
if que1=="4":
    score+=1
    print(f"right answer 👍!! score is :{score}")
else:
    print(f"wrong answer❌")

que2=input("Capital of india?")
    
if que2.lower()=="delhi":
    score+=1
    print(f"right answer 👍!! score is :{score}")

else:
    print('wrong answer!!❌')
            
que3=input("Python is interpreted or compiled?")
        
if que3.lower()=="interpreted":
    score+=1
    print(f"right answer 👍!! score is :{score}")
            
else:
    print("wrong answer!!❌")

print(f"your score is {score}")