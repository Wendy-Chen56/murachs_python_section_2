# Murach's Python Programming
# Section 2 - Other Concepts and Skills
# Chapter 10 Practice - How to Work with Strings

print("Chapter 10 Practice")
print()


# --------------------------------
# Practice 1 - Indexing and Slicing
# --------------------------------

message = "Python Strings"

print(message[0])
print(message[-1])
print(message[:6])
print(message[7:])

print()


# --------------------------------
# Practice 2 - Search with in
# --------------------------------

sentence = "Python is easy to learn."

print("Python" in sentence)
print("Java" in sentence)

print()


# --------------------------------
# Practice 3 - String Methods
# --------------------------------

number = "12345"
print(number.isdigit())

title = "python programming"
print(title.title())

name = "    Wendy Chen     "
print(name.strip())

print()


# --------------------------------
# Practice 4 - find() and replace()
# --------------------------------

email = "student@pacific.edu"

print(email.find("@"))

phone = "209-555-1236"
phone = phone.replace("-", "")

print(phone)

print()


# --------------------------------
# Practice 5 - split()
# --------------------------------

date = "6/9/2026"
date_parts = date.split("/")

print(date_parts[0])
print(date_parts[1])
print(date_parts[2])

print()


name = "Wendy|Chen"

name_parts = name.split("|")
print(name_parts[0])
print(name_parts[1])

print()


# --------------------------------
# Practice 6 - join()
# --------------------------------

address = [
    "Stockton",
    "CA",
    "U.S"
]

full_address = ",".join(address)

print(full_address)

letters = "PYTHON"
letters_spaced = " ".join(letters)

print(letters_spaced)

print()

