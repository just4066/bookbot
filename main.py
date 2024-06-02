def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path) 
           
def read_book(book_path):
    with open (book_path) as f:
        return f.read()
            
def count_words(files_contents):
    words = files_contents.split()
    return len(words)

def count_caracters(text):
    list_of_words = text.split()
    dict_of_caracters = {}
    
    for word in list_of_words:
        lowered_word = word.lower()
        
        for caracter in lowered_word:
            if caracter in dict_of_caracters:
                dict_of_caracters[caracter] += 1
            else:
                dict_of_caracters[caracter] = 1

    return dict_of_caracters

def sort_caracters(caracters_count):
    return sorted(caracters_count.items(), key=lambda x: x[1], reverse=True)

def print_report(text_path):
    text = read_book(text_path)
    words_count = count_words(text)
    caracters_count = count_caracters(text)
    sorted_caracters = sort_caracters(caracters_count)
    
    print(f"--- Begin report of {text_path} ---")
    print(f"{words_count} words in the document\n\n")
    
    for caracter, count in sorted_caracters:
        if caracter.isalpha():
            print(f"The caracter '{caracter}' was found {count} times")
      
main()