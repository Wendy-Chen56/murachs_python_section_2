# Chapter 12 - Practice
# How to Work with Dictionaries

# Practice 1 - Create and access a dictionary

states = {
    "CA": "California",
    "NY": "New York",
    "TX": "Texas"
}

print("Practice 1")
print(states["CA"])
print(states["NY"])


# Practice 2 - Add, update, and delete items

states["FL"] = "Florida"
states["CA"] = "California State"
del states["TX"]

print("\nPractice 2")
print(states)


# Practice 3 - Loop through keys and values

print("\nPractice 3")
for code, state in states.items():
    print(code, state)
