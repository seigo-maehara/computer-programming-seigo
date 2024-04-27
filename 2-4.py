class Line:
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2
    
    def next(self,s):
        return print(str(self.arr1[self.arr1.index(s) + 1]))
    
    def prev(self,s):
        return print(str(self.arr1[self.arr1.index(s) - 1]))
    
    def next_exp(self,s):
        return print(str(self.arr2[self.arr2.index(s) + 1]))
    
    def prev_exp(self,s):
        return print(str(self.arr2[self.arr2.index(s) - 1]))

exec(input())
