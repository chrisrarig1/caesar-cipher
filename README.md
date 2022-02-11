# Cryptography

- Create an *encrypt* function that takes in a plain text phrase and a numeric shift
- Create a *decrypt* function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
- Create a *crack* function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

## Approach

### Encrypt

- I felt it was easiest to generate a dictionary of both upper and lower case words with numbers as their values
- Using this I was able to shift through the dictionaries returning the matching key for the new shifted value

### Decrypt

- Roger gave us this one in class. Just invoke the encrypt function with a negative key value

### Crack

- I used a brute force method trying every possible shift until all words were in the list of python given English words.
- To account for upper case and punctuation I removed them before comparing to the list

## Resources Used

- For the *all* function: https://www.w3schools.com/python/ref_func_all.asp
- For the *regex*: https://regex101.com/
