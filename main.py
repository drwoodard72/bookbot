from stats import get_num_words
from stats import get_num_characters

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def main():
    book_file_path="./books/frankenstein.txt"
    book_text = get_book_text(book_file_path)
    book_word_count = get_num_words(book_text)
    book_character_counts = get_num_characters(book_text)

    print(book_word_count)
    print(book_character_counts)


main()
