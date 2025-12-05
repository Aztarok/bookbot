from stats import final_report, get_word_count, get_character_count, sort_book
import sys

def get_book_text(filePath):
    with open(filePath, "r") as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = ""
    if sys.argv[1:]:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    whole_book = get_book_text(file_path)
    word_count = get_word_count(whole_book)
    character_count = get_character_count(whole_book)
    book_sorted = sort_book(character_count)

    final_report(file_path, word_count, book_sorted)

if __name__ == "__main__":
    main()
