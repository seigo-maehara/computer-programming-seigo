class Date:
    def __init__(self,y,m,d):
        self.year = y
        self.month = m
        self.day = d
    
    def is_new_year_day(self):
        return (self.month == 1) and (self.day == 1)
    
    def __str__(self):
        return "このインスタンスは"+str(self.year)+"年"+str(self.month)+"月"+str(self.day)+"日です。"
    
    def __gt__(self,other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                elif self.day <= other.day:
                    return False
    
    def __eq__(self,other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False

exec(input())
