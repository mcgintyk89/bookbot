import sys
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
    
from stats import count_words
from stats import character_count
from stats import sort_on

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    char_count = character_count(text)
    sorted_char_count = sort_on(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_char_count:
        char_string = char_data["char"]
        char_count_value = char_data["num"]
        if char_string.isalpha():
            print(f"{char_string}: {char_count_value}")
    print("============= END ===============")


main()