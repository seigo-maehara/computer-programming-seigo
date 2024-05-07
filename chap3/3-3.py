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


def preorder(n):
    if n == None:
        return
    else:
        print(n.value, end=" ")
        preorder(n.left)
        preorder(n.right)


def postorder(n):
    if n == None:
        return
    else:
        postorder(n.left)
        postorder(n.right)
        print(n.value, end=" ")


def inorder(n):
    if n == None:
        return
    else:
        inorder(n.left)
        print(n.value, end=" ")
        inorder(n.right)


exec(input())