f = open('mydata','r')
#print(f.read())
#print(f.readline(6),end = '')
#print(f.readline())


#f2 = open('data','w')
f2 = open('data','a')
#f2.write(" .she is a engineeer")
for i in f:
    f2.write(i)