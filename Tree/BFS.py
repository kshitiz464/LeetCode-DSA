from collections import defaultdict
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class tree():
    @staticmethod
    def height(node):
        if node is None:
            return 0
        else:
            lheight = tree.height(node.left)
            rheight = tree.height(node.right)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

    @staticmethod
    def bfs_iter(root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].data)
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    @staticmethod
    def iter_inorder(root):
        curr = root
        stack = []

        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.data, end = " ")
                curr = curr.right
            else:
                break
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# tree.bfs_iter(root)
inorder = tree.iter_inorder(root)


