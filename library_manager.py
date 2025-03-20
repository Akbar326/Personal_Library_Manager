import json
import os
from colorama import init, Fore, Style

init()

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return []
    
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    print("\n" + Fore.CYAN + "=== Add a Book ===" + Style.RESET_ALL)
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid year (number)." + Style.RESET_ALL)
    
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read = read_input == "yes"

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(Fore.GREEN + "Book added successfully!" + Style.RESET_ALL)

def remove_book(library):
    print("\n" + Fore.CYAN + "=== Remove a Book ===" + Style.RESET_ALL)
    title = input("Enter the title of the book to remove: ")
    initial_length = len(library)
    library = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print(Fore.GREEN + "Book removed successfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Book '{title}' not found!" + Style.RESET_ALL)
    return library

def search_library(library):
    print("\n" + Fore.CYAN + "=== Search for a Book ===" + Style.RESET_ALL)
    print("Search by:")
    print("1. Title")
    print("2. Author")
    
    search_choice = input("Enter your choice: ")
    
    if search_choice == "1":
        search_by = "title"
    elif search_choice == "2":
        search_by = "author"
    else:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        return
    
    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\n" + Fore.YELLOW + "Matching Books:" + Style.RESET_ALL)
        for i, book in enumerate(results, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(Fore.RED + f"No books found matching '{search_term}' in {search_by} field" + Style.RESET_ALL)

def display_all_books(library):
    print("\n" + Fore.CYAN + "=== Your Library ===" + Style.RESET_ALL)
    if library:
        for i, book in enumerate(library, 1):
            status = "Read" if book['read'] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print(Fore.YELLOW + "Library is empty!" + Style.RESET_ALL)

def display_statistics(library):
    print("\n" + Fore.CYAN + "=== Library Statistics ===" + Style.RESET_ALL)
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def display_menu():
    print("\n" + Fore.CYAN + "Menu" + Style.RESET_ALL)
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def main():
    library = load_library()
    
    print(Fore.YELLOW + "\n===================================")
    print("  Welcome to Personal Library Manager")
    print("===================================" + Style.RESET_ALL)
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n" + Fore.GREEN + "Library saved to file. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == '__main__':
    main()