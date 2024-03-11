# Hashtable left join



## Whiteboard Process
![whiteboard]()

## Approach & Efficiency

The `left_join` function performs a left join operation on two hashmaps, specifically designed for a use case involving synonyms and antonyms dictionaries. Here's a breakdown of how the function operates:

1. **Initialization of Result Container**: The function starts by initializing an empty list named `result`. This list will eventually contain the output of the left join operation, formatted as a list of lists. Each sublist will include a word (key from the synonyms dictionary) and its corresponding synonym and antonym.

2. **Iteration Over Synonyms Dictionary**: The function iterates over each key-value pair in the `synonyms` dictionary. This iteration ensures that each word and its synonym are considered for the left join operation.

3. **Retrieval of Corresponding Antonym**: For each word encountered in the synonyms dictionary, the function attempts to find a corresponding antonym in the `antonyms` dictionary using the `.get()` method. This method is chosen because it allows for a default value to be specified ("NONE" in this case) if the word does not exist in the `antonyms` dictionary. This step is crucial for implementing the "left join" logic, ensuring that all entries from the `synonyms` dictionary are included in the result, regardless of whether they have a corresponding entry in the `antonyms` dictionary.

4. **Construction of Sublists**: For each word, a sublist is created containing the word itself, its synonym (retrieved from the `synonyms` dictionary), and its antonym (retrieved from the `antonyms` dictionary or defaulted to "NONE"). This sublist represents a single record of the left join operation.

5. **Aggregation of Results**: Each sublist created in the previous step is appended to the `result` list. This step is repeated for every word in the `synonyms` dictionary, aggregating all the left join records into a single list.

6. **Returning the Final Result**: After processing all entries in the `synonyms` dictionary, the function returns the `result` list. This list contains sublists, each of which represents a word and its associated synonym and antonym (if available), effectively completing the left join operation between the two provided dictionaries.

By following these steps, the `left_join` function efficiently combines data from two related hashmaps, providing a structured way to explore relationships between words, their synonyms, and antonyms.


## Solution

[Link to Code](../../code_challenges/hashtable_left_join.py)

# Example usage

Synonyms Hash Table	 	 	Antonyms Hash Table	 
Key	Value	 	Key	Value
diligent	employed	 	diligent	idle
fond	enamored	 	fond	averse
guide	usher	 	guide	follow
outfit	garb	 	flow	jam
wrath	anger	 	wrath	delight
…	…	 	…	…
OUTPUT
[
   ["font", "enamored", "averse"],
   ["wrath", "anger", "delight"],
   ["diligent", "employed", "idle"],
   ["outfit", "garb", NULL],
   ["guide", "usher","follow"]
]