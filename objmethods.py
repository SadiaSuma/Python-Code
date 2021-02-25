class students:
    school = "telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    

    def get_m1(self):
        return self.m1            #accessors

    def set_m1(self,vl):          #mutators
        self.m1 = vl 
    @classmethod                 #decorators
    def getschool(cls):
        return students.school
    @staticmethod
    def info():
        print("i am a student of class 8")

s1 = students(23,33,98)
s2 = students(44,55,77)
print(students.getschool())
students.info()

print(s1.avg())
