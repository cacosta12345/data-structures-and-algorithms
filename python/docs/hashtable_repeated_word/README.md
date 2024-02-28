# Hashtable Repeated Word

Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

## Whiteboard Process
![whiteboard]()

## Approach & Efficiency
Preprocess the String: It first converts the string to lowercase and uses the re.findall method with the regular expression '\w+' to split the string into words. This approach also removes punctuation, making the function capable of comparing words irrespective of punctuation marks.

Hashtable to Track Words: It initializes a Hashtable object with a size equal to the number of words in the input string. This is just for optimization; the size can be adjusted based on expected input sizes or left as the default.

Iterate and Check: As it iterates through the list of words, it checks whether each word has already been added to the hashtable. If a word is found in the hashtable, it means this is the first repeated word, so the function returns it. If the word is not found, it's added to the hashtable.

Return None: If the function completes the loop without finding any repeated word, it returns None.

## Solution

[Link to Code](../../code_challenges/hashtable_repeated_word.py)

# Example usage
text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."

repeated_word = first_repeated_word(text)

print(f"The first repeated word is: '{repeated_word}'")

Output: The first repeated word is: 'it'