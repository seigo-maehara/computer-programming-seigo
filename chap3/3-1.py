class Node:
    def __init__(self, x):
        self.value = x
    
    def __str__(self):
        if self.value is None:
            return ""
        else:
            return self.value


exec(input())
