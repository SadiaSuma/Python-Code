class topten:
    def __init__(self):
        self.nums = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.nums <= 10:
            val = self.nums
            self.nums+=1
            return val
        else:
            raise StopIteration
suma = topten()
for i in suma:
    print(i)

















'''
nums = [2,3,4,5,6,7,8]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
'''