def shell_sort(alist):
    """最优时间复杂度：根据步长序列的不同而不同
    最坏时间复杂度：O(n^2)
    稳定性：不稳定"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i-gap) >= 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
