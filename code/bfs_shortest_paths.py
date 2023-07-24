'''
    The BFS approach to the SSSP (single source shortest path) problem
    works for unweighted graphs. In this scenario each edge has a weight
    of one, so the shortest path is simply the minimum # of edges between
    two nodes. Although this problem is trivial, especially for smaller
    graphs. The algorithm we use is nonetheless an important application
    of BFS and iterates on the generic approach of Ford's algorithm.

'''



def bfs(s, adj_list, paths, preds):
    
    queue = []
    
    init_sssp(s, paths, preds)
    
    queue.append(s)
    
    while len(queue) != 0:
        
        u = queue.pop(0)
        
        for i in range(len(adj_list[u])):
            v = adj_list[u][i]
            if paths[v] > paths[u] + 1:
                paths[v] = paths[u] + 1
                preds[v] = u
                queue.append(v)
            
            
    
    return
    
    
def init_sssp(s, paths, preds):
    
    paths[s] = 0
    preds[s] = None
    
    for i in range(len(paths)):
        if i != s:
            paths[i] = 100000
            preds[i] = None

    return


def main():
    
    adj_list = [[4, 8], [0, 2], [5, 6, 8], [2, 6], [1, 7], 
                [1, 4], [5], [5, 6], [1, 3]]
    
    paths = [1000000] * len(adj_list)
    preds = [None] * len(adj_list)
    
    source = 8
    
    bfs(source, adj_list, paths, preds)
    
    for i in range(len(adj_list)):
        print("The least # of edges from", source, "to", i, "is", paths[i])
    
    return

if __name__ == '__main__':
    main()