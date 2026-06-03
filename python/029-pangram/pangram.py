import string

def is_pangram(sentence):
    return all(letter in set(sentence.lower()) for letter in string.ascii_lowercase)
