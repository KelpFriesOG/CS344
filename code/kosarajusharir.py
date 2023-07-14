def kosaraju_sharir(adj_list, roots, marks):
    
    # Initializing the process stack
    process_stack = []
    
    # Resetting the roots and marks for each vertex
    for i in range(len(adj_list)):
        marks[i] = False
        roots[i] = None
        
    # Phase 1: Push in postorder in rev(G)
    for i in range(len(adj_list)):
        # for every vertex, if the vertex is unmarked...
        if marks[i] == False:
            # Call push_post_rev_dfs on the vertex (use the position
            # of the vertex in the adj_list: i)
            push_post_rev_dfs(i, adj_list, marks, roots, process_stack)
    
    # Phase 2: DFS again in stack order
    while len(process_stack) != 0:
        
        # Now this time we process from the top of the stack
        # to the bottom of the stack, which is to say we
        # process in reverse postorder.
        vertex = process_stack.pop()
        
        # The popped vertex is the root of one strongly
        # connected component. So we send it to be marked,
        # in the process it and all of its descendants,
        # will be given a root!
        if roots[vertex] == None:
            label_one_dfs(vertex, adj_list, roots, vertex)

    return

def push_post_rev_dfs(vertex, adj_list, marks, roots, container):
    
    # Since we are processing the vertex,
    # mark it.
    marks[vertex] = True
    
    # For each other vertex, w
    for i in range(len(adj_list)):
        
        # Check if there is an edge from w to vertex
        try:
            
            # THIS ENTIRE ALGORITHM WORKS UNDER THE ASSUMPTION
            # THAT THE ADJACENCY LIST CONTAINS VERTICES
            # LABELED AS LOWER CASE LETTERS.
            
            # We first shift our vertex by adding 97 and then
            # treat the result as an ASCII code and use chr()
            # to convert the int code into a char.
            # Ex. 0 -> 97 -> 'a', 1 -> 98 -> 'b', e.t.c
            
            # We then search for the character in adj_list[i] 
            # via the index() method. If the index method
            # does not find the vertex, we catch the ValueError
            # it spits out and continue to the next
            # loop iteration to check adj_list[i+1]
            u = adj_list[i][adj_list[i].index(chr(vertex + 97))]
            
            # If u was given a value, then it means we found
            # chr(vertex + 97) in adj_list[i]. This line
            # is functionally meaningless but it shows that
            # the value we found, when converted to its ascii code
            # and shifted down is the same as vertex.
            # Mathematically we are ascertaining ord(u) - 97 == vertex
            u = ord(u) - 97
            
            # For this existent edge w -> vertex, if w is unmarked,
            # then we continue by recursively performing a dfs
            # on w (the parent of vertex). This is why this method
            # is a "rev_dfs".
            if marks[i] == False:
                push_post_rev_dfs(i, adj_list, marks, roots, container)
        
        # This is similar to a try-catch block from Java, if we
        # we ran into some value error we simply continue,
        # because for us the error indicates that adj_list[i]
        # simply has no outgoing edge to vertex, this is a non-issue.
        except ValueError:
            pass
    
    # After processing each node, w, that was the parent of vertex
    # We push the vertex onto the stack.
    # At the end of the day, the values in this stack should be
    # filled in postorder. This means popping from the stack
    # would result in values being processed in reverse postorder!
    container.append(vertex)
    
def label_one_dfs(vertex, adj_list, roots, r):
    
    # The passed vertex is given the root r.
    roots[vertex] = r
    
    # For every outgoing edges from v, v -> w
    for i in range(len(adj_list[vertex])):
        
        # We first get the index that corresponds
        # with the letter at adj_list[vertex][i].
        # THIS ENTIRE ALGORITHM WORKS UNDER THE ASSUMPTION
        # THAT THE ADJACENCY LIST CONTAINS VERTICES
        # LABELED AS LOWER CASE LETTERS.
        w = ord(adj_list[vertex][i]) - 97
        
        # If the root of the w is None, it has
        # yet to be processed and can be considered
        # as being part of the component which has
        # the root r (which maybe v or one of v's ancestors).
        if roots[w] == None:
            
            # We make a recursive call to label w, and
            # any of w's descendants as having the same
            # root that vertex has.
            label_one_dfs(w, adj_list, roots, r)
        
    
     
        
        
    
    

def main():
    
    adj_list = [['b'], [ 'f' ], ['h'], ['c'], 
                [ 'f', 'i' ], ['g', 'l' ], ['a', 'c', 'k'], ['d', 'l'], 
                [ 'n' ], [ 'k', 'm' ], [ 'h', 'l' ], ['o', 'p'], 
                [ 'i' ], [ 'j', 'o' ], [ 'k' ], []]
    
    roots = [None] * 16
    marks = [False] * 16
    
    kosaraju_sharir(adj_list, roots, marks)
    
    print("\n", roots, "\n")
    
    print("The number of unique roots is the number of components")
    
    print("In this case there are", len(set(roots)), "components!\n")
    
    components = set(roots)
    i = 0
    
    for e in components:
        print("Component", i+1, "'s startpoint of traversal:", e)
        i+=1
    
    return




if __name__ == '__main__':
    main()
    
        
        
    
    