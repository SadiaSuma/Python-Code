class A:
    def feature1(self):
        print("f1")
    def feature2(self):
        print("f2")

class B(A):             #multilevelinheriting
    def feature3(self):
        print('f3')
    def feature4(self):
        print("f4")
class C(A,B):                         #MULTIPLEINHERITING
    def feature5(self):
        print("f5")

a = A()
a.feature1()
a.feature2()
b = B()
b.feature3()
b.feature4()