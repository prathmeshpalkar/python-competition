#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sample library inventory
library_inventory = {
    "Book1": 5,
    "Book2": 3,
    "Book3": 7,
    "Book4": 2,
    "Book5": 4
}

def display_books():
    print("Available Books:")
    for book, quantity in library_inventory.items():
        print(f"{book} - Quantity: {quantity}")

def borrow_book():
    book_title = input("Enter the title of the book you want to borrow: ")
    if book_title in library_inventory and library_inventory[book_title] > 0:
        library_inventory[book_title] -= 1
        print(f"You have borrowed '{book_title}'. Enjoy reading!")
    else:
        print("Sorry, the book is either unavailable or not in the inventory.")

def return_book():
    book_title = input("Enter the title of the book you want to return: ")
    if book_title in library_inventory:
        library_inventory[book_title] += 1
        print(f"Thank you for returning '{book_title}'.")
    else:
        print("This book doesn't belong to our library.")


while True:
    print("\nLibrary Management System")
    print("1. Display Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_books()
    elif choice == '2':
        borrow_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        print("Thank you for using the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


# In[ ]:




