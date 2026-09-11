# Chapter 13 - How to Work with Recursion and Algorithms
# How to Compute the Factorial of a Number


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = 5

    result = factorial(number)

    print("Factorial of", number, "is", result)


if __name__ == "__main__":
    main()
