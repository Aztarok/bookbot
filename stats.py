def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    character_count = {}

    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def sort_on(items):
    return items["num"]

def sort_book(book_dictionary):
    sorted_list = []
    for char in book_dictionary:
        sorted_list.append({
            "char": char,
            "num": book_dictionary[char]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def final_report(file_path, word_count, book_sorted):
    print(12 * "=" + " BOOKBOT " + 12 * "=")
    print(f"Analyzing book found at {file_path}...")
    print(11 * "-" + " Word Count " + 10 * "-")
    print(f"Found {word_count} total words")
    print(9 * "-" + " Character Count " + 7 * "-")

    for char in book_sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print(13 * "=" + " END " + 15 * "=")
