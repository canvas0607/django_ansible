def plus(x):
    if x == 1 or x == 0:
        return 1
    return plus(x-1)

a = plus(5)

print(a)