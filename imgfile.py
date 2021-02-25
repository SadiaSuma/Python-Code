f = open('suma.jpg.jpg','rb')
f1 = open('mypic.jpg','wb')
for j in f:
    print(j)
for i in f:
    f1.write(i)