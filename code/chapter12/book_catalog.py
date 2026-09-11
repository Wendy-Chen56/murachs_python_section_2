# Chapter 12 - The Book Catalog Program

def display_books(books):
    print("\nBook Catalog")

    for code, book in books.items():
        title = book[0]
        price = book[1]
        print(code, "-", title, "-", price)


def main():
    books = {
        "PY": ["Python Programming", 39.99],
        "HTML": ["HTML and CSS", 29.99],
        "JS": ["JavaScript", 34.99]
    }

    display_books(books)


if __name__ == "__main__":
    main()
