class student:
    def __init__(self,m1,m2):
        self.m1 =m1 
        self.m2 = m2
    def sum(Self,a= None,b = None, c = None):
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a!= None and b!=None:
            s = a+b
        else:
            s = a
        return s

s1 = student(30,60)
print(s1.sum(4,9,99))