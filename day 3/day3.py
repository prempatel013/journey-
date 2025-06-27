"""
🐍 PYTHON DAY 3 MASTER FILE: FUNCTIONS & DATA STRUCTURES 🐍
Covers:
- Functions (def, parameters, return)
- Dictionaries (key-value pairs)
- Advanced list operations
- Modules and imports
"""

# ================ 1. FUNCTIONS ================
print("\n" + "="*50 + "\n📌 FUNCTIONS\n" + "="*50)

"""
🔍 Theory:
Functions are reusable blocks of code that:
1. Take inputs (parameters)
2. Perform actions
3. Return outputs

Why use them?
- Avoid code repetition
- Organize logic into named blocks
- Make code easier to debug
"""

# 🛠️ Example 1: Basic Function
print("\n--- Example 1: Greeting Function ---")
def greet(name):
    """Returns a personalized greeting"""  # Docstring (documentation)
    return f"Hello, {name}! Welcome to Python."

message = greet("Alice")
print(message)

# 🛠️ Example 2: Function with Multiple Parameters
print("\n--- Example 2: BMI Calculator ---")
def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index"""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)  # Rounds to 1 decimal place

print(f"BMI: {calculate_bmi(70, 1.75)}")

# 🎯 Exercise 1: Password Strength Checker
"""
Create a function that:
1. Takes a password string
2. Returns "Weak", "Medium", or "Strong" based on:
   - Weak: <8 characters
   - Medium: 8-12 chars, no special characters
   - Strong: >12 chars with special chars (!,@,#, etc.)
"""

# ================ 2. DICTIONARIES ================
print("\n" + "="*50 + "\n📚 DICTIONARIES\n" + "="*50)

"""
🔍 Theory:
Dictionaries store data as key-value pairs:
- Keys: Unique identifiers (usually strings)
- Values: Associated data (any type)
- Created with curly braces {}
"""

# 🛠️ Example 1: Basic Dictionary
print("\n--- Example 1: User Profile ---")
user = {
    "username": "coder123",
    "email": "coder@example.com",
    "age": 25,
    "is_active": True
}

print(f"User: {user['username']}")
print(f"Email: {user.get('email', 'Not provided')}")  # Safer access

# 🛠️ Example 2: Dictionary Operations
print("\n--- Example 2: Inventory System ---")
inventory = {"apples": 50, "bananas": 30, "oranges": 45}

# Add new item
inventory["grapes"] = 20

# Update quantity
inventory["apples"] += 10

# Check existence
if "bananas" in inventory:
    print(f"Bananas in stock: {inventory['bananas']}")

# 🎯 Exercise 2: Word Frequency Counter
"""
Write a function that:
1. Takes a string (e.g., "hello world hello")
2. Returns a dictionary with word counts
   {'hello': 2, 'world': 1}
"""

# ================ 3. ADVANCED LIST OPERATIONS ================
print("\n" + "="*50 + "\n📈 ADVANCED LISTS\n" + "="*50)

# 🛠️ Example 1: List Slicing
print("\n--- Example 1: List Slicing ---")
numbers = [10, 20, 30, 40, 50, 60]
print("Middle elements:", numbers[2:5])  # [30, 40, 50]
print("Every 2nd item:", numbers[::2])   # [10, 30, 50]

# 🛠️ Example 2: List Comprehension
print("\n--- Example 2: Squares with Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)  # [1, 4, 9, 16, 25]

# 🛠️ Example 3: Sorting
print("\n--- Example 3: Leaderboard ---")
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
print("Top scorer:", sorted_scores[0][0])

# 🎯 Exercise 3: Unique Words Finder
"""
Given a list of words:
words = ["apple", "banana", "apple", "orange", "banana"]
Create a new list with only unique words using:
1. List comprehension
2. Or convert to set and back to list
"""

# ================ 4. MODULES ================
print("\n" + "="*50 + "\n📦 MODULES\n" + "="*50)

"""
🔍 Theory:
Modules are Python files containing reusable code.
Python has 300+ built-in modules!
"""

# 🛠️ Example 1: Math Module
print("\n--- Example 1: Math Operations ---")
import math

print("Square root of 16:", math.sqrt(16))
print("Pi constant:", math.pi)

# 🛠️ Example 2: Random Module
print("\n--- Example 2: Dice Roller ---")
from random import randint

def roll_dice():
    return randint(1, 6)

print("You rolled:", roll_dice())

# 🎯 Exercise 4: Current Date Printer
"""
Use the 'datetime' module to:
1. Print today's date
2. Format it as "Month Day, Year" (e.g., "October 03, 2023")
"""

# ================ 🎯 DAY 3 PROJECTS ================
print("\n" + "="*50 + "\n🎯 DAY 3 PROJECTS\n" + "="*50)

# Project 1: User Profile Manager
print("\n--- Project 1: User Profile Manager ---")
def create_profile():
    profile = {}
    profile["name"] = input("Enter name: ")
    profile["age"] = int(input("Enter age: "))
    profile["email"] = input("Enter email: ")
    return profile

user_profile = create_profile()
print("\nUser Profile Created:")
for key, value in user_profile.items():
    print(f"{key.capitalize()}: {value}")

# Project 2: Movie Rating System (Capstone)
print("\n--- Project 2: Movie Rating System ---")
movies = {
    "The Shawshank Redemption": {"rating": 9.3, "votes": 2500000},
    "The Godfather": {"rating": 9.2, "votes": 1800000}
}

def add_movie(title, rating, votes):
    movies[title] = {"rating": rating, "votes": votes}

def show_movies():
    print("\nCurrent Movies:")
    for title, details in movies.items():
        print(f"{title}: {details['rating']}/10 ({details['votes']} votes)")

add_movie("Pulp Fiction", 8.9, 1500000)
show_movies()

# ================ 📝 NOTES SECTION ================
"""
📝 My Personal Notes:

[Add your observations here]
Example:
- 2023-10-03: Remember that dictionary keys must be immutable (strings, numbers, tuples)
- 2023-10-03: Functions can return multiple values as tuples!
"""

# ================ 🚀 WHAT'S NEXT? ================
"""
Tomorrow's Topics (Day 4):
1. File Handling (read/write files)
2. Object-Oriented Programming (classes)
3. Working with JSON data
"""

print("\n" + "="*50 + "\n🎉 CONGRATS ON COMPLETING DAY 3! 🎉\n" + "="*50)