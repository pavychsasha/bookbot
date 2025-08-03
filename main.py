import sys
from stats import get_words_count, get_sorted_num_of_char

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def print_words_count(text: str) -> None:
    num_words = get_words_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def print_character_count(text: str) -> None:
    print("--------- Character Count -------")
    sorted_char_list = get_sorted_num_of_char(text)
    for char_info in sorted_char_list:
        print(f"{char_info["char"]}: {char_info["num"]}")



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    content = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..")


    print_words_count(content)
    print_character_count(content)

    print("============= END ===============")

main()
