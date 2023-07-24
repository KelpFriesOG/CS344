from queue import PriorityQueue

class Vertex():
    MAX = 1000000
    
    def __init__(self, pos, marked = False) -> None:
        self.pos = pos
        self.marked = marked
        
    def __repr__(self) -> str:
        return str(self.pos) + " min path = " + str(self.path)

    def __eq__(self, __value: object) -> bool:
        
        if type(__value) != type(self):
            return False
        
        if self.pos == __value.pos:
            return True
        
        return False
    
    def __lt__(self, __value: object) -> bool:
        
        if type(__value) != type(self):
            return False
        
        if self.pos < __value.pos:
            return True
        
        return False
        

def nn_dijkstra(s, vertices, adj_list, paths, preds):

    init_sssp(vertices, s, paths, preds)
    pq = PriorityQueue()
    
    print("Starting...")

    for i in range(len(vertices)):
        # vertices[i].marked = True
        pq.put((paths[i], vertices[i]))

    while pq.qsize() != 0:
        
        u = pq.get()[1]
        for i in range(len(adj_list[u.pos])):
            
            v = vertices[adj_list[u.pos][i][0]]
            weight = adj_list[u.pos][i][1]
            
            if paths[u.pos] + weight < paths[v.pos]:
                
                relax(u, v, weight, paths, preds) # This already updates the value of v.path GLOBALLY
                
                

    return

def init_sssp(vertices, s, paths, preds) -> None:
    
    paths[s] = 0
    preds[s] = None
    
    for i in range(len(vertices)):
        if i != s:
            paths[i] = 1000000
            preds[i] = None
            
    return

def relax(u, v, weight, paths, preds) -> None:
    
    # v.path = u.path + weight
    # v.prev = u
    
    paths[v.pos] = paths[u.pos] + weight
    preds[v.pos] = u
    
    return

def main():
    
    vertices = [Vertex(0), Vertex(1), Vertex(2), 
                Vertex(3), Vertex(4), Vertex(5)]
    adj_list = [[[1, 7], [2, 12]], [[2, 2], [3, 9]], [[4, 10]], [[5, 1]], [[3, 4], [5, 5]], []]
    
    paths = [1000000] * len(vertices)
    
    preds = [None] * len(vertices)
    
    source = 0
    
    nn_dijkstra(source, vertices, adj_list, paths, preds)
    
    for i in range(len(vertices)):
        print("Shortest path length from", source, "to", i, "is", paths[i])
    
    return
    
    return

if __name__ == '__main__':
    
    main()