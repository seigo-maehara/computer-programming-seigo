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

    def __eq__(self, other):
        return self.real ** 2 + self.imagine ** 2 == other.real ** 2 + other.imagine ** 2

    def __gt__(self, other):
        return self.real ** 2 + self.imagine ** 2 > other.real ** 2 + other.imagine ** 2

    def __add__(self, other):
        r = self.real + other.real
        i = self.imagine + other.imagine
        if i > 0:
            return f"{r} + {i}i"
        elif i == 0:
            return f"{r}"
        else:
            return f"{r} - {abs(i)}i"
        
    def __mul__(self, other):
        r = self.real * other.real - self.imagine * other.imagine
        i = self.real * other.imagine + self.imagine * other.real
        if i > 0:
            return f"{r} + {i}i"
        elif i == 0:
            return f"{r}"
        else:
            return f"{r} - {abs(i)}i"

exec(input())
