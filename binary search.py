dataset = [2,4,5,7,8,12,14,17,19,22,25,27,28,33,37,39,42,48,53,59]

def binary_search(data, target, low=0, high=0):
    """Uses the binary search algorithm to find a particular 'target'"""
    if high == 0:
        high = len(data) - 1

    mid = (low + high) // 2

    if low > high:
        return False
    elif target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else: 
        return binary_search(data, target, mid + 1, high)
    
print(binary_search(dataset, 49))

def reverse_list(sequence, start, stop):
    if start < stop - 1:
        sequence[start], sequence[stop - 1] = sequence[stop - 1], sequence[start]
        reverse_list(sequence, start + 1, stop -1)

reverse_list(dataset, 0, len(dataset))

print(dataset)

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        print(partial)
        result = partial * partial

        if n % 2 == 1:
            result *= x

        return result
    
print(power(2, 7))