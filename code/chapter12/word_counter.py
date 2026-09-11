# Chapter 12 - The Word Counter Program

def main():
    text = input("Enter some text: ")

    words = text.split()

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\nWord Counts")
    for word, count in word_count.items():
        print(word, count)


if __name__ == "__main__":
    main()
