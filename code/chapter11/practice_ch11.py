# Chapter 11 Practice
# Murach's Python Programming

from datetime import datetime, timedelta

# --------------------------------------------------
# Practice 1
# Get the current date and time
# --------------------------------------------------

# 1. Import datetime from the datetime module.
# 2. Get the current date and time.
# 3. Print the current date and time.

now = datetime.now()
print("Current date and time:", now)


# --------------------------------------------------
# Practice 2
# Format a date
# --------------------------------------------------

# 1. Format the current date as MM/DD/YYYY.
# 2. Print the formatted date.

formatted_date = now.strftime("%m/%d/%Y")
print("Formatted date:", formatted_date)

# --------------------------------------------------
# Practice 3
# Work with a span of time
# --------------------------------------------------

# 1. Import timedelta from the datetime module.
# 2. Calculate the date 30 days from today.
# 3. Print the new date.

future_date = now + timedelta(days=30)
print("30 days from today:", future_date)
