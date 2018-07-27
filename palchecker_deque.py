from pythonds.basic.deque import Deque

def palchecker(aString):
    s = Deque()

    for ch in aString:
        s.addRear(ch)#添加到尾部

    found = True

    while s.size() > 1 and found:
        first = s.removeFront()#移除首项
        last = s.removeRear()#移除尾部
        if first != last:
            found = False
    return found

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
