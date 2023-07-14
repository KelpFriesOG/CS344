
# Data regarding each vertex will
# be self contained in the vertex itself!
class Vertex():
    
    # Constructor for each vertex,
    # will only require the user to enter
    # a name, the rest will be defaulted.
    def __init__(self, name, low = 0, root = None, pre = 0) -> None:
        
        self.name = name
        self.low = low
        self.root = root
        self.pre = pre
        self.marked = False

    # When printing a list of vertices,
    # this is similar to overriding
    # the toString() method of an
    # object in Java. Run the program
    # to see what I mean!
    def __repr__(self) -> str:
        return self.name + " rooted at: " + self.root.name


def tarjan(vertices, adj_list):
    
    # Initializing the clock and the stack
    clock = 0
    process_stack = []
    
    # Resetting the core properties
    # of each vertex object in the list
    # of the vertices.
    for i in range(len(vertices)):
        vertices[i].pre = vertices[i].low = 0
        vertices[i].marked = False
        vertices[i].root = None
    
    # Go through the list of vertices
    # and activate a DFS on each unmarked
    # vertex.   
    for i in range(len(vertices)):
        v = vertices[i]
        # If the vertex is unmarked, we
        # start our dfs traversal.
        if not v.marked:
            tarjan_dfs(i, vertices, adj_list, clock, process_stack)

def tarjan_dfs(pos, vertices, adj_list, clock, container):
    
    v = vertices[pos]
    
    # We first mark the vertex we are working on!
    v.marked = True
    
    # We increment the clock
    clock += 1
    
    # The processing of this vertex begins now!
    v.pre = clock
    
    # By default, before looking at the
    # descendants of v, we can say that
    # v.low is at most v.pre, so
    # either v.low remains unchanged,
    # or it gets smaller later.
    v.low = v.pre
    
    # We are processing v, therefore
    # we add it, (the entire object, not
    # just its index) to the stack.
    container.append(v)
    
    # For each outgoing edge from v, v-> w
    for i in range(len(adj_list[pos])):
        
        # IMPORTANT: We assume that the entered vertexes
        # in the adj_list are lower case letters.
        # IF THEY ARE NOT LOWERCASE LETTERS THIS ALGORITHM
        # FAILS.
        
        # We use ord() to get the ascii value of each letter
        # and then shift it down by 97 to get an appropriate
        # index such that 'a' -> 0, 'b' -> 1, e.t.c
        w_index = ord(adj_list[pos][i]) - 97
        
        # Based on the prior index, and assuming that
        # the vertices list is ordered by index, we
        # can get the vertex object that corresponds with
        # the index.
        w = vertices[w_index]
        
        # If the vertex w is not marked...
        if not w.marked:
            
            # We recursively call tarjan_dfs() on it
            # since it is a descendant of v.
            tarjan_dfs(w_index, vertices, adj_list, clock, container)
            
            # The recursive call should have popped up to
            # set the value of w.low. If w.low < v.low
            # Then v.low is set to w.low, else v.low remains
            # unchanged.
            # If the value of v.low remains unchanged after
            # the line below, then we can determine
            # that v is the root of a strong component
            # which is also a sink, that check
            # is coming up soon!
            v.low = min(v.low, w.low)
        
        # If w was marked, then we check if
        # it has a root, if it does, then
        # its been processes and we do nothing.
        # Otherwise we check...
        elif w.root == None:
            
            # If w.pre is less than v.low, that
            # means that w is a parent of v. 
            # (It cannot mean)
            # In either case, this means that we
            # SHOULD NOT pop the stack yet.
            # To make sure we don't pop the stack,
            # the value of v.low is changed!
            v.low = min(v.low, w.pre)
    
    # If v.low is still equal to v.pre after going
    # through all its reachable vertices, that
    # means that v is the root of a sink component.
    if v.low == v.pre:
        
        # We perform a loop where we pop of
        # each vertex in the strong sink component,
        # until we hit the root of the sink.
        # Keep in mind that
        w = None
        while w != v:
            w = container.pop()
            w.root = v
    
    

def main():
    
    vertices = [Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d'),
                Vertex('e'), Vertex('f'), Vertex('g'), Vertex('h'),
                Vertex('i'), Vertex('j'), Vertex('k'), Vertex('l'),
                Vertex('m'), Vertex('n'), Vertex('o'), Vertex('p')]
    
    adj_list = [['b'], [ 'f' ], ['h'], ['c'], 
                [ 'f', 'i' ], ['g', 'l' ], ['a', 'c', 'k' ], ['d', 'l'], 
                [ 'n' ], [ 'k', 'm' ], [ 'h', 'l' ], ['o', 'p'], 
                [ 'i' ], [ 'j', 'o' ], [ 'k' ], []]
    
    tarjan(vertices, adj_list)
    
    print(sorted(vertices, key=lambda v: v.root.name))
    
    print("Holy crap it worked!")
    
    return

if __name__ == '__main__':
    main()