# from kshitiz import LinkedList
from LinkedList import SLL1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = 0

class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


class SLL2(SLL1.SLL):
    def reverse_by_group_size(self, head, k):
        if head is None:
            return None
        curr = head
        next = None
        prev = None
        count = 0

        while (curr is not None) and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next is not None:
            head.next = self.reverse_by_group_size(next, k)
        return prev

    @staticmethod
    def detect_loop_flag(head):
        while head is not None:
            if head.flag == 1:
                return True
            head.flag = 1
            head = head.next
        return False

    @staticmethod
    def detect_loop_hashing(head):
        while head is not None:
            node_set = set()
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False

    @staticmethod
    def find_loop_start(head):
        if head is None or head.next is None:
            return None
        sp, fp = head, head
        while fp and fp.next:
            sp, fp = sp.next, fp.next.next
            if sp == fp:
                sp = head
                while sp != fp:
                    sp, fp = sp.next, fp.next
                return sp

    @staticmethod
    def remove_loop_hashing(head):
        s = set()
        prev = None
        while head:
            if head in s:
                prev.next = None
                return True
            s.add(head)
            prev = head
            head = head.next

    @staticmethod
    def remove_loop_floyd(head):
        if head is None or head.next is None:
            return None
        sp = head
        fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

            if sp == fp:
                sp = head
                while sp != fp:
                    sp = sp.next
                    fp = fp.next
                while fp.next != sp:
                    fp = fp.next
                fp.next = None
                return True

    def remove_duplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return self.head

    def move_last_to_first(self):
        last = self.head
        sec_last = None
        while last.next is not None:
            sec_last = last
            last = last.next
            # print(last.data, sec_last.data)
        sec_last.next = None
        last.next = self.head
        self.head = last
        return self.head

    def add_1(self):
        temp = self.head
        d = 0
        while temp:
            d = d*10 + temp.data
            temp = temp.next
        d = d + 1
        temp = self.head
        prev = None
        for i in str(d):
            if temp:
                temp.data = int(i)
            else:
                node = Node(int(i))
                prev.next = node
                temp = prev
            prev = temp
            temp = temp.next
        return self.head

    def add_2_ll(self,num1,num2):
        head1, head2 = num1, num2
        d1 = 0
        d2 = 0
        while head1:
            d1 = d1*10 + head1.data
            head1 = head1.next
        while head2:
            d2 = d2*10 + head2.data
            head2 = head2.next
        del num2
        d1 += d2
        head1 = num1
        prev = None

        for i in str(d1):
            if head1:
                head1.data = int(i)
            else:
                node = Node(int(i))
                prev.next = node
                head1 = prev
            #     this didn't work when reversed list as numbers were passed
            #  this worked:
            #     node = Node(int(i))
            #     head1 = node
            #     prev.next = head1
            prev = head1
            head1 = head1.next

        return num1

    @staticmethod
    def intersetPoint(head1, head2):
        # Better approach with O(0) space
        p1, p2 = head1, head2
        if not p1 or not p2:
            return None
        while p1 and p2:
            p1 = p1.next if p1 else head2
            p2 = p2.next if p2 else head1
            # print(p1.data, p2.data)
        return p1.data
        # this approach takes space O(m)
        # p1, p2 = head1, head2
        # s = set()
        # while p1:
        #     s.add(p1)
        #     p1 = p1.next
        # while p2:
        #     if p2 in s:
        #         return p2.data
        #     p2 = p2.next
        # return None

    @staticmethod
    def get_len(head):
        len = 0
        while head:
            len += 1
            head = head.next
        return len

    @staticmethod
    def split(head, size):
        if not head:
            return None
        for i in range(size - 1):
            if head.next:
                head = head.next
            else:
                break
        next_head = head.next
        head.next = None
        return next_head

    @staticmethod
    def merge(left, right, head):
        curr = head
        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        while curr.next:
            curr = curr.next
        return curr

    @staticmethod
    def mergeSort(head):
        # head = self.head
        if not head or not head.next:
            return head
        length = SLL2.get_len(head)
        size = 1
        dummy = ListNode()
        dummy.next = head

        while size < length:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = SLL2.split(left, size)
                curr = SLL2.split(right, size)
                tail = SLL2.merge(left, right, tail)
            size *= 2
        return dummy.next









def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")


A = [2, 5, 1, 55, 2, 3]

llist = SLL2()
llist.insertAtBegin(5)
llist.insertAtBegin(4)
llist.insertAtBegin(1)
llist.insertAtBegin(9)
llist.insertAtBegin(23)
llist.insertAtBegin(2)

# llist2 = SLL2()
# llist2.insertAtBegin(5)
# llist2.insertAtBegin(4)
# llist2.insertAtBegin(3)
# llist2.insertAtBegin(1)
# llist2.insertAtBegin(1)
# llist2.insertAtBegin(1)
# head = ListNode(A[0])
# for i in range(1,len(A)):
#     curr = head
#     curr.next = ListNode(A[i])
#     curr = curr.next
#     print(curr.data)

print("before removing duplicates")
# print_list(head)
llist.printLL()


print("after removing duplicates")
newhead = llist.mergeSort(llist.head)
# print(llist.head.data)
print_list( newhead)
# llist2.printLL()
