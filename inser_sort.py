def insert_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i
        while j >0 and alist[j-1] > alist[j]:
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print(alist)
