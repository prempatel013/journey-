"""
🐍 PYTHON DAY 4 MASTER FILE: FILES, OOP & JSON 🐍
Covers:
- File handling (read/write)
- Object-Oriented Programming (classes)
- JSON data processing
"""

# ================ 1. FILE HANDLING ================
print("\n" + "="*50 + "\n📁 FILE HANDLING\n" + "="*50)

"""
🔍 Theory:
Files allow persistent data storage. Key modes:
- 'r' : Read (default)
- 'w' : Write (overwrites)
- 'a' : Append
- 'x' : Exclusive creation
- 'b' : Binary mode
"""

# 🛠️ Example 1: Writing to a File
print("\n--- Example 1: Writing Diary Entry ---")

def write_diary(entry):
    with open("diary.txt", "a") as file:  # 'a' = append mode
        file.write(f"{entry}\n")
    print("✓ Entry saved!")

write_diary("2025-06-28: Learned file handling in Python!")


# 🛠️ Example 2: Reading from a File
print("\n--- Example 2: Reading Config ---")


def read_config():
    try:
        with open("config.txt") as file:
            return file.read().splitlines()  # Returns list of lines
    except FileNotFoundError:
        return ["default_setting=1"]

settings = read_config()
print("Current settings:", settings)

# 🎯 Exercise 1: File Analyzer
"""
Create a function that:
1. Takes a filename
2. Returns:
   - Line count
   - Word count
   - Most common word
"""




# ================ 2. OBJECT-ORIENTED PROGRAMMING ================
print("\n" + "="*50 + "\n🧩 OBJECT-ORIENTED PROGRAMMING (OOP)\n" + "="*50)

"""
🔍 Theory:
OOP models real-world entities using:
- Classes: Blueprints for objects
- Objects: Instances of classes
- Attributes: Data (variables)
- Methods: Functions inside classes

Key Principles:
- Encapsulation: Bundling data + methods
- Inheritance: Child classes inherit from parents
- Polymorphism: Same method works differently for different classes
"""

# 🛠️ Example 1: Basic Class
print("\n--- Example 1: Bank Account Class ---")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"✓ Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("⚠️ Insufficient funds!")
        else:
            self.balance -= amount
            print(f"✓ Withdrew ${amount}. Remaining: ${self.balance}")

# Using the class
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)

# 🛠️ Example 2: Inheritance
print("\n--- Example 2: Savings Account (Inheritance) ---")
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

savings = SavingsAccount("Bob", 500)
savings.add_interest()

# 🎯 Exercise 2: Book Class
"""
Create a 'Book' class with:
- Attributes: title, author, pages
- Method: get_summary() returns "Title by Author (X pages)"
Create 2 book objects and print their summaries
"""





# ================ 3. WORKING WITH JSON ================
print("\n" + "="*50 + "\n📦 JSON DATA\n" + "="*50)

"""
🔍 Theory:
JSON (JavaScript Object Notation) is a lightweight data format.
Python's json module converts:
- dict ↔ JSON string ↔ file
"""

# 🛠️ Example 1: Dict to JSON
print("\n--- Example 1: Saving User Data ---")
import json

user_profile = {
    "name": "Charlie",
    "age": 28,
    "skills": ["Python", "Data Analysis"]
}

# Write to file
with open("user.json", "w") as file:
    json.dump(user_profile, file, indent=2)  # indent for pretty printing

# 🛠️ Example 2: Reading JSON
print("\n--- Example 2: Loading Config ---")
def load_config():
    try:
        with open("config.json") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"theme": "light", "font_size": 12}

config = load_config()
print("Current config:", config)

# 🎯 Exercise 3: JSON Inventory Manager
"""
Create functions to:
1. Add items to inventory (name, quantity)
2. Save inventory to JSON file
3. Load inventory from file
"""

# ================ 🎯 DAY 4 PROJECTS ================
print("\n" + "="*50 + "\n🎯 DAY 4 PROJECTS\n" + "="*50)

# Project 1: Contact Book with Files
print("\n--- Project 1: Contact Book ---")
class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self._load_contacts()
    
    def _load_contacts(self):
        try:
            with open(self.filename) as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        self._save_contacts()
        print(f"✓ Added {name}")
    
    def _save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=2)
    
    def search(self, name):
        return self.contacts.get(name, "Contact not found")

# Usage
book = ContactBook()
book.add_contact("Alice", "555-1234")
print("Alice's number:", book.search("Alice"))

# Project 2: RPG Character System (OOP)
print("\n--- Project 2: RPG Characters ---")
class RPGCharacter:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 100
    
    def level_up(self):
        self.level += 1
        self.health += 20
        print(f"🌟 {self.name} leveled up to {self.level}!")
    
    def __str__(self):
        return f"{self.name} ({self.character_class}, Lvl {self.level})"

warrior = RPGCharacter("Grimbold", "Warrior")
warrior.level_up()
print(warrior)

# ================ 📝 NOTES SECTION ================
"""
📝 My Personal Notes:

[Add your observations here]
Example:
- 2023-10-04: Remember to always close files or use 'with' blocks
- 2023-10-04: Class names use PascalCase by convention
"""

# ================ 🚀 WHAT'S NEXT? ================
"""
Tomorrow's Topics (Day 5):
1. Working with APIs (requests library)
2. Virtual environments
3. Web scraping basics
"""

print("\n" + "="*50 + "\n🎉 CONGRATS ON COMPLETING DAY 4! 🎉\n" + "="*50)