def shunxu_search(alist, item):
    i = 0
    found = False
    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
        else:
            i += 1
    return found


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(shunxu_search(alist, 54))
print(shunxu_search(alist, 19))
