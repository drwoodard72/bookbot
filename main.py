def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def get_word_count(text):
    return f"{len(text.split())} words found in the document"

def main():
    book_file_path="./books/frankenstein.txt"
    #print(get_book_text(book_file_path))
    print(get_word_count(get_book_text(book_file_path)))

main()