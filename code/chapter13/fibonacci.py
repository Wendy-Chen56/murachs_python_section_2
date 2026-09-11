# Chapter 13 - How to Work with Recursion and Algorithms
# How to Compute a Fibonacci Series


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    count = 10

    print("Fibonacci series:")

    for i in range(count):
        print(fibonacci(i), end=" ")

    print()


if __name__ == "__main__":
    main()
