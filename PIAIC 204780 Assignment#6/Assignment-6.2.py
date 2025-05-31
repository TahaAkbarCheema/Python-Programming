# ----------------------------------- Assignment # 6 --------------------------------------------

# NAME : Taaha Akbar Cheema
# ROLL NO:  PIAIC 204780
# Barch No : 70

# ----------------------------------- Project 2: Library Book Management System----------------------
# Library system with book catalog and borrowed list
books = {
    "1984": {"author": "Orwell", "available": True},
    "Dracula": {"author": "Stoker", "available": True}
}

borrowed_books = []  # List to track borrowed books

# Function to view all books
def view_books():
    print("\nAvailable Books:")
    for book_title, details in books.items():
        availability = "Available" if details["available"] else "Not Available"
        print(f'"{book_title}" by {details["author"]} - {availability}')

# Function to borrow a book
def borrow_book():
    book_title = input("Enter book name to borrow: ").strip().lower()
    
    # Check if book exists
    found = False
    for title in books:
        if title.lower() == book_title:
            found = True
            if books[title]["available"]:
                books[title]["available"] = False
                borrowed_books.append(title)
                print(f'You have borrowed "{title}".')
            else:
                print(f'"{title}" is currently not available.')
            break

    if not found:
        print("Book not found. Please check the name and try again.")

# Function to return a book
def return_book():
    book_title = input("Enter book name to return: ").strip().lower()
    
    # Check if the book is in the borrowed list
    if book_title in borrowed_books:
        books[book_title]["available"] = True
        borrowed_books.remove(book_title)
        print(f'You have returned "{book_title}".')
    else:
        print(f'"{book_title}" was not borrowed from this library.')

# Function to add a new book
def add_book():
    book_title = input("Enter the title of the new book: ").strip()
    author = input("Enter the author of the book: ").strip()
    if book_title.lower() in (title.lower() for title in books):
        print(f'"{book_title}" already exists in the library.')
    else:
        books[book_title] = {"author": author, "available": True}
        print(f'"{book_title}" by {author} has been added to the library.')

# Function to view borrowed books
def view_borrowed_books():
    if borrowed_books:
        print("\nBorrowed Books:")
        for book in borrowed_books:
            print(f'"{book}"')
    else:
        print("\nNo books have been borrowed.")

# Main function to control the menu
def main():
    while True:
        print("\nWelcome to the Library System")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add New Book")
        print("5. View Borrowed Books")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            add_book()
        elif choice == '5':
            view_borrowed_books()
        elif choice == '6':
            print("Thank you for using the Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the library system
if __name__ == "__main__":
    main()

