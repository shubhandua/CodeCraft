class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_last_occurrence(self, key):
        last_occurrence = None
        temp = self.head
        prev = None
        last_occurrence_prev = None

        while temp:
            if temp.data == key:
                last_occurrence = temp
                last_occurrence_prev = prev
            prev = temp
            temp = temp.next

        if last_occurrence:
            if last_occurrence_prev:  # If not the head node
                last_occurrence_prev.next = last_occurrence.next
            else:  # If the last occurrence is the head node
                self.head = self.head.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(5)
ll.append(2)
ll.append(10)

print("Original List:")
ll.print_list()

ll.delete_last_occurrence(2)

print("After deleting last occurrence of 2:")
ll.print_list()
