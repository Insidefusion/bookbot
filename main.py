import sys
from stats import get_num_words, get_chars_dict, get_sort_chars

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sort_chars(chars_dict)
    print_report(book_path, num_words, sorted_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
