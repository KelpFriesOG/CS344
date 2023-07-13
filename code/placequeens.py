def place_queens(board, row):
    
    # Base Case: if we have processed the whole board
    if(row >= len(board)):
        print(board)
    # Recursive Case: Process for the row.
    else:
        # j represents all the possible values of the queen's position
        # The range of j therefore is from 0 to len(board) - 1
        # Here, we go through each possible positions
        # for the Queen.
        for j in range(0, len(board)):
            # We first assume the position is valid
            valid = True
            
            # i or rather the position i in the board array
            # represents all the positions of the previous
            # queens
            # Here we compare the previous filled slots
            # of the array and see if they conflict
            # with our placeholder location for the queen.
            for i in range(0, row):
                # If the queen in row i has the same
                # column as the placeholder position 
                # (board[i] == j)
                # OR
                # If the queen in row i has a left diagonal
                # position in comparison to the placeholder
                # position.
                # board[i] == j - row + i
                # OR
                # If the queen in row i has a right diagonal
                # position in comparison to the placeholder
                # position.
                # board[i] == j + row - i
                # If any of these statements are
                # true, then valid => false
                # Then we must exit this call as a
                # point of failure (we don't commit
                # our value at the position, which is j).
                
                if (board[i] == j or
                    board[i] == j - row + i or
                    board[i] == j + row - i):
                    valid = False
            
            # If valid == True at this point,
            # then the queen is placed at this point and
            # place_queens is called recursively
            # to deal with the queen for the nect row.
            if valid:
                board[row] = j
                place_queens(board, row+1)
    
def main():
    
    
    board = [None, None, None, None, None, None, None, None]
    print("Valid queen positions of a 6x6 board with 4 queens:")
    place_queens(board, 0)
    
    
    
    
    
if __name__ == '__main__':
    
    main()
    
            