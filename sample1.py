def even_odd():
    try:
        n = input("type a number:")
        n = int(n)
        print(n * n)
    except (ZeroDivisionError,ValueError):
        print("poor")

def print_str():
    s = input("type a strings")
    print (s)

def ch3(a,b,c,d=1,e=1):
    n = a * b * c * d * e
    print(n)

def getHalf(a):
    n = a // 2
    print(n)
    return n

def getFour(b):
    n = b * 4
    print(n)

def chFloat():
    try:
        s = input("type string:")
        s = float(s)
        return s
    except(ValueError):
        print("poor")

print(chFloat())


