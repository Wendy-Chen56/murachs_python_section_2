# Murach's Python Programming
# Section 2 - Other Concepts and Skills
# Chapter 10 - How to Work with Strings

print("Chapter 10 - How to Work with Strings")
print()


# --------------------------------
# 1. Unicode
# --------------------------------

print("5 =", ord("5"))
print("A =", ord("A"))
print("a =", ord("a"))

print()


# --------------------------------
# 2. Indexes
# --------------------------------

message = "Hello out there!"

print(message[0])
print(message[1])
print(message[-1])

print()


# --------------------------------
# 3. Slicing
# --------------------------------

message = "Hello out there!"

print(message[:5])
print(message[6:9])
print(message[10:])
print(message[:-1])

print()


# --------------------------------
# 4. Repetition
# --------------------------------

print("=" * 20)
print("A horse! " * 2)

print()


# --------------------------------
# 5. Multiline String
# --------------------------------

query = '''SELECT categoryID, name AS categoryName
FROM Category WHERE categoryID = ?'''

print(query)

print()


# --------------------------------
# 6. Search a String
# --------------------------------

spam = "Congratulations. You've won a million dollars."

print("million" in spam)
print("Million" in spam)
print("on" in spam)

print()


# --------------------------------
# 7. Loop Through a String
# --------------------------------

message = "Hi!"

for char in message:
    print(char)

print()


# --------------------------------
# 8. Basic String Methods
# --------------------------------

entry = "12345"
print(entry.isdigit())

title = "The Meaning of Life"
print(title.startswith("The"))

movie = "the meaning of life"
print(movie.title())

ssn = " 392 55 7722 "
print(ssn.strip())

print("Hammer".ljust(14), "$9.99".rjust(10))
print("Nails".ljust(14), "$14.50".rjust(10))

print()


# --------------------------------
# 9. find()
# --------------------------------

email = "joel.murach@com"

at_index = email.find("@")
dot_index = email.find(".", at_index)

print(at_index)
print(dot_index)

print()


# --------------------------------
# 10. Get First Word
# --------------------------------

title = "The Meaning of Life"

i = title.find(" ")

if i == -1:
    first_word = "This title doesn't contain a space."
else:
    first_word = title[0:i]

print(first_word)

print()


# --------------------------------
# 11. replace()
# --------------------------------

cc_number = "4012-881022-88810"
cc_number = cc_number.replace("-", " ")

print(cc_number)

phone_number = "555-555-1234"
phone_number = phone_number.replace("-", "")

print(phone_number)

print()


# --------------------------------
# 12. removeprefix() / removesuffix()
# --------------------------------

email = "joel@murach.com"

print(email.removeprefix("joel"))
print(email.removesuffix(".com"))

print()


# --------------------------------
# 13. split()
# --------------------------------

quotation = "These are the times that try men's souls."

words = quotation.split()

print(words[0])
print(words[3])
print(words[-1])

print()


date = "11/9/1972"
date = date.split("/")

month = int(date[0])
day = int(date[1])
year = int(date[2])

print(month)
print(day)
print(year)

print()


address = "John Doe|1500 Any Street|New York|NY|10001"
address = address.split("|")

print(address[0])
print(address[1])
print(f"{address[2]}, {address[3]} {address[4]}")

print()


# --------------------------------
# 14. join()
# --------------------------------

first_name = "Eric"
last_name = "Idle"

full_name = last_name + ", " + first_name

print(full_name)


address = [
    "John Doe",
    "1500 Any Street",
    "New York",
    "NY",
    "10001"
]

address = "|".join(address)

print(address)


letters = "HORSE"
letters_spaced = " ".join(letters)

print(letters_spaced)

print()

