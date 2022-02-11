import string
import nltk
from nltk.corpus import words, names
import re

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

## Created dict of lower and upper case letters and their corresponding numbers
upper = dict(zip(string.ascii_uppercase, range(1,27)))
lower = dict(zip(string.ascii_lowercase, range(1,27)))
# Created a list of keys and values for easier pulls by index
key_up = list(upper.keys())
val_up = list(upper.values())
key_low = list(lower.keys())
val_low = list(lower.values())



def encrypt(plain, key):
    word_list = list(plain)
    if key > 26:
        key = 26 - (key%26) 
    new_word = ''
    for letter in word_list:
        if letter in upper.keys():
            let_key = upper.get(letter)+key
            if let_key > 26:
                let_key = let_key - 26
            new_letter = key_up[let_key-1]
            new_word += new_letter
        elif letter in lower.keys():
            let_key = lower.get(letter)+key
            if let_key > 26:
                let_key = let_key - 26
            new_letter = key_low[let_key-1]
            new_word += new_letter
        else:
            new_word += letter
    return new_word


def decrypt(encrypted, key):
    return encrypt(encrypted, -key)


def crack(encrypted):
    words_list = words.words()
    x = 0
    while x < 26:
        x = x + 1 
        ## This will be the final return
        decrypt = encrypt(encrypted, x)
        ## This manipulates the data to ensure it matches the same style as the words_list
        decrypt_low = re.sub(r'[^\w\s]', '', encrypt(encrypted, x)).lower().split(' ')
        if all(i in words_list for i in decrypt_low):
            return decrypt
    ## Added this return to overwrite None return
    return ''








# if __name__ == "__main__":
#     phrase = 'Hey how are you'
#     # encryp = encrypt(phrase, 6)
#     print(encrypt(phrase, 4))
#     print(crack(phrase))