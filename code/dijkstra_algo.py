from queue import PriorityQueue
from heapdict import heapdict

# Problem:
''' The built in priority in Python does not have a DecreaseKey function.
    If I want to replicate the behavior of this function I have two options:
    
    - Read the python documentation and understand the sifting operations
    and use them to delete a specific element and then insert the same element
    with a different weight.
    
    - Start from scratch and create (or creatively copy and credit) a OOP
    Priority Queue implementation which includes familiar operations including
    DecreaseKey!
    
    - Instead of using path and previous as properties attached to vertex objects,
    I can use two arrays that store the prev and path value for each vertex globally!
    
    I choose option 3 because I am lazy. I suggest using option 2 for practice.
    
    UPDATE: IT WORKS!
    
    '''

class Vertex():
    MAX = 1000000
    
    def __init__(self, pos, marked = False) -> None:
        self.pos = pos
        self.marked = marked
        
    def __repr__(self) -> str:
        return str(self.pos) + " min path = " + str(self.path)

def dijkstra(s, vertices, adj_list) -> None:
    
    init_sssp(vertices, s)
    pq = PriorityQueue()
    pq = heapdict()
    
    print("Starting")
    
    vertices[s].marked = True
    pq[vertices[s]] = paths[s]
    
    while len(pq) != 0:
        
        u = pq.popitem()[0]
        
        for i in range(len(adj_list[u.pos])):
            v = vertices[adj_list[u.pos][i][0]]
            weight = adj_list[u.pos][i][1]
            
            if paths[u.pos] + weight < paths[v.pos]:
                
                relax(u, v, weight)
                
                if v.marked == True:
                    pq[v] = paths[v.pos]
                else:
                    v.marked = True
                    pq[v] = paths[v.pos]
                    
        
        
    # print("Starting...")
    
    # vertices[s].marked = True
    # pq.put((paths[s], vertices[s]))

    # while pq.qsize() != 0:
        
    #     u = pq.get()[1]
    #     for i in range(len(adj_list[u.pos])):
            
    #         v = vertices[adj_list[u.pos][i][0]]
    #         weight = adj_list[u.pos][i][1]
            
    #         if paths[u.pos] + weight < paths[v.pos]:
                
    #             relax(u, v, weight) # This already updates the value of v.path GLOBALLY
                
    #             if v.marked == True:
    #                 continue
    #             else:
    #                 v.marked = True
    #                 pq.put((paths[v.pos], v))
    return

def relax(u, v, weight) -> None:
    
    # v.path = u.path + weight
    # v.prev = u
    
    paths[v.pos] = paths[u.pos] + weight
    preds[v.pos] = u
    
    return

def init_sssp(vertices, s) -> None:
    
    paths[s] = 0
    preds[s] = None
    
    for i in range(len(vertices)):
        if i != s:
            paths[i] = float("Inf")
            preds[i] = None
            
    return
    
def main():
    
    vertices = [Vertex(0), Vertex(1), Vertex(2), 
                Vertex(3), Vertex(4), Vertex(5)]
    adj_list = [[[1, 7], [2, 12]], [[2, 2], [3, 9]], [[4, 10]], [[5, 1]], [[3, 4], [5, 5]], []]
    
    adj_list = [[[2, -2]], [[0, 4], [2, 3]], [[3, 2]], [[1, -1]], [[0, 0], [1, 0], [2, 0], [3, 0]]]
    vertices = [Vertex(0), Vertex(1), Vertex(2), Vertex(3), Vertex(4)]
    
    global paths
    global preds
    
    paths = [None] * len(vertices)
    
    preds = [None] * len(vertices)
    
    source = 4
    
    dijkstra(source, vertices, adj_list)
    
    for i in range(len(vertices)):
        print("Shortest path length from", source, "to", i, "is", paths[i])
    
    return
    

if __name__ == '__main__':
    main()
    