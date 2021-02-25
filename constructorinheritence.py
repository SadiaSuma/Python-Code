class A:
    def __init__(self):
        print("in a init")
    def feature1(self):
        print("f1")
    def feature2(self):
        print("f2")

class B():   
    def __init__(self):
        super().__init__()
        print("in b init")          
    def feature3(self):
        print('f3')
    def feature4(self):
        print("f4")

class C(A,B):
    def __init__(self):
        super().__init__()            #it will call left to right so it will cl first A
        print("in c init")
    def feat(self):
        super().feature4()

a = C()
a.feat()