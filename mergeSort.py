def merge(list1, list2, list3):
    i = j = 0

    while i + j < len(list3):
        if (j == len(list2) or (i < len(list1) and list1[i] < list2[j])):
            list3[i + j] = list1[i]

            i += 1
        
        else:
            list3[i + j] = list2[j]
            j += 1


def merge_sort(arr):
    n = len(arr)

    if n < 2:
        return
    
    mid = n // 2

    list1 = arr[0: mid]
    list2 = arr[mid: n]

    merge_sort(list1)
    merge_sort(list2)

    merge(list1, list2, arr)