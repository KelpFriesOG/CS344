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


# Not used, just as reference
def dfs_all(vertices, adj_list, marks):
    
    clock = 0
    
    for i in range(len(marks)):
        marks[i] = False
    
    for i in range(len(marks)):
        if marks[i] == False:
            clock = dfs(i, vertices, adj_list, marks, clock)

# Not used, just as reference
def dfs(pos, vertices, adj_list, marks, clock):
    
    marks[pos] = True
    vertex = vertices[pos]
    
    clock = clock + 1
    
    vertex.pre = clock
    
    for j in range(len(adj_list[pos])):
        w = adj_list[pos][j]
        if marks[w] == False:
            vertices[w].parent = vertex
            clock = dfs(w, vertices, adj_list, marks, clock)
    
    clock = clock + 1
    
    vertex.post = clock
    
    return clock
    
def is_acyclic(vertices, adj_list):
    
    for i in range(len(vertices)):
        vertices[i].status = "new"
    
    for i in range(len(vertices)):
        
        if "new".__eq__(vertices[i].status):
            if is_acyclic_dfs(i, vertices, adj_list) == False:
                return False
    
    return True

def is_acyclic_dfs(pos, vertices, adj_list) -> bool:

    vertex = vertices[pos]
    vertex.status = "active"
    
    for j in range(len(adj_list[pos])):
        w = adj_list[pos][j]
        
        if "active".__eq__(vertices[w].status):
            return False
    
        elif "new".__eq__(vertices[w].status):
            if is_acyclic_dfs(w, vertices, adj_list) == False:
                return False
        
    
    vertex.status = "finished"
    return True

# Test on an acyclic graph          
def test1():
    
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [], [3, 4]]
    marks = [False, False, False, False, False, False]
    
    result = is_acyclic(vertices, adj_list)
    
    assert result == True

# Test for detection of loops
def test2():
    
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [0], [3, 4]]
    marks = [False, False, False, False, False, False]
    
    result = is_acyclic(vertices, adj_list)
    
    assert result == False

# Test for detection of self-loops    
def test3():
    
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[0, 2, 4], [], [3, 4], [], [], [3, 4]]
    marks = [False, False, False, False, False, False]
    
    result = is_acyclic(vertices, adj_list)
    
    assert result == False

def main():
    
    # This is the dag from the chapter 6 notes.
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [], [3, 4]]
    
    result = is_acyclic(vertices, adj_list)
    
    if result == True: print("The graph is acyclic!")
    else: print("The graph is cyclic!")
    
    # The unit tests here try some common scenarios:
    # acyclic graphs, graphs with a loop, and graphs with self loops.
    try:
        test1()
        test2()
        test3()
        print("Unit tests went smoothly too!")
    except AssertionError as e:
        print(e.with_traceback)
        
    return


if __name__ == '__main__':
    main()