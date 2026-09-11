# Chapter 13 Practice
# Recursion and Algorithms


# Practice 1: Complete the recursive function
# to add the numbers from 1 to n.

def add_numbers(n):
    if n == 1:
        return 1
    else:
        return n + add_numbers(n - 1)


# Practice 2: Complete the recursive factorial function.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    print("Recursion Practice")
    print()

    print("Sum from 1 to 5:", add_numbers(5))
    print("Factorial of 5:", factorial(5))


if __name__ == "__main__":
    main()
