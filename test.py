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



print(sorted([3,5,6,8],reverse=True))

