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
            
class JDate(Date):
    def __init__(self,g,y,m,d):
        if g == "令和":
            self.year = y + 2018
        elif g == "平成":
            self.year = y + 1988
        elif g == "昭和":
            self.year = y + 1925
        elif g == "明治":
            self.year = y + 1867
        else:
            self.year = y
        self.month = m
        self.day = d
    
    def __str__(self):
        if (self.year > 2019) or (self.year == 1989 and self.month > 5 ) or (self.year == 1989 and self.month == 5 and self.day >= 1):
            gengo = "令和"
            jyear = self.year - 2018
        elif (self.year > 1989) or (self.year == 1989 and self.month > 1) or (self.year == 1989 and self.month == 1 and self.day >= 8):
            gengo = "平成"
            jyear = self.year - 1988
        elif (self.year > 1926) or (self.year == 1926 and self.month == 12 and self.day >= 25):
            gengo = "昭和"
            jyear = self.year - 1925
        elif (self.year > 1912) or (self.year == 1912 and self.month > 7) or (self.year == 1912 and self.month == 7 and self.day >= 30):
            gengo = "大正"
            jyear = self.year - 1911
        elif (self.year > 1868) or (self.year == 1868 and self.month > 1) or (self.year == 1868 and self.month == 1 and self.day >= 25):
            gengo = "明治"
            jyear = self.year - 1867
        else:
            gengo = "out-of-range"
            jyear = self.year
        s = "このインスタンスは元号"+str(gengo)+str(jyear)+"年"+str(self.month)+"月"+str(self.day)+"日です 。"
        return s 

exec(input())
