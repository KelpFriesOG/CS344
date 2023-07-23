from queue import PriorityQueue

# WIP does not work as intented for now!

# Problem:
''' The built in priority in Python does not have a DecreaseKey function.
    If I want to replicate the behavior of this function I have two options:
    
    - Read the python documentation and understand the sifting operations
    and use them to delete a specific element and then insert the same element
    with a different weight.
    
    - Start from scratch and create (or creatively copy and credit) a OOP
    Priority Queue implementation which includes familiar operations including
    DecreaseKey!
    
    For practice I plan on choosing option 2 :)
    
    '''

class Vertex():
    MAX = 1000000
    
    def __init__(self, pos, prev = None, path = MAX, marked = False) -> None:
        self.pos = pos
        self.prev = prev
        self.path = path
        self.marked = marked
        
    def __repr__(self) -> str:
        return str(self.pos) + " min path = " + str(self.path)

def dijkstra(s, vertices, adj_list) -> None:
    
    init_sssp(vertices, s)
    pq = PriorityQueue()
    listified_pq = [None] * len(vertices)
    
    vertices[s].marked = True
    pq.put((vertices[s].path, vertices[s]))

    while not pq.empty:
        
        u = pq.get()
        for i in range(adj_list[u.pos]):
            
            v = vertices[adj_list[u.pos][i][0]]
            weight = adj_list[u.pos][i][1]
            
            if u.path + weight < v.path:
                relax(u, v, weight) # This already updates the value of v.path GLOBALLY
                
                if v.marked == True:
                    continue
                else:
                    v.marked = True
                    pq.put((v.path, v))
    return

def relax(u, v, weight) -> None:
    
    v.path = u.path + weight
    v.prev = u
    
    return

def init_sssp(vertices, s) -> None:
    
    source = vertices[s]
    source.path = 0
    source.prev = None
    
    for i in range(len(vertices)):
        if i != s:
            vertices[i].path = 1000000
            vertices[i].prev = None
            
    return
    
def main():
    
    vertices = [Vertex(0), Vertex(1), Vertex(2), 
                Vertex(3), Vertex(4), Vertex(5)]
    adj_list = [[[1, 7], [2, 12]], [[2, 2], [3, 9]], [[4, 10]], [[5, 1]], [[3, 4], [5, 5]], []]
    
    dijkstra(0, vertices, adj_list)
    
    for i in range(len(vertices)):
        print(vertices[i])
        print(vertices[i].marked)
    
    return
    

if __name__ == '__main__':
    main()
    