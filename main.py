import sys
import os
from stats import get_num_words, get_char_count, sort_char_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        if os.path.isfile(book_path):
            book = get_book_text(book_path)
            word_count = get_num_words(book)
            char_count = get_char_count(book)
            sorted_chars_by_num = sort_char_dict(char_count)
        
            # Print the Report
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {book_path}...")
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words")
            print("--------- Character Count -------")
            for item in sorted_chars_by_num:
                if item["char"].isalpha():
                    print(f"{item["char"]}: {item["num"]}")
            print("============= END ===============")
        else:
            print(f"{book_path} is not a valid path")
            sys.exit(2)

main()