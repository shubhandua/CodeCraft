import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    min_heap = []
    
    # Step 1: Push the first node of each list into the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))  # Store (value, index, node)
    
    dummy = ListNode(0)
    current = dummy

    # Step 2: Extract the smallest element and push the next node from the same list
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
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
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

print("Merged sorted linked list:")
merged_head = merge_k_sorted_lists(lists)
print_linked_list(merged_head)
