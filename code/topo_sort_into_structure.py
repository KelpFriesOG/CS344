
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
        
        w = adj_list[pos][j]
        
        if "active".__eq__(vertices[w].status):
            # I guess this qualifies as failing gracefully?!
            return -1
    
        elif "new".__eq__(vertices[w].status):
            clock = topo_sort_dfs(w, vertices, adj_list, struct, clock)
        
    
    vertex.status = "finished"
    struct[clock] = pos
    clock = clock - 1
    
    return clock
    
    

def main():
    
    # This is the dag from the chapter 6 notes.
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [], [3, 4]]
    marks = [False, False, False, False, False, False]
    
    print(topo_sort(vertices, adj_list))
    
    return


if __name__ == '__main__':
    main()