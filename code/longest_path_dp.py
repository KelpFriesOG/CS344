class Vertex():
    
    def __init__(self, name, status = "new") -> None:
        self.name = name
        self.status = status
        
    def __repr__(self) -> str:
        return self.name



def post_process(vertices, adj_list):

    postordering = []

    for i in range(len(vertices)):
        vertices[i].status = "new"
    
    for i in range(len(vertices)):
        if "new".__eq__(vertices[i].status):
            post_process_dfs(i, vertices, adj_list, postordering)

    return postordering

def post_process_dfs(pos, vertices, adj_list, container):
    
    vertex = vertices[pos]
    vertex.status = "active"
    
    for j in range(len(adj_list[pos])):
        w = adj_list[pos][j][0]
        
        if "new".__eq__(vertices[w].status):
            post_process_dfs(w, vertices, adj_list, container)
        elif "active".__eq__(vertices[w].status):
            return
    
    vertex.status = "finished"
    container.append(vertex)
    

def longest_path(source, dest, postordering, adj_list, llp_list):
    
    for i in range(len(postordering)):
        target = ord(postordering[i].name) - 65

        if target == dest:
            llp_list[target] = 0
        else:
            llp_list[target] = -99999
            for j in range(len(adj_list[target])):
                w = adj_list[target][j][0]
                length = adj_list[target][j][1]
                llp_list[target] = max(llp_list[target], length + llp_list[w])
        
    return llp_list[source]
    
def main():

    weighted_adj_list = [ [[2, 5], [4, 3]], [], [[3, 10], [4, 6]], [], [], [[3, 5], [4, 4]] ]
    llp_list = [None, None, None, None, None, None]
    
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F")]
    
    postordering = post_process(vertices, weighted_adj_list)
    
    print(postordering)
    
    answer = longest_path(0, 4, postordering, weighted_adj_list, llp_list)
    
    print(answer)
    


    return


if __name__ == '__main__':
    main()