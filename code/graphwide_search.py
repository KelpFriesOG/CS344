def traverse_graph(adj_list, marks):
    
    for i in range(len(marks)):
        marks[i] = False
    
    count = 1
    for i in range(len(adj_list)):
        if marks[i] == False:
            print("\nTraversing component ", count, "...")
            iter_dfs(i, adj_list, marks)
            count+=1
    

def iter_dfs(s, adj_list, marks):
    
    stack = []
    stack.append(s)
    
    while len(stack) != 0:
        
        v = stack.pop()
        if marks[v] == False:
            print("Processing vertex ", v, "...")
            
            marks[v] = True
            for i in range(len(adj_list[v])):
                stack.append(adj_list[v][i])



def main():
    
    adj_list = [[1, 2], [0, 2], [0, 1], [4], [3]]
    marks = [False, False, False, False, False]
    
    traverse_graph(adj_list, marks)
    
    print("\n", marks)
    
    ''' The goal of the traverse_graph method is to mark all components
        of a disconnected graph. This is done by deploy a search on every
        component one at a time. Deploying a search on one component marks
        all the vertices in it (because by definition a component is connected).
        
        After the set of vertices in the first component we look for the next
        unmarked vertex and then deploy the search on it and so forth.
        
        '''
    
    return    
    
    
if __name__ == '__main__':
    main()