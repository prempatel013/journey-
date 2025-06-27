import random
import string

def generate_password(length=12):
    """Generates a random strong password"""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def save_password(vault, service):
    password = generate_password()
    vault[service] = password
    print(f"🔑 Password for {service}: {password}")

# Main program
password_vault = {}
while True:
    print("\n1. Generate New Password 2. View Passwords 3. Exit")
    choice = input("Choose: ")
    
    if choice == "1":
        service = input("Service name (e.g., Gmail): ")
        save_password(password_vault, service)
    elif choice == "2":
        print("\n🔒 YOUR PASSWORDS:")
        for service, pwd in password_vault.items():
            print(f"{service}: {'*' * len(pwd)}")
    else:
        print("Vault locked!") 
        break