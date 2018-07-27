def quick_sort(alist):
    if len(alist) <= 1:
        return alist

    left_less = []
    right_less = []
    base = alist.pop()

    for i in alist:
        if i <base:
            left_less.append(i)
        else:
            right_less.append(i)

    return quick_sort(left_less) + [base] + quick_sort(right_less)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quick_sort(alist))
