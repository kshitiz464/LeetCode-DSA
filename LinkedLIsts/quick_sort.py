def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        print(low, arr[low] )
        print(high, arr[high])
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    return


arr = []
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)
