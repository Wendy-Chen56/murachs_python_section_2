# Chapter 11 - How to Work with Dates and Times
# Murach's Python Programming

from datetime import date, time, datetime, timedelta


# --------------------------------------------------
# 1. Create a date object
# --------------------------------------------------

today = date.today()
christmas = date(2026, 12, 25)

print("Today's date:", today)
print("Christmas:", christmas)


# --------------------------------------------------
# 2. Create a time object
# --------------------------------------------------

start_time = time(9, 30)
end_time = time(17, 0)

print("Start time:", start_time)
print("End time:", end_time)


# --------------------------------------------------
# 3. Create a datetime object
# --------------------------------------------------

now = datetime.now()
meeting = datetime(2026, 10, 15, 14, 30)

print("Current date and time:", now)
print("Meeting:", meeting)


# --------------------------------------------------
# 4. Parse a string into a datetime object
# --------------------------------------------------

date_string = "12/25/2026"

christmas_datetime = datetime.strptime(
    date_string,
    "%m/%d/%Y"
)

print("Date string:", date_string)
print("Converted datetime:", christmas_datetime)


# --------------------------------------------------
# 5. Format dates and times
# --------------------------------------------------

formatted_date = today.strftime("%m/%d/%Y")
formatted_date_2 = today.strftime("%B %d, %Y")
formatted_datetime = now.strftime("%m/%d/%Y %I:%M %p")

print("Formatted date:", formatted_date)
print("Another date format:", formatted_date_2)
print("Formatted date and time:", formatted_datetime)


# --------------------------------------------------
# 6. Work with spans of time
# --------------------------------------------------

time_until_christmas = christmas - today

print("Time until Christmas:", time_until_christmas)
print("Days until Christmas:", time_until_christmas.days)


one_week = timedelta(days=7)

next_week = today + one_week
last_week = today - one_week

print("Next week:", next_week)
print("Last week:", last_week)


# --------------------------------------------------
# 7. Get date and time parts
# --------------------------------------------------

print("Christmas year:", christmas.year)
print("Christmas month:", christmas.month)
print("Christmas day:", christmas.day)

print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)

print("Meeting year:", meeting.year)
print("Meeting month:", meeting.month)
print("Meeting day:", meeting.day)
print("Meeting hour:", meeting.hour)
print("Meeting minute:", meeting.minute)


# --------------------------------------------------
# 8. Compare date objects
# --------------------------------------------------

if today < christmas:
    print("Christmas is in the future.")
elif today > christmas:
    print("Christmas has already passed.")
else:
    print("Today is Christmas.")
