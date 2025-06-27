def add_book(library):
    """Adds a book to the library dictionary"""
    title = input("Enter book title: ")
    author = input("Enter author: ")
    pages = int(input("Enter page count: "))
    library[title] = {"author": author, "pages": pages}
    print(f"✅ Added '{title}' to library!")

def show_library(library):
    """Displays all books in the library"""
    print("\n📖 YOUR LIBRARY:")
    for title, details in library.items():
        print(f"'{title}' by {details['author']} ({details['pages']} pages)")

# Main program
my_library = {}
while True:
    print("\nOptions: 1. Add Book 2. View Library 3. Quit")
    choice = input("Choose (1-3): ")
    
    if choice == "1":
        add_book(my_library)
    elif choice == "2":
        show_library(my_library)
    elif choice == "3":
        print("Happy reading!")
        break
    else:
        print("⚠️ Invalid choice")