def merge_sort(alist):
    print("Splitting ",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalg = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalg)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalg):
            if lefthalf[i] < righthalg[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalg[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalg):
            alist[k] = righthalg[j]
            j += 1
            k += 1
    print("Merging ",alist)
    
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
