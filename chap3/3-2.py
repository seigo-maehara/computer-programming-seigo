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

exec(input())
