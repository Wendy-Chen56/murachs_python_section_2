# Chapter 12 - How to Work with Dictionaries
# How to create a dictionary

countries = {
    "US": "United States",
    "CA": "Canada",
    "MX": "Mexico"
}

print(countries)


# How to get, set, and add items

# Get an item
country = countries["US"]
print("US:", country)

# Set an item
countries["US"] = "United States of America"
print("Updated US:", countries["US"])

# Add an item
countries["JP"] = "Japan"
print("Added JP:", countries["JP"])

print(countries)


# How to delete items

del countries["MX"]

print("After deleting MX:")
print(countries)


# How to loop through keys and values

# Loop through the keys
print("Country codes:")
for code in countries:
    print(code)

# Loop through the keys and values
print("Country codes and names:")
for code, country in countries.items():
    print(code, country)


# How to convert between dictionaries and lists

# Convert dictionary keys to a list
codes = list(countries.keys())
print("Codes:", codes)

# Convert dictionary values to a list
country_names = list(countries.values())
print("Countries:", country_names)

# Convert a list of tuples to a dictionary
country_list = [
    ("FR", "France"),
    ("DE", "Germany"),
    ("IT", "Italy")
]

country_dict = dict(country_list)
print("New dictionary:", country_dict)




# How to use the merge and update operators

countries1 = {
    "US": "United States",
    "CA": "Canada"
}

countries2 = {
    "MX": "Mexico",
    "JP": "Japan"
}

# Merge two dictionaries
all_countries = countries1 | countries2
print("Merged dictionary:")
print(all_countries)

# Update a dictionary
countries1 |= countries2
print("Updated dictionary:")
print(countries1)


# How to use dictionaries with complex objects as values

books = {
    "python": ["Python Programming", 39.99],
    "html": ["HTML and CSS", 29.99],
    "javascript": ["JavaScript", 34.99]
}

print("Book information:")
print(books["python"])

print("Title:", books["python"][0])
print("Price:", books["python"][1])
