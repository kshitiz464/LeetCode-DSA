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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_in_groups(self, head, k):
        if head is None:
            return None
        current = head
        next_node = None
        prev = None
        count = 0
        # Reverse first k nodes of the linked list
        while current is not None and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        # next_node is now pointing to (k+1)th node
        # Recursively call for the list starting from current.
        # And make rest of the list as next of first node
        if next_node is not None:
            head.next = self.reverse_in_groups(next_node, k)

        # prev is new head of the input list
        return prev

    def reverse_groups(self, k):
        self.head = self.reverse_in_groups(self.head, k)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create linked list and append elements from A
linked_list = LinkedList()
A = [2, 5, 1, 55, 2, 3]
for item in A:
    linked_list.append(item)

print("Original list:")
linked_list.print_list()

# Reverse in groups of 2
k = 2
linked_list.reverse_groups(k)

print(f"List after reversing in groups of {k}:")
linked_list.print_list()
