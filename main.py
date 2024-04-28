def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_words = get_words(book_text)
    words_count = get_word_count(book_words)
    letter_count = get_letter_count(book_text)
    sorted_dict = sort_dict_by_number(letter_count)
  
    print_report(book_path, words_count, sorted_dict)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_words(text):
    return text.split()

def get_word_count(words):
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    lowercased_text = text.lower()
    for letter in lowercased_text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    
    return letter_dict


        
def print_report(path, word_count, dictionnary):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")

    for letter in dictionnary:
        if letter.isalpha():
            print(f"the '{letter}' character was found {dictionnary[letter]} times")    

def sort_dict_by_number(dictionary):
    # Sort the dictionary items by their values (counts)
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1])
    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(sorted_items)
    return sorted_dict

main()