from pythonds.basic.stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    s = Stack()

    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not s.isEmpty():
        newString = newString + digits[s.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))
