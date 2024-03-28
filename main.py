from collections import Counter


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
    count_words(file_contents)
    char_dict = count_characters(file_contents)
    print(char_dict)


def count_words(text):
    count = len(text.split())
    print("There are {} words in the text".format(count))

def count_characters(text):
    char_dict = Counter(text)
    return char_dict.most_common()

if __name__ == "__main__":
    main()

