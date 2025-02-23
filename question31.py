def delete_middle(stack, current_index=0):
    # Base case: If stack is empty, return
    if not stack:
        return
    
    middle_index = len(stack) // 2  # Find middle index

    # Base case: If we reached the middle, remove it
    if current_index == middle_index:
        stack.pop()
        return
    
    # Store the top element and remove it
    temp = stack.pop()

    # Recursive call to reach the middle
    delete_middle(stack, current_index + 1)

    # Push back stored elements after deletion
    stack.append(temp)

# Example Usage
stack = [1, 2, 3, 4, 5]  # Stack representation (top -> bottom)

print("Original Stack:", stack)
delete_middle(stack)
print("Stack after deleting middle element:", stack)
