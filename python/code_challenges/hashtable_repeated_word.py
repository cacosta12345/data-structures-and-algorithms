from data_structures.hashtable import Hashtable
import re

def first_repeated_word(s):
    # Ensure punctuation is effectively treated as space, splitting words correctly.
    words = re.findall(r'\b\w+\b', s.lower())
    
    hash_table = Hashtable(len(words))  # Assume Hashtable is already defined.
    
    for word in words:
        if hash_table.has(word):
            return word
        else:
            hash_table.set(word, True)
    
    return None

