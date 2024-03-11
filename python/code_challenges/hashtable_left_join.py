from data_structures.hashtable import Hashtable


def left_join(synonyms, antonyms):
    """
    Perform a left join on two hashmaps.

    :param synonyms: A dictionary of word strings as keys and synonyms as values.
    :param antonyms: A dictionary of word strings as keys and antonyms as values.
    :return: A list of lists, where each sublist contains a key from the first hashmap and its corresponding values from both hashmaps.
    """
    result = []

    # Iterate over the keys in the synonyms dictionary to maintain order
    for key in synonyms:
        synonym = synonyms[key]
        antonym = antonyms.get(key, "NONE")  # Use .get() to handle missing keys with a default value of "NONE"
        result.append([key, synonym, antonym])

    return result

