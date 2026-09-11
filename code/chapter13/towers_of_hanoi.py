# Chapter 13 - How to Work with Recursion and Algorithms
# Towers of Hanoi


def move_disks(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
    else:
        move_disks(n - 1, source, auxiliary, destination)

        print("Move disk", n, "from", source, "to", destination)

        move_disks(n - 1, auxiliary, destination, source)


def main():
    number_of_disks = 3

    print("Towers of Hanoi")
    print("Number of disks:", number_of_disks)
    print()

    move_disks(number_of_disks, "A", "C", "B")


if __name__ == "__main__":
    main()
