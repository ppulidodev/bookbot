def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    word_number = count_words(text)
    character_count = count_characters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_number} words found in the document")
    for e in character_count:
        print(f"The {e} character was found {character_count[e]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict


main()