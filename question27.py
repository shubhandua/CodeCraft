class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)  # Dummy node to handle edge cases
    dummy.next = head
    slow, fast = dummy, dummy

    # Step 1: Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Step 2: Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Delete the nth node
    slow.next = slow.next.next

    return dummy.next  # Return new head

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original linked list:")
print_linked_list(head)

n = 2  # Remove 2nd node from end
head = remove_nth_from_end(head, n)

print(f"Linked list after removing {n}th node from end:")
print_linked_list(head)
