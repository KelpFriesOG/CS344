

def edit_distance(origin: str, dest: str):
    
    # Matrix to store results of subproblems
    edit_matrix = [[0 for x in range(len(dest)+1)] for x in range(len(origin)+1)]
    
    # Filling in the matrix in a bottom up manner
    for i in range(len(origin)+1):
        for j in range(len(dest)+1):
            
            # INSERTION
            # If origin string is empty.
            # put in all characters of second string
            if i == 0:
                edit_matrix[i][j] = j
            
            # REMOVAL
            # If dest string is empty...
            # remove all characters of the second string.
            elif j == 0:
                edit_matrix[i][j] = i
                
            # IF SAME
            # If the characters between the original and
            # destination string are the same, then
            # skip the current iteration and put
            # in the same edit distance for the current
            # pair of comparisons as the last pair.
            elif origin[i-1] == dest[j-1]:
                edit_matrix[i][j] = edit_matrix[i-1][j-1]
                
            # IF DIFFERENT
            # If the characters between the original and
            # destination string are different, then
            # consider all options, and choose
            # the option that increases the edit distance
            # by the most minimal amount.
            else:
                edit_matrix[i][j] = 1 + min(edit_matrix[i][j-1], edit_matrix[i-1][j], edit_matrix[i-1][j-1])
                
    # After all iterations, the final, and least amount
    # of edit distance between the two strings will be
    # in the lower corner of the 2D array 
    # (the last indexed row and column) 
    return edit_matrix[len(origin)][len(dest)]
        
          
def main():
    origin_word = "ALGORITHM"
    dest_word = "ALTRUISTIC"
    print('The minimum edit distance between '+ origin_word +
          ' and ' + dest_word + ' is ' + str(edit_distance(origin_word, dest_word)))

            
if __name__ == '__main__':
    main()