

def iter_dfs(s, adj_list, marks):
    
    # Reset the marks array
    for i in range(len(marks)):
        marks[i] = False
    
    # Create a stack and append the first element
    # I know the book says push, but python supports
    # stacks by being able to call stack operations
    # on a traditional list. When we append, we add
    # to the end of the list. What matters for a stack is that
    # we insert (append) and remove (pop) from the same end of the structure.
    stack = []
    stack.append(s)
    
    # The stack will only be emptied after
    # each reachable node from s is marked.
    while len(stack) != 0:
        
        # We remove and get the vertex at the top of the stack 
        # (the most recently appended element, which is at the end of the list)
        v = stack.pop()
        
        # If the popped element has not been marked, then...
        if marks[v] == False:
            
            # We mark it.
            marks[v] = True
            
            # I added in this line so the user can
            # see the order in which each unmarked
            # vertex is processed. This line should
            # help illustrate the difference
            # between dfs and bfs!
            print("Processing vertex "+str(v)+"...")
            
            # And then for each of its neighbors
            # (each element in the adj list of the vertex)
            for i in range(len(adj_list[v])):
                
                # We push the neighbors into the stack to be processed next!
                stack.append(adj_list[v][i])


def iter_bfs(s, adj_list, marks):
    
    # Reset the marks array
    for i in range(len(marks)):
        marks[i] = False
    
    
    # Create a queue and insert the first element at the end.
    # Note that while you could make an explicit Queue class
    # yourself or use one from a library, I am using a list
    # to simulate a queue. What matters for a queue is that
    # elements are added and removed from opposing ends of the list.
    queue = []
    queue.append(s)
    
    # The queue will only be emptied after 
    # each reachable node from s is marked.
    while len(queue) != 0:
        
        # Typically the pop operation removes from the
        # same end that the element was inserted into,
        # but here the 0 tells Python to "pop" from
        # the front of the structure. This is
        # for all practical purposes identical to a dequeue operation!
        v = queue.pop(0)
        
        # If the dequeued element has not been marked...
        if marks[v] == False:
            
            # We mark it.
            marks[v] = True
            
            # I added in this line so the user can
            # see the order in which each unmarked
            # vertex is processed. This line should
            # help illustrate the difference
            # between dfs and bfs!
            print("Processing vertex "+str(v)+"...")
            
            # And then for each of its neighbors
            # (each element in the adj list of the vertex)
            for i in range(len(adj_list[v])):
                
                # We enqueue the neighbors into the queue to be processed next!
                queue.append(adj_list[v][i])
            


def main():

    # Feel free to draw up your own graph and
    # put in it's details here!
    adj_list = [[1, 2], [0, 2], [0, 1], [4], [3]]
    marks = [False, False, False, False, False]
    
    print("\nStarting DFS...\n")
    
    iter_dfs(2, adj_list, marks)
    
    print(marks)
    
    print("\nStarting BFS...\n")
    
    iter_bfs(2, adj_list, marks)
    
    print(marks)

    ''' Both methods ultimately mark the same component in its entirety,
        but the order in which the vertices are accessed is different 
        depending on the search algorithm used. 
        
        Both algorithms go through at most all the vertices V once, and
        at most all the edges E once.
        
        Therefore the (worst-case) time complexity for both traversals is:
        
        O(V + E)
        
        '''

if __name__ == '__main__':
    main()