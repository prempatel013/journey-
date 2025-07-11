"""
🐍 PYTHON DAY 2 MASTER FILE: CONTROL FLOW & COLLECTIONS 🐍
Covers:
- Conditional statements (if/elif/else)
- Loops (for/while)
- Lists and tuples
- Error handling
"""

# ================ 1. CONDITIONAL STATEMENTS ================
print("\n" + "="*50 + "\n🔀 CONDITIONAL STATEMENTS (if/elif/else)\n" + "="*50)

"""
🔍 Theory:
Conditionals let your program make decisions based on conditions.
Structure:
if condition1:
    # code block
elif condition2:
    # code block
else:
    # default code block

Key Points:
- Indentation (4 spaces) defines code blocks
- Conditions evaluate to True/False
- elif is optional (as many as needed)
- else is optional
"""

# 🛠️ Example 1: Basic if-else
print("\n--- Example 1: Temperature Check ---")


temp = float(input("Enter current temperature (°C): "))

if temp > 30:
    print("It's hot! Stay hydrated.")
elif 20 <= temp <= 30:
    print("Nice weather!")
else:
    print("It's cold. Bring a jacket.")

# 🛠️ Example 2: Nested Conditionals
print("\n--- Example 2: Age Verification ---")
age = int(input("Enter your age: "))

if age >= 18:
    license = input("Do you have a driver's license? (yes/no): ").lower()
    if license == "yes":
        print("You can drive!")
    else:
        print("You need to get a license first.")
else:
    print("Too young to drive.")

# 🎯 Exercise 1: Grade Calculator
"""
Write a program that:
1. Takes a score (0-100) as input
2. Prints the grade:
   - A (90-100)
   - B (80-89)
   - C (70-79)
   - D (60-69)
   - F (<60)
"""

grade=int(input("Enter your Grade buddy👂: "))
if grade>=90:
    print('you got A Grade congratulations 🎉')

elif grade>=80:
    print('you got B Grade congratulations 🎉')
elif grade>=70:
    print('you got C Grade congratulations 🎉')
elif grade>=60:
    print('you got D Grade ')
elif grade<60:
    print("you got F Grade")


# ================ 2. LOOPS ================
print("\n" + "="*50 + "\n🔄 LOOPS (for/while)\n" + "="*50)

"""
🔍 Theory:
Loops repeat code until a condition is met.

for loops:
- Iterate over sequences (lists, strings, range, etc.)
- Fixed number of iterations

while loops:
- Run until condition becomes False
- Potentially infinite (be careful!)
"""

# 🛠️ Example 1: for loop with range()
print("\n--- Example 1: Countdown Timer ---")
for i in range(5, 0, -1):  # start=5, stop=0, step=-1
    print(f"Countdown: {i}")
print("Blast off!")

# 🛠️ Example 2: while loop with user input
print("\n--- Example 2: Number Guessing Game ---")
secret = 7
attempts = 3

while attempts > 0:
    guess = int(input(f"Guess the number (1-10). {attempts} attempts left: "))
    if guess == secret:
        print("You won!")
        break
    attempts -= 1
else:  # Runs if loop completes without break
    print(f"Out of attempts! The number was {secret}.")

# 🎯 Exercise 2: Multiplication Table
"""
Create a program that:
1. Takes a number as input
2. Prints its multiplication table from 1 to 10
Example output for 5:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""
num=int(input('enter the number: '))
for i in range (1,11):  #here i used range that is built in function that  generate a sequence of numbers.It generates numbers starting from 1 (inclusive)
# Up to but not including 11 (so it stops at 10)
    print(f'{num}X{i} = {num*i}  ')

# ================ 3. LISTS & TUPLES ================
print("\n" + "="*50 + "\n📚 LISTS & TUPLES\n" + "="*50)

"""
🔍 Theory:
Lists:
- Ordered, mutable (changeable) sequences
- Created with square brackets []

Tuples:
- Ordered, immutable (unchangeable)
- Created with parentheses ()
- Faster than lists for fixed data
"""

# 🛠️ Example 1: List operations
print("\n--- Example 1: Shopping List ---")
shopping_list = ["apples", "milk", "bread"]

# Add item
shopping_list.append("eggs")
print(f"After adding: {shopping_list}")

# Remove item
shopping_list.remove("milk")
print(f"After removing: {shopping_list}")

# Access items
print(f"First item: {shopping_list[0]}")
print(f"Last item: {shopping_list[-1]}")

# 🛠️ Example 2: Tuple unpacking
print("\n--- Example 2: Coordinate System ---")
point = (3, 4)  # (x, y) coordinates
x, y = point  # Tuple unpacking
print(f"X coordinate: {x}, Y coordinate: {y}")

# 🎯 Exercise 3: To-Do List Manager
"""
Build a program that:
1. Starts with empty list
2. Menu options:
   - Add task
   - Remove task
   - View all tasks
   - Quit
Use while loop to keep running until quit
"""
'''here is solution of i did 

menu_list=[]

while True:

    ask=int(input('what do you want to do : \n 1.add task \n 2.Remove task \n 3.View all tasks \n 4.Quit\n'))

    if ask==1:
        task=input("so write which task you want to add: ")
        menu_list.append(task)
        
    elif ask==2:
        remove=input(f'{menu_list} which task you want to remove')
        menu_list.remove(remove)
    elif ask==3:
        print(f"{menu_list}")
    elif ask==4:
        quit()
        
        
        '''

# ================ 4. ERROR HANDLING ================
print("\n" + "="*50 + "\n⚠️ ERROR HANDLING (try/except)\n" + "="*50)

"""
🔍 Theory:
Prevent crashes from invalid input/operations.
Basic structure:
try:
    # risky code
except ErrorType:
    # handle error
"""

# 🛠️ Example: Safe number input
print("\n--- Example: Age Validator ---")
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age can't be negative")
        break
    except ValueError:
        print("Please enter a valid positive number!")

print(f"Your age is: {age}")

# ================ 🎯 DAY 2 PROJECT ================
print("\n" + "="*50 + "\n🎯 DAY 2 CAPSTONE: QUIZ GAME\n" + "="*50)

questions = [
    ("What is 2+2?", "4"),
    ("Capital of France?", "paris"),
    ("Python is interpreted or compiled?", "interpreted")
]

score = 0

print("Welcome to the Python Quiz!")
for question, correct_answer in questions:
    user_answer = input(f"\nQ: {question} ").lower()
    if user_answer == correct_answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The answer is: {correct_answer}")

print(f"\nYour final score: {score}/{len(questions)}")

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
# ================ 📝 NOTES SECTION ================
"""
📝 My Personal Notes:

[Add your observations here]
Example:
- 2025-06-25: Remember that list indices start at 0!
- 2025-06-25: 'break' exits the entire loop, 'continue' skips to next iteration
"""

# ================ 🚀 WHAT'S NEXT? ================
"""
Tomorrow's Topics (Day 3):
1. Functions (def, return, parameters)
2. Dictionaries (key-value pairs)
3. More list operations (slicing, sorting)
"""

print("\n" + "="*50 + "\n🎉 CONGRATS ON COMPLETING DAY 2! 🎉\n" + "="*50)