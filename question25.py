class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to reverse a linked list
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to add 1 to the number represented by the linked list
def add_one(head):
    # Step 1: Reverse the linked list
    head = reverse_list(head)

    # Step 2: Add 1 to the first node
    carry = 1
    current = head

    while current:
        current.val += carry
        if current.val < 10:
            carry = 0
            break
        else:
            current.val = 0
            carry = 1
        if not current.next and carry:
            current.next = ListNode(1)
            carry = 0
        current = current.next

    # Step 3: Reverse the linked list back
    return reverse_list(head)

# Helper function to create a linked list from a number
def create_linked_list_from_number(num):
    head = None
    for digit in str(num):
        if not head:
            head = ListNode(int(digit))
            current = head
        else:
            current.next = ListNode(int(digit))
            current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage
num = 1299  # Input number as a linked list (1 -> 2 -> 9 -> 9)
head = create_linked_list_from_number(num)

print("Original linked list:")
print_linked_list(head)

head = add_one(head)

print("Linked list after adding 1:")
print_linked_list(head)
