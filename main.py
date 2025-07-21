import sys
from stats import get_book_text, get_num_words, get_character_counts, get_sorted_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relative_book_path = sys.argv[1]
    text = get_book_text(fp=relative_book_path)
    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    counts = get_character_counts(text)
    # print(counts)
    sorted_counts = get_sorted_counts(counts)
    # print(sorted_counts)
    pruned_sorted_counts = [f"{x['char']}: {x['num']}" for x in sorted_counts if x["char"].isalpha()]

    response = (
        "============ BOOKBOT ============\n"
        f"Analyzing book found at {relative_book_path}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------")

    print(response)
    for count in pruned_sorted_counts:
        print(count)
    print("============= END ===============")

if __name__ == "__main__":
    main()