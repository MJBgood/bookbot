def get_book_text(fp: str) -> str:
    with open(fp, "r") as f:
        return f.read()

def get_num_words(text: str) -> int:
    return len(text.split())

def get_character_counts(text: str) -> dict:
    counts = {}
    for char in text:
        safe_char = char.lower()
        char_count = counts.get(safe_char, 0)
        counts[safe_char] = char_count + 1

    return counts

def get_sorted_counts(counts: dict) -> list:
    unsorted = []
    for k, v in counts.items():
        unsorted.append({"char": k, "num": v})

    def sort_on(items):
        return items["num"]

    unsorted.sort(reverse=True, key=sort_on)

    return unsorted