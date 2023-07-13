
# This vertex object will be used as part
# of a list of vertices that we will manipulate
# to show when and how each vertex was accessed.
class Vertex():
    
    def __init__(self, name, parent = None, pre = None, post = None) -> None:
        self.name = name
        self.parent = parent
        self.pre = pre
        self.post = post
    
    # When an object is printed in Python
    # the print function uses the __repr__
    # method that each object has
    # to get some string that represents
    # the object.
    
    # Here we are overriding the default
    # behavior of __repr__ so that we
    # can easily print the name
    # of the vertex as opposed
    # to its address in memory.
    def __repr__(self) -> str:
        return self.name
    


def dfs_all(vertices, adj_list, marks):
    
    clock = 0
    
    for i in range(len(marks)):
        marks[i] = False
    
    for i in range(len(marks)):
        if marks[i] == False:
            clock = dfs(i, vertices, adj_list, marks, clock)

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
    

def main():
    
    # This is the dag from the chapter 6 notes.
    vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"),
                Vertex("F")]
    adj_list = [[2, 4], [], [3, 4], [], [], [3, 4]]
    marks = [False, False, False, False, False, False]
    
    dfs_all(vertices, adj_list, marks)
    
    for i in range(len(vertices)):
        name = vertices[i].name
        parent = vertices[i].parent
    
        if parent != None:
            print("The parent of ", name, " is ", parent.name)

        else:
            print(name, " has no parent!")
    
    print()
    
    for i in range(len(vertices)):
        
        name = vertices[i].name
        pre = vertices[i].pre
        post = vertices[i].post
        
        print(name, " began processing at t = ", pre)
        print(name, " finished processing at t = ", post)
        
        print()

    preorder = sorted(vertices, key=lambda v: v.pre)
    print("Preordering (ordered by v.pre): ", preorder, "\n")
    
    postorder = sorted(vertices, key=lambda v: v.post)
    print("Postordering (ordered by v.post): ", postorder, "\n")



    print("A dynamic table / graph is still WIP, but try",
          "drawing one yourself to see how the intervals",
          "line up!")
    
    return


if __name__ == '__main__':
    main()