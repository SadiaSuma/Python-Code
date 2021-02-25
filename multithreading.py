from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(Self):
        for i in range(5):
            print("hi")
            sleep(1)
obj1 = hello()
obj2 = hi()
obj1.start()
sleep(0.2)
obj2.start()
obj1.join()
obj2.join()
print("bye")