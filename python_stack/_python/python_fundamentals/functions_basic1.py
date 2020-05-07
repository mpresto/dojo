# NUMBER OF CORRECT PREDICTED OUTCOMES: 12/15


# 1 PREDICTED OUTPUT: 5
def a():
    return 5


print(a())


# 2 PREDICTED OUTPUT: 10
def a():
    return 5


print(a()+a())


# 3 PREDICTED OUTPUT: 5
def a():
    return 5
    return 10


print(a())


# 4 PREDICTED OUTPUT: 5
def a():
    return 5
    print(10)


print(a())


# 5 PREDICTED OUTPUT: 5
#   ACTUAL OUTPUT 5 None
def a():
    print(5)


x = a()
print(x)


# 6 PREDICTED OUTPUT: 3 5 8
#    ACTUAL OUTPUT: 3 5 (and a TypeError)

def a(b, c):
    print(b+c)


print(a(1, 2) + a(2, 3))


# 7 PREDICTED OUTPUT: 25
def a(b, c):
    return str(b)+str(c)


print(a(2, 5))


# 8 PREDICTED OUTPUT: 100 10 7
#    ACTUAL OUTPU: 100 10

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(a())


# 9 PREDICTED OUTPUT: 7 14 21
def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))


# 10 PREDICTED OUTPUT: 8
def a(b, c):
    return b+c
    return 10


print(a(3, 5))


# 11 PREDICTED OUTPUT: 500 500 300 500
b = 500
print(b)


def a():
    b = 300
    print(b)


print(b)
a()
print(b)


# 12 PREDICTED OUTPUT: 500 500 300 500
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b   # still within the scope of the function


print(b)
a()
print(b)


# 13 PREDICTED OUTPUT: 500 500 300 300
b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


print(b)
b = a()  # sets b to return value of a()
print(b)


# 14 PREDICTED OUTPUT: 1 3 2
def a():
    print(1)
    b()
    print(2)


def b():
    print(3)


a()


# 15 PREDICTED OUTPUT: 1 3 5 10
def a():
    print(1)
    x = b()
    print(x)
    return 10


def b():
    print(3)
    return 5


y = a()
print(y)
