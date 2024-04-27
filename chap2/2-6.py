class Comp:
    def __init__(self, a, b):
        self.real = a
        self.imagine = b
    
    def __str__(self):
        if self.imagine == 0:
            return str(self.real)
        elif self.imagine < 0:
            return f"{self.real} - {abs(self.imagine)}i"
        else:
            return f"{self.real} + {self.imagine}i"


exec(input())

