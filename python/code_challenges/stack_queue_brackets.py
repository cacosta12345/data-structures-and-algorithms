def multi_bracket_validation(input_string):
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    # Initialize an empty stack
    stack = []

    # Iterate through each character in the input string
    for char in input_string:
        # If the character is an opening bracket, push it onto the stack
        if char in "([{":
            stack.append(char)
        # If the character is a closing bracket
        elif char in ")]}":
            # If the stack is empty or the top of the stack doesn't match the corresponding opening bracket, return False
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            # Pop the opening bracket from the stack
            stack.pop()

    # If the stack is empty, the brackets are balanced, return True; otherwise, return False
    return len(stack) == 0

# You can now run your test file on this function.
