def kosaraju_sharir(adj_list, roots, marks):
    
    process_stack = []
    
    for i in range(len(adj_list)):
        marks[i] = False
        roots[i] = None
        
    # Phase 1: Push in postorder in rev(G)
    for i in range(len(adj_list)):
        if marks[i] == False:
            push_post_rev_dfs(i, adj_list, marks, roots, process_stack)
    
    # Phase 2: DFS again in stack order
    while len(process_stack) != 0:
        vertex = process_stack.pop()
        if roots[vertex] == None:
            label_one_dfs(vertex, adj_list, roots, vertex)

    return

def push_post_rev_dfs(vertex, adj_list, marks, roots, container):
    
    marks[vertex] = True
    
    for i in range(len(adj_list)):
        # if chr(vertex+97) in adj_list[i] and marks[i] == False:
        #     push_post_rev_dfs(i, adj_list, marks, roots, container)
        
        try:
            u = adj_list[i][adj_list[i].index(chr(vertex + 97))]
            u = ord(u) - 97
            if marks[i] == False:
                push_post_rev_dfs(i, adj_list, marks, roots, container)
        
        except ValueError:
            pass
    
    container.append(vertex)
    
def label_one_dfs(vertex, adj_list, roots, r):
    
    roots[vertex] = r
    
    for i in range(len(adj_list[vertex])):
        w = ord(adj_list[vertex][i]) - 97
        if roots[w] == None:
            label_one_dfs(w, adj_list, roots, r)
        
    
     
        
        
    
    

def main():
    
    adj_list = [['b'], [ 'f' ], ['h'], ['c'], 
                [ 'f', 'i' ], ['g', 'l' ], ['a', 'k'], ['d', 'l'], 
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
    
        
        
    
    