class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)

        position = 0
        current_node = self.head
        while (current_node != None and position + 1 != index):
            position = position + 1
            current_node = current_node.next

            if current_node != None:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present.")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    def remove_last_node(self):

        if self.head is None:
            return

        curr_node = self.head
        while (curr_node.next != None and curr_node.next.next != None):
            curr_node = curr_node.next

        curr_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        current_node = self.head

        # Check if the head node contains the specified data
        if current_node.data == data:
            self.remove_first_node()
            return

        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def iter_search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def recu_search(self, key):
        return self.recu_search_node(self.head, key)

    def recu_search_node(self, curr, key):
        if curr is None:
            return False
        if curr.data == key:
            return True
        return self.recu_search_node(curr.next, key)

    def iter_reverse_list(self):
        curr = self.head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    def recu_reverse(self):
        self.head = self._recu_reverse_list(self.head,None)
    def _recu_reverse_list(self, curr, prev=None):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        return self._recu_reverse_list(next_node,curr)

    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size = size + 1
                current_node = current_node.next
            return size
        else:
            return 0

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# A = [2, 5, 1, 55, 2, 3]
# Inst = SLL()
# for i in A:
#     Inst.insertAtEnd(i)
# # print(Inst.iter_search(4))
# # print(Inst.recu_search(2))
# # Inst.iter_reverse_list()
# Inst.recu_reverse()
#
# Inst.printLL()
#
# print("\nSize of linked list :", end=" ")
# print(Inst.sizeOfLL())

# add nodes to the linked list
# llist.insertAtEnd('a')
# llist.insertAtEnd('b')
# llist.insertAtBegin('c')
# llist.insertAtEnd('d')
# llist.insertAtIndex('g', 2)
#
# # print the linked list
# print("Node Data")
# llist.printLL()
#
# # remove a nodes from the linked list
# print("\nRemove First Node")
# llist.remove_first_node()
# print("Remove Last Node")
# llist.remove_last_node()
# print("Remove Node at Index 1")
# llist.remove_at_index(1)
#
# # print the linked list again
# print("\nLinked list after removing a node:")
# llist.printLL()
#
# print("\nUpdate node Value")
# llist.updateNode('z', 0)
