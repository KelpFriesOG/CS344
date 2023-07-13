def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def quickselect(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)
        
        if k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        elif k > pivot_index:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return arr[pivot_index]
    
    return arr[low]  # or return arr[high] (both are equivalent for a single-element range)

# Example usage:
arr = [25, 24, 33, 39, 3, 18, 19, 31, 23, 49, 45, 16, 1, 29, 40, 22, 15, 20, 24, 4, 13, 34]
k = 16
result = quickselect(arr, 0, len(arr) - 1, k - 1)
print(f"The {k}-th smallest element is {result}")
