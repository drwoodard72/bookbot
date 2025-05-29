from stats import get_word_count
from stats import get_num_characters
from stats import get_sorted_char_counts
import sys

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_path=sys.argv[1]
    book_text = get_book_text(book_file_path)
    book_word_count = get_word_count(book_text)
    sorted_char_counts = get_sorted_char_counts(get_num_characters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for char_count in sorted_char_counts:
        if char_count["char"].isalpha() == True:        
            print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")


main()
