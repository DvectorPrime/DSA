def insertion_sort(A):
    """Uses the insertion search algorithm to sort a list 'A' """
    """It runs in O(nsquared)in worse case and O(n) when the list is nearly sorted"""

    for i in range(1, len(A)):
        cur = A[i]

        j = i
        while j > 0 and cur < A[j - 1]:
            A[j] = A[j - 1]
            j -= 1

        A[j] = cur

lists = [1, 0, 9, 3, -2, 8, 3, 8, 4,2, 4, 0, 3]

insertion_sort(lists)
print(lists)