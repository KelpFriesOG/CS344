def partition(arr, lo, hi, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i

def find_median_brute_force(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid]

def MoM_select(arr, lo, hi, k):
    
    # If we hit either base case, the complexity
    # of the remaining work becomes constant
    if lo == hi:
        return arr[lo]
    if hi - lo < 5:
        subarray = arr[lo:hi+1]
        return find_median_brute_force(subarray)
    
    # Initializing an array to hold medians of each block
    num_blocks = (hi - lo + 1) // 5
    medians = []
    
    # To get the median of each block
    # We just use a simple brute force
    # approach. The complexity for
    # finding the median of each block
    # is constant O(1)
    for i in range(num_blocks):
        median_lo = lo + i * 5
        median_hi = median_lo + 4
        median = find_median_brute_force(arr[median_lo:median_hi+1])
        medians.append(median)
    
    # RECURSION: We then call the MoM method
    # to get the median of the medians.
    # The call processes n / 5 elements (that is the number of medians)
    # where n is the elements in the given list.
    # Complexity: T(n/5)
    pivot_index = MoM_select(medians, 0, len(medians) - 1, len(medians) // 2)
    
    
    # We get the actual pivot index by simply
    # accessing the index of the element that was returned.
    # Complexity: O(n)
    pivot_index = arr.index(pivot_index, lo, hi+1)
    
    # We then partition elements based on the pivot index,
    # The partition method returns the new position of the
    # same element that we used.
    # Complexity: O(n)
    pivot_index = partition(arr, lo, hi, pivot_index)
    
    # BASE CASE
    # If the position of the element after partitioning
    # is the kth position, then we return k
    if k == pivot_index:
        return k
    
    # RECURSIVE CASE
    # If k is less than the position of the pivot after
    # partitioning, then we recursively call MoM_select
    # on the left subarray, which is at most 7 / 10ths
    # the size of the original array.
    # Complexity: T(7n/10)
    elif k < pivot_index:
        return MoM_select(arr, lo, pivot_index - 1, k)
    
    # RECURSIVE CASE
    # If k is greater than the position of the pivot after
    # partitioning, then we recursively call MoM_select
    # on the right subarray, which is at most 7 / 10ths
    # the size of the original array.
    # Complexity: T(7n/10)
    else:
        return MoM_select(arr, pivot_index + 1, hi, k)

    # Overall complexity of MoM_select = O(n)
    # Based on the recurrence relation: T(n) <= T(7n/10) + T(n/5) + O(n)
    # T(n) <= T(9n/10) + O(n)
    
    # How to analyze?
    
    ''' Method 1: 
    
    '''

# Example usage
arr = [12, 8, 23, 4, 16, 11, 15, 10, 6, 9, 5, 7, 20, 14, 18, 21, 13, 17, 19, 22]
k = 1
kth_smallest = MoM_select(arr, 0, len(arr) - 1, k)
print(f"The {k+1}th smallest element is:", kth_smallest)
