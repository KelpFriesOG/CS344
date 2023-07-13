lis_bigger = [[None] * 24] * 23

def fast_LIS(arr, lo, hi):
    arr[0] = -10000000000
    for i in range(0, hi):
        lis_bigger[i][hi+1] = 0
    for j in range(hi, 0, -1):
        for i in range(0, j):
            keep = 1 + lis_bigger[j][j+1]
            skip = lis_bigger[i][j+1]
            if arr[i] >= arr[j]:
                lis_bigger[i][j] = skip
            else:
                lis_bigger[i][j] = max(skip, keep)
    return lis_bigger[0][1]
                
    

def main():
    
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
    
    print(fast_LIS(arr, 0, len(arr)-1))
    
    print(lis_bigger)
    
    
if __name__ == '__main__':
    main()