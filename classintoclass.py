class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap =self.laptop()

    def show(self):
        print(self.name,self.age)
        self.laptop
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'dcl'
            self.ram = '4gb'
            self.cpu = 'i3'
        def show(self):
            print(self.brand,self.ram,self.cpu)


#to get from inner class you can write s1.lap.brand
#you can also write student.laptop()


s1 =student('suma',23)
s2 = student('ritu',22)
s1.show()
s2.show()