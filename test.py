def plus(a,b):
    if b == a:
        return a
    return b + plus(a,b-1)


def muti(a,b):
    if b == 1:
        return a
    return a + muti(a,b-1)


def fib(x):
    if x == 1 or x == 2:
        return 1

    return fib(x-1) + fib(x-2)



def printhan(fr,to):
    print("{}-->{}".format(fr,to))


def hano(fr,to,space,n):
    if n == 1:
        printhan(fr,to)
    else:
        hano(fr,space,to,n-1)
        hano(fr,to,space,1)
        hano(space,to,fr,n-1)



hano('A','B','C',3)

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


#Towers(5,"A","B","C")




def wmuti(a,b):
    i = 0
    j = 0
    while  i != b:
        j += a
        i += 1
    return j

x = wmuti(5,6)



def cmp(x,y):
    if x>y:
        return -1
    else:
        return 1



# print(sorted([3,5,6,8],reverse=True))

