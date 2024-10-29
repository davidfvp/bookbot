def count_words(content):
    return len(content.split())

def count_letters(content):
    letters = {}
    for c in content.lower():
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters

def read_content(file_name):
    with open(file_name, "r") as file:
        return file.read()

def print_report(file_name):
        content = read_content(file_name)
        print("--- Begin report of {file_name} ---")
        print(f"{count_words(content)} words found in the document")
        print()
        letters = count_letters(content)
        for letter in dict(sorted(letters.items(), key=lambda item: item[1], reverse=True)):
            if (letter.isalpha()):
                print(f"The '{letter}' character was found {letters[letter]} times")
        print("--- End report ---")

def main():
    print_report("books/frankenstein.txt")


main()