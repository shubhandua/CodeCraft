class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify the merge process
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append the remaining nodes
    current.next = l1 if l1 else l2

    return dummy.next  # Return the merged sorted list

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
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 5])

print("Merged sorted linked list:")
merged_head = merge_two_sorted_lists(l1, l2)
print_linked_list(merged_head)
