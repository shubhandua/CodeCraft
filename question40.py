def longest_valid_parentheses(s):
    stack = [-1]  # Initialize stack with -1 for base case
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Store index of '('
        else:
            stack.pop()  # Match ')'
            if stack:
                max_length = max(max_length, i - stack[-1])  # Update max length
            else:
                stack.append(i)  # Store index of unmatched ')'

    return max_length

# Example Usage
s = "(()))())("
print("Length of Longest Valid Parentheses Substring:", longest_valid_parentheses(s))
