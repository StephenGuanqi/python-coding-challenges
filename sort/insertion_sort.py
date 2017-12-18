def insertion_sort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


def insertion_sort_rec(A, n):
    """
    sor the first n elements of array A
    :param A:
    :return:
    """
    if n == 1:
        return

    insertion_sort_rec(A, n - 1)

    key = A[n - 1];
    j = n - 2;
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertion_sort_rec(arr, len(arr))
print("Sorted array is:")
print(arr)
