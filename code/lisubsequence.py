# WIP


''' Returns the length of the largest increasing subsequence '''
def largest_increasing_subsequence(prev, arr, lo, hi):
    if hi - lo < 0:
        return 0
    elif(arr[lo] <= prev):
        return largest_increasing_subsequence(prev, arr, lo+1, hi)
    else:
        skip = largest_increasing_subsequence(prev, arr, lo+1, hi)
        take = largest_increasing_subsequence(arr[lo], arr, lo+1, hi) + 1
        return max(skip, take)
    
''' Returns the actual largest increasing subsequence '''
def largest_increasing_ss_set(prev, arr, lo, hi):
    if hi - lo < 0:
        return ''
    elif(arr[lo] <= prev):
        return largest_increasing_ss_set(prev, arr, lo+1, hi)
    else:
        skip = largest_increasing_ss_set(prev, arr, lo+1, hi)
        take = str(arr[lo]) + " " + largest_increasing_ss_set(arr[lo], arr, lo+1, hi) 
        if len(str.split(skip)) >  len(str.split(take)): return skip 
        else: return take

def main():
    
    myArr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
    result = largest_increasing_subsequence(-10000, myArr, 0, len(myArr)-1)
    print(result)
    result = largest_increasing_ss_set(-10000, myArr, 0, len(myArr)-1)
    print(result)
    
    
if __name__ == '__main__':
    main()