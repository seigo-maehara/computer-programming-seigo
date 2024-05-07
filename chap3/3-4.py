class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def __str__(self):
        if self.value is None:
            return ""
        else:
            return self.value

    def set_nodes(self, x, y):
        self.left, self.right = x, y
        return self

count = 0


def preorder(n):
    if n == None:
        return count
    else:
        count = count + 1
        preorder(n.left)
        preorder(n.right)


class Tree:
    def __init__(self, root_node):
        self.root = root_node
    
    def size(self):
        if self.root is None:
            return 0
        else:
            preorder(self.root)
            print(count)
        

exec(input())
