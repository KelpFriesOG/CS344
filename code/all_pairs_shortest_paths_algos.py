from queue import PriorityQueue
from heapdict import heapdict

class Vertex():
    MAX = 1000000
    
    def __init__(self, pos, marked = False) -> None:
        self.pos = pos
        self.marked = marked
        
    def __repr__(self) -> str:
        return str(self.pos) + " min path = " + str(self.path)

def bellman_ford(vertices, adj_list, src):
    
    # All the distance values are
    # initialized to 0, with the exception
    # of the distance from the source to itself
    # which is suitably initialized to 0 and
    # (and never changes unless there is a
    # negatively weighted cycle).
    dist = [float("Inf")] * len(vertices)
    dist[src] = 0
    
    # We limit this algorithm to have V - 1
    # iterations because we know that finding
    # the SSSP from s to every other vertex
    # will take at most V - 1 iterations
    # (unless there are negative cycles).
    for _ in range(len(vertices) - 1):
        
        # We go through the entire edge list,
        # i will contain the index of the tail end vertex
        # and j will contain the edge itself (which has two values)
        for i in range(len(adj_list)):
            for j in range(len(adj_list[i])):
                
                # We decipher the actual edge.
                # The 0th indexed value of the edge is the
                # head-end vertex.
                # The 1st indexed value of the edge is the
                # weight of the edge.
                # We use u and just another name for i
                v = adj_list[i][j][0]
                w = adj_list[i][j][1]
                u = i
                
                # If the current dist of the tail end vertex, dist[u],
                # is not infinity and if the sum
                # of that distance and the weight of the
                # edge ,u -> v, is less than the current dist value
                # stored in the outgoing vertex, dist[v], then
                # we minimize dist[v] by setting it equal to
                # dist[u] + w
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    # After V - 1 iterations on the graph with the SSSP algorithm,
    # if there is still an edge which can be minimized, this 
    # indicates that whatever edge that is left to minimized can
    # minimized indefinitely (infinitely). This
    # indicates the presence of a negative loop.
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            v = adj_list[i][j][0]
            w = adj_list[i][j][1]
            if dist[i] != float("Inf") and dist[i] + w < dist[v]:
                print("Negative cycle detected")
                return []
            
                
    # After the algorithm is over we simply print out an informal
    # breakdown of what the dist array represents.
    
    return dist

def dijkstra(s, vertices, adj_list):
    
    dist = [float("Inf")] * len(vertices)
    
    preds = [None] * len(vertices)
    
    pq = heapdict() # as opposed to PriorityQueue
    
    dist[s] = 0
    
    print("Starting")
    
    vertices[s].marked = True
    pq[vertices[s]] = dist[s]
    
    while len(pq) != 0:
        
        u = pq.popitem()[0]
        
        for i in range(len(adj_list[u.pos])):
            
            v = vertices[adj_list[u.pos][i][0]]
            weight = adj_list[u.pos][i][1]
            
            if dist[u.pos] + weight < dist[v.pos]:
                
                result = relax(u, v, weight, dist)
                dist[v.pos] = result[0]
                preds[v.pos] = result[1]
                
                if v.marked == True:
                    pq[v] = dist[v.pos]
                else:
                    v.marked = True
                    pq[v] = dist[v.pos]

    return dist

def relax(u, v, weight, dist) -> None:
    
    # v.path = u.path + weight
    # v.prev = u
    
    return [dist[u.pos] + weight, u]
    
def johnson(vertices, adj_list):
    
    # Add an artifical source vertex
    
    vertices.append(Vertex(len(vertices)))
    adj_list.append([])
    
    for i in range(len(vertices) - 1):
        adj_list[len(vertices) - 1].append([i, 0])
    
    # Compute vertex prices (minimum distances from the
    # artifical vertex) and fail gracefully if needed.
    
    bf_distances = bellman_ford(vertices, adj_list, len(vertices) - 1)
    
    if len(bf_distances) == 0:
        print("Negative cycle detected!")
        return None
    
    # Reweight every edge
    for i in range(len(vertices) - 1):
        neighbors = adj_list[i]
        for neighbor in neighbors:
            u = i
            v = neighbor[0]
            neighbor[1] = bf_distances[u] + neighbor[1] - bf_distances[v]
    
    dj_distances = []
    
    # Extra step remove s:
    del vertices[-1]
    del adj_list[-1]
    
    # Compute reweighted shortest path distance
    # with the reweighted edges.
    for i in range(len(vertices)):
        result = dijkstra(i, vertices, adj_list)
        dj_distances.append(result)
    
    # Compute the original shortest path distances
    for u in range(len(vertices)):
        for v in range(len(vertices)):
            if dj_distances[u][v] == float("Inf"):
                continue
            dj_distances[u][v] += (bf_distances[v] - bf_distances[u])
            
    
    return dj_distances

def main():
    
     # print("Starting...")
    
    adj_list = [[[2, -2]], [[0, 4], [2, 3]], [[3, 2]], [[1, -1]]]
    vertices = [Vertex(0), Vertex(1), Vertex(2), Vertex(3)]
    
    result = johnson(vertices, adj_list)
    
    for i in range(len(result)):
        print(result[i])
    
    return

if __name__ == '__main__':
    main()