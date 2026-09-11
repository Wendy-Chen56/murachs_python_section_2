# Chapter 13 - How to Work with Recursion and Algorithms
# Introduction to Recursion


def add_numbers(n):
    if n == 1:
        return 1
    else:
        return n + add_numbers(n - 1)


def main():
    number = 5

    total = add_numbers(number)

    print("Add the numbers from 1 to", number)
    print("Total:", total)


if __name__ == "__main__":
    main()
