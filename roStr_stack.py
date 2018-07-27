from pythonds.basic.stack import Stack

s = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            s.push(convertString[n])
        else:
            s.push(convertString[n%base])
        n  = n // base
    res = ""
    while not s.isEmpty():
        res = res + str(s.pop())
    return res

print(toStr(1453, 16))
