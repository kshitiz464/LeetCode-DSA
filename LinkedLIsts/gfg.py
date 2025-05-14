# # Python3 program to remove duplicate
# # nodes from a sorted linked list
#
# # Node class
#
#
# class Node:
#
#     # Constructor to initialize
#     # the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # Function to insert a new node
#     # at the beginning
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     # Given a reference to the head of a
#     # list and a key, delete the first
#     # occurrence of key in linked list
#     def deleteNode(self, key):
#
#         # Store head node
#         temp = self.head
#
#         # If head node itself holds the
#         # key to be deleted
#         if (temp is not None):
#             if (temp.data == key):
#                 self.head = temp.next
#                 temp = None
#                 return
#
#         # Search for the key to be deleted,
#         # keep track of the previous node as
#         # we need to change 'prev.next'
#         while(temp is not None):
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next
#
#         # if key was not present in
#         # linked list
#         if(temp == None):
#             return
#
#         # Unlink the node from linked list
#         prev.next = temp.next
#
#         temp = None
#
#     # Utility function to print the
#     # linked LinkedList
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data, end=' ')
#             temp = temp.next
#
#     # This function removes duplicates
#     # from a sorted list
#     def removeDuplicates(self):
#         temp = self.head
#         print("temp = ", temp.data)
#         if temp is None:
#             return
#         while temp.next is not None:
#             print("while stat", temp.data, temp)
#             if temp.data == temp.next.data:
#                 temp.next = temp.next.next
#                 print("inside if statement:", temp.next.data)
#             else:
#                 temp = temp.next
#                 print("inside else stat:", temp.data, temp)
#         print("end head= ", self.head.data, self.head)
#         return self.head
#
#
# # Driver Code
#
# # A = [2, 5, 1, 55, 2, 3]
# llist = LinkedList()
# # for i in A:
# #     llist.push(i)
# llist.push(20)
# llist.push(13)
# llist.push(13)
# llist.push(11)
# llist.push(11)
# llist.push(11)
# print("Created Linked List: ")
# llist.printList()
# print()
# print("Linked List after removing",
#       "duplicate elements:")
# llist.removeDuplicates()
# llist.printList()
#
# # This code is contributed by
# # Dushyant Pathak.


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_sort_bottom_up(head):
    if not head or not head.next:
        return head

    length = get_length(head)
    size = 1
    dummy = ListNode()
    dummy.next = head

    while size < length:
        current = dummy.next
        tail = dummy

        while current:
            left = current
            right = split(left, size)
            current = split(right, size)
            tail = merge(left, right, tail)

        size *= 2

    return dummy.next


def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def split(head, size):
    if not head:
        return None
    for _ in range(size - 1):
        if head.next:
            head = head.next
        else:
            break
    next_head = head.next
    head.next = None
    return next_head


def merge(left, right, head):
    current = head
    while left and right:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next

    current.next = left if left else right

    while current.next:
        current = current.next

    return current


# Utility function to print the linked list
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("NULL")


# Example usage
if __name__ == "__main__":
    # Example 1
    head1 = ListNode(15)
    head1.next = ListNode(10)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(20)
    head1.next.next.next.next = ListNode(3)
    head1.next.next.next.next.next = ListNode(2)
    print_list(head1)
    sorted_head1 = merge_sort_bottom_up(head1)
    print("Unsorted List:")
    print_list(head1)
    print("Sorted List:")
    print_list(sorted_head1)



