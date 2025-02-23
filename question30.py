def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

    for char in expression:
        if char in "({[":
            stack.append(char)  # Push opening brackets
        elif char in ")}]":
            if not stack or stack.pop() != bracket_map[char]:  # Check matching
                return False

    return len(stack) == 0  # If stack is empty, it's balanced

# Example Usage
expressions = ["{[()]}", "{[(])}", "{{[[(())]]}}", "((()))", "({[)]}"]

for expr in expressions:
    print(f"{expr}: {'Balanced' if is_balanced(expr) else 'Not Balanced'}")
