class Vertex():
    
    def __init__(self, name, status = "new") -> None:
        self.name = name
        self.status = status
        
    def __repr__(self) -> str:
        return self.name

def some_process(v):
    print(v)

def post_process(vertices, adj_list):

    for i in range(len(vertices)):
        vertices[i].status = "new"
    
    for i in range(len(vertices)):
        if "new".__eq__(vertices[i].status):
            post_process_dfs(i, vertices, adj_list)

def post_process_dfs(pos, vertices, adj_list):
    
    vertex = vertices[pos]
    vertex.status = "active"
    
    for j in range(len(adj_list[pos])):
        w = adj_list[pos][j]
        
        if "new".__eq__(vertices[w].status):
            post_process_dfs(w, vertices, adj_list)
        elif "active".__eq__(vertices[w].status):
            return
    
    vertex.status = "finished"
    some_process(vertex)

def reverse_graph(adj_list):
    
    new_list = [[] for j in range(len(adj_list))]
    
    # While its tempting to say that the complexity here
    # is O(V * E), lets look closer...
    
    for i in range(len(adj_list)):
        # For every vertex
        source_vertex = i
        for j in range(len(adj_list[i])):
            # For every edge of that vertex
            dest_vertex = adj_list[i][j]
            new_list[dest_vertex].append(source_vertex)
    
    # Remember that E, the number of edges, on
    # a directed graph is bounded upto V*(V-1)
    # Therefore we could say that the complexity
    # here is simply O(V^2 + V) (i am simply replacing E).
    # Then it becomes evident that in terms of V\
    # The complexity is O(V^2)
    
    # But if we take a slightly more abstract angle
    # O(V + E) provides us with more info on where
    # the V^2 came from in terms of graph theory.
    
    # Saying the complexity is O(V * E) would translate
    # to O(V^3) which is simply wrong, so lets not do that lol.
    
    return new_list

def main():
    
    # This is the dag from the chapter 6 notes.
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [], [3, 4]]
    
    print("", "The nodes below should be printed",
          "in reverse topological order.",
          "Which is the same as postorder!", "", sep='\n')
    
    post_process(vertices, adj_list)
    
    reversed_adj_list = reverse_graph(adj_list)
    
    print("", "The nodes below should be printed",
          "in some valid topological order.",
          "This ordering is not necessarily the same as",
          "the reverse postorder of the",
          "original graph", "", sep='\n')
    
    post_process(vertices, reversed_adj_list)

    
if __name__ == '__main__':
    main()