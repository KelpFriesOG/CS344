
def fast_subset_sum(arr, T: int):

    # Setting up the memoization structure to have T+1 columns
    # and n+1 rows (overall space complexity = O(n*T)) where
    # n is the length of the array and T is the sum.
    ss = [[False for i in range(T + 1)] for j in range(len(arr)+1)]
    
    # For all values of the first column, set the value in
    # the structure to true. In other words, if the sum
    # is 0 (remember that the ith column represents a sum)
    # then the empty subset, which is a subset of all subsets
    # satisfies the problem.
    for i in range(len(arr)+1):
        ss[i][0] = True
    
    
    # For all values in the first row (except 
    # the first column), set the value in
    # in the structure to false. In other words, if the
    # sum is non-zero (the first column was skipped to
    # account for this), and the array (set) is as
    # a whole sums to 0, then it is impossible to
    # get the target element (always False).
    for i in range(1, T+1):
        ss[0][i] = False
    
    # After setting up the base cases we traverse
    # from row 1 through the last
    for i in range(1, len(arr)+1):
        # We also traverse through each column
        # from the column 1 through the last.
        for j in range(1, T+1):
            
            # If the column value (which represents the sum)
            # is less than the i-1th value of the set,
            # This means that if we were to decrement the
            # running sum by the i-1th value the result would
            # be negative. We cannot have that!
            # Therefore we simply copy over the truth value
            # based on the i-1th row of the subset structure
            # to show that no change occured.
            if j < arr[i-1]:
                ss[i][j] = ss[i-1][j]
                
            # Now the interesting part!
            # If the column value, j, which is the running
            # sum is greater than or equal to the i-1th
            # value of the original array,
            # then we can safely choose to subtract as follows
            # j - arr[i-1] without risking the result being
            # negative.
            # If the previous running sum (ss[i-1][j]) was
            # already True, then we are simply copying
            # over that value into ss[i][j]
            # Otherwise if the previous running sum (ss[i-1][j])
            # was False, then we consider that perhaps
            # the subtraction will point us to a cell with
            # a truth value of True (a subtraction that led
            # to the sum being 0).
            if j >= arr[i-1]:
                ss[i][j] = ss[i-1][j] or ss[i-1][j-arr[i-1]] 
    
    # After processing the entire array,
    # the final result, of whether or not
    # the sum could be reached via any
    # combination will be in the bottom
    # right corner of this 2D array.
    return ss[len(arr)][T]


def main():
    
    # Try out different sets and sums!
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    print(fast_subset_sum(set, sum))
    

if __name__ == '__main__':
    main()