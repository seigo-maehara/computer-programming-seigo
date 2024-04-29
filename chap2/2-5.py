class Line:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
    
    def next(self, s):
        return print(str(self.arr1[self.arr1.index(s) + 1]))
    
    def prev(self, s):
        return print(str(self.arr1[self.arr1.index(s) - 1]))
    
    def next_exp(self, s):
        return print(str(self.arr2[self.arr2.index(s) + 1]))
    
    def prev_exp(self, s):
        return print(str(self.arr2[self.arr2.index(s) - 1]))


class Line2(Line):
    def next(self, s):
        if s not in self.arr1:
            return "no such station exists."
        elif s == self.arr1(-1):
            return "input is a terminal station."
        else:
            super().next(s)
    
    def prev(self, s):
        if s not in self.arr1:
            return "no such station exists."
        elif s == self.arr1(0):
            return "input is a terminal station."
        else:
            super().prev(s)

    def next_exp(self, s):
        if s not in self.arr1:
            return "no such station exists."
        else:
            if s not in self.arr2:
                return "express does not stop at this station."
            elif s == self.arr2(-1):
                return "input is a terminal station."
            else:
                super(). next_exp(s)

    def prev_exp(self, s):
        if s not in self.arr1:
            return "no such station exists."
        else:
            if s not in self.arr2:
                return "express does not stop at this station."
            elif s == self.arr2(0):
                return "input is a terminal station."
            else:
                super().prev_exp(s)


exec(input())
