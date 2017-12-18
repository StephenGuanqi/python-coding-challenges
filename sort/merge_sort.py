def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    mid = n // 2
    L = merge_sort(array[:mid])
    R = merge_sort(array[mid:])
    return merge(L, R)


def merge(L, R):
    i = 0
    j = 0
    answer = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i < len(L):
        answer.extend(L[i:])
    if j < len(R):
        answer.extend(R[j:])
    return answer


def merge_sort2(array, l, r):
    if l == r:
        return
    mid = l + (r - l) // 2
    merge_sort2(array, l, mid)
    merge_sort2(array, mid + 1, r)
    merge2(array, l, mid, r)


def merge2(array, l, m, r):
    nl = m - l + 1
    nr = r - m
    L = [0] * nl
    R = [0] * nr
    for i in range(nl):
        L[i] = array[l + i]
    for i in range(nr):
        R[i] = array[m + 1 + i]

    i = 0
    j = 0
    k = l

    while i < nl and j < nr:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < nl:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        arr[k] = R[j]
        j += 1
        k += 1


arr = [12, 11, 13, 5, 6]
arr = merge_sort(arr) # or has no effect to original array
print("Sorted array is:")
print(arr)