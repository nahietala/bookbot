from stats import word_count, characters, sort_chars
import sys

#Setting sys.argv and exit parameters
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

#Bookbot primary function
def main():
    bk_word_count = word_count(path)
    bk_char_dict = characters(path)
    sorted_chars = sort_chars(bk_char_dict)
    print_report(path, bk_word_count, sorted_chars)

#Sorting book characters
def print_report(path, bk_word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count -----------")
    print(f"Found {bk_word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict["count"]}")
    print("============= END ===============")

main()
