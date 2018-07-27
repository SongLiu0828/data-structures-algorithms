from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    found = True
    index = 0
    while index < len(symbolString) and found:
        symbol = symbolString[index]
        if symbol == "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                found = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    found = False

        index += 1

    if found and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
