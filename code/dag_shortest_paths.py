class Vertex():
    
    def __init__(self, name, status = "new", parent = None, pre = None, post = None) -> None:
        
        # Everything here except name and status is
        # unneeded, I just am too lazy
        # to change my CTRL-C and CTRL-Ved code.
        self.name = name
        self.parent = parent
        self.pre = pre
        self.post = post
        self.status = status
        
    def __repr__(self) -> str or int:
        return self.name
    


def topo_sort(vertices, adj_list):
    
    for i in range(len(vertices)):
        vertices[i].status = "new"
    
    S = [None] * len(vertices)
    clock = len(vertices) - 1
    
    for i in range(len(vertices)):
        
        if "new".__eq__(vertices[i].status):
            clock = topo_sort_dfs(i, vertices, adj_list, S, clock)
    
    return S

def topo_sort_dfs(pos, vertices, adj_list, struct, clock):

    vertex = vertices[pos]
    vertex.status = "active"
    
    for j in range(len(adj_list[pos])):
        
        w = adj_list[pos][j][0]
        
        if "active".__eq__(vertices[w].status):
            # I guess this qualifies as failing gracefully?!
            return -1
    
        elif "new".__eq__(vertices[w].status):
            clock = topo_sort_dfs(w, vertices, adj_list, struct, clock)
        
    
    vertex.status = "finished"
    struct[clock] = pos
    clock = clock - 1
    
    return clock

def dag_sssp(s, vertices, adj_list, paths):
    
    topo_order = topo_sort(vertices, adj_list)
    
    for i in range(len(vertices)):
        
        v = topo_order[i]
        
        if s == v:
            paths[v] = 0
        else:
            paths[v] = 1000000
        
            for i in range(len(adj_list)):
                for j in range(len(adj_list[i])):
                    
                    if adj_list[i][j][0] == v:
                        
                        u = i
                        weight = adj_list[i][j][1]
                        
                        if paths[v] > paths[u] + weight:
                            paths[v] = paths[u] + weight
                
        
    
    return


def main():
    
    vertices = [Vertex(0), Vertex(1), Vertex(2), 
                Vertex(3), Vertex(4), Vertex(5)]
    adj_list = [[[1, 7], [2, 12]], [[2, 2], [3, 9]], [[4, 10]], [[5, 1]], [[3, 4], [5, 5]], []]
    
    paths = [1000000] * len(vertices)
    
    source = 0
    
    dag_sssp(0, vertices, adj_list, paths)
    
    for i in range(len(vertices)):
        print("Shortest path length from", source, "to", i, "is", paths[i])
    
    return

if __name__ == '__main__':
    main()