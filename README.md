# Murach's Python Programming - Section 2

This repository contains lesson examples, practice exercises, and presentation slides for Chapters 9-13 of Murach's Python Programming.

The project is designed so that another student can clone the repository and run the Python programs by following the instructions in this README.

---

## Prerequisites

Before running the programs, make sure you have:

- Python 3 installed
- Git installed
- IDLE (included with standard Python installations) or a terminal such as PowerShell

No external Python packages are required for these chapters.

---

## Clone the Repository

Open PowerShell or a terminal and run:

```bash
git clone https://github.com/Wendy-Chen56/murachs_python_section_2.git
```

Then enter the repository:

```bash
cd murachs_python_section_2
```

All commands below should be run from the main repository folder.

You can also open each `.py` file in IDLE and press **F5** to run it.

---

## Repository Structure

```text
murachs_python_section_2/
├── README.md
├── code/
│   ├── chapter09/
│   ├── chapter10/
│   ├── chapter11/
│   ├── chapter12/
│   └── chapter13/
└── slides/
```

---

# Chapter 9 - How to Work with Numbers

This chapter covers:

- Floating-point numbers
- The math module
- Formatting numbers with f-strings
- Decimal numbers
- Rounding with ROUND_HALF_UP

## Files

- `code/chapter09/chapter09_numbers.py` - Lesson examples
- `code/chapter09/practice_ch09.py` - Practice exercises

## How to Run

```bash
python code/chapter09/chapter09_numbers.py
python code/chapter09/practice_ch09.py
```

---

# Chapter 10 - How to Work with Strings

This chapter covers:

- String indexes and slicing
- String repetition
- Multiline strings
- Searching strings with `in`
- Looping through characters
- Basic string methods
- `find()` and `replace()`
- `removeprefix()` and `removesuffix()`
- `split()` and `join()`

## Files

- `code/chapter10/chapter10_strings.py` - Lesson examples
- `code/chapter10/practice_ch10.py` - Practice exercises

## How to Run

```bash
python code/chapter10/chapter10_strings.py
python code/chapter10/practice_ch10.py
```

---

# Chapter 11 - How to Work with Dates and Times

This chapter covers:

- Creating `date`, `time`, and `datetime` objects
- Parsing strings into datetime objects with `strptime()`
- Formatting dates and times with `strftime()`
- Working with spans of time using `timedelta`
- Getting date and time parts
- Comparing date and time objects
- The Invoice Due Date program
- The Timer program

## Files

- `code/chapter11/chapter11_dates_times.py` - Lesson examples
- `code/chapter11/invoice_due_date.py` - Invoice Due Date program
- `code/chapter11/timer.py` - Timer program
- `code/chapter11/practice_ch11.py` - Practice exercises

## How to Run

```bash
python code/chapter11/chapter11_dates_times.py
python code/chapter11/invoice_due_date.py
python code/chapter11/timer.py
python code/chapter11/practice_ch11.py
```

---

# Chapter 12 - How to Work with Dictionaries

This chapter covers:

- How to create a dictionary
- How to get, set, and add items
- How to delete items
- How to loop through keys and values
- How to convert between dictionaries and lists
- The Country Code program
- The Word Counter program
- How to use the merge and update operators
- How to use dictionaries with complex objects as values
- The Book Catalog program

## Files

- `code/chapter12/chapter12_dictionaries.py` - Basic dictionary operations and examples
- `code/chapter12/country_codes.py` - Country Code program
- `code/chapter12/word_counter.py` - Word Counter program
- `code/chapter12/book_catalog.py` - Book Catalog program
- `code/chapter12/practice_ch12.py` - Practice exercises

## How to Run

```bash
python code/chapter12/chapter12_dictionaries.py
python code/chapter12/country_codes.py
python code/chapter12/word_counter.py
python code/chapter12/book_catalog.py
python code/chapter12/practice_ch12.py
```

---

# Chapter 13 - How to Work with Recursion and Algorithms

This chapter covers:

- An introduction to recursion
- How recursion works in Python
- How to use recursion to add a range of numbers
- How to compute the factorial of a number
- How to compute a Fibonacci series
- The Towers of Hanoi puzzle
- The recursive algorithm for solving the Towers of Hanoi puzzle

## Files

- `code/chapter13/chapter13_recursion.py` - Demonstrates recursion by adding a range of numbers
- `code/chapter13/factorial.py` - Computes the factorial of a number using recursion
- `code/chapter13/fibonacci.py` - Computes a Fibonacci series using recursion
- `code/chapter13/towers_of_hanoi.py` - Demonstrates the recursive solution to the Towers of Hanoi puzzle
- `code/chapter13/practice_ch13.py` - Practice with recursive functions

## How to Run

```bash
python code/chapter13/chapter13_recursion.py
python code/chapter13/factorial.py
python code/chapter13/fibonacci.py
python code/chapter13/towers_of_hanoi.py
python code/chapter13/practice_ch13.py
```

---

# Presentation Slides

The presentation slides for Chapters 9-13 are located in the `slides/` folder.

Included presentations:

- `slides/chapter09_numbers_workshop.pptx`
- `slides/chapter_10_How_to_Work_with_Strings.pptx`
- `slides/chapter_11_Dates_and_Times.pptx`
- `slides/chapter_12_How_to_Work_with_Dictionaries.pptx`
- `slides/chapter_13_How_to_Work_with_Recursion_and_Algorithms.pptx`

---

# Replication Instructions

To verify this project:

1. Clone the repository.
2. Enter the `murachs_python_section_2` folder.
3. Run the lesson and practice files using the commands provided above.
4. Confirm that each Python program runs without runtime errors.
5. Check the `slides/` folder for the presentation files.

The Python programs in this repository use Python's standard library and do not require external packages.