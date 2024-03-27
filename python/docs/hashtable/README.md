# Hashtable implementation

## Approach & Efficiency

### Methods

- `set(key, value)`: Inserts a key-value pair into the hashtable.
- `get(key)`: Retrieves the value associated with a given key.
- `has(key)`: Checks if a key exists in the hashtable.
- `keys()`: Returns a collection of keys in the hashtable.
- `display()`: Displays the contents of the hashtable.

## Solution

[Link to Code](../../data_structures/hashtable.py)

## Example usage

### Create a hashtable
hashtable = Hashtable()

### Insert key-value pairs
hashtable.set("apple", 10)
hashtable.set("banana", 20)

### Retrieve values
print(hashtable.get("apple"))  # Output: 10

### Check key existence
print(hashtable.has("banana"))  # Output: True

### Display hashtable contents
print(hashtable.display())