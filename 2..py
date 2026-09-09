def abeceda():
    for i in range(65,91):
        for j in range(65,91):
            for g in range(65,91):
                print(chr(i),chr(j),chr(g),sep='')

zoz=[]
def prepare(n:int): #rekurzia
    global zoz
    zoz=['-']*n
    print(zoz)

def doit(n:int):
    prepare(n)
    shredder(n)

def shredder(n:int):
    global zoz
    if n==-1:
        print(' '.join(zoz))
    else:
        for i in range(97,123):
            zoz[n-1]=chr(i)
            shredder(n-1)
doit(3)