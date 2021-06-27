from typing import List

my_words = ['cat', 'dog', 'ear', 'car', 'elephant']

def uppercase_words(words: List[str] = my_words) -> None:
    """Print out each string in a list in all caps"""
    for word in words:
        print(word.upper())

print(uppercase_words())


def only_words_that_start_with_e(words: List[str] = my_words) -> None:
    """This function will only print out words that begin with the 
       letter e, whether uppercase or lowercase."""
    for word in words:
        if word[0].lower() == 'e':
            print(word.upper())

print(only_words_that_start_with_e())


def only_certain_letters(accepted_letters: List[str] = ['c', 'd'], 
                         words: List[str] = my_words) -> None:
    """This function will only print out words in 
       uppercase that begin with one of the letters 
       in accepated letters."""
    for word in words:
        if word[0].lower() in accepted_letters:
            print(word.upper())

print(only_certain_letters())