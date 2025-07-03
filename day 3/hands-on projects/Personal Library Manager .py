# Project 1: Personal Library Manager 📚
# Concepts: Functions, Dictionaries, User Input



def add_book(library):
    """Adds a book to the library dictionary"""
    title = input("Enter book title: ")
    author = input("Enter author: ")
    pages = int(input("Enter page count: "))
    rating= float(input("Enter the Rating of this Book(1-5): "))
    library[title] = {"author": author, "pages": pages ,"rating": rating }
    print(f"✅ Added '{title}' to library!")



def show_library(library):
    """Displays all books in the library"""
    print("\n📖 YOUR LIBRARY:")
    for title, details in library.items():
        print(f"'{title}' by {details['author']} ({details['pages']} pages) ({details['rating']} of ratings)")



def search_book(library, title):
    """Search for a book by title in the library list."""
    if title in library:
        return f"✅ '{title}' is available in the library."
    else:
        return f"❌ '{title}' is not found in the library."


# Main program
my_library = {}
while True:
    print("\nOptions: \n 1. Add Book \n 2. View Library\n 3. Quit\n 4. search for book in library")
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        add_book(my_library)
    elif choice == "2":
        show_library(my_library)
   
    elif choice == "3":
        print("Happy reading!")
        break
    elif choice =="4":
        title=input("which book you want to search in library: ")
        result=search_book(my_library,title)
        
        print(result)
    else:
        print("⚠️ Invalid choice")




# Enhancement Ideas:

# Add book ratings (1-5 stars)

# Implement a search function
# Pro Tip: Try combining these projects - e.g., add a "wishlist" feature to the library manager using the shopping cart logic!