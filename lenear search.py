
pos =-1
def search(list,n):
    i = 0
    while i<len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list =[1,2,33,44,55,66,77]
n = 44
if search(list,n):
    print('found at', pos+1)
else:
    print("not found")