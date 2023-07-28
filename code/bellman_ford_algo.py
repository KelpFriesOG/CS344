def bellman_ford(src):

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
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                
                # We decipher the actual edge.
                # The 0th indexed value of the edge is the
                # head-end vertex.
                # The 1st indexed value of the edge is the
                # weight of the edge.
                # We use u and just another name for i
                v = edges[i][j][0]
                w = edges[i][j][1]
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
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            v = edges[i][j][0]
            w = edges[i][j][1]
            if dist[i] != float("Inf") and dist[i] + w < dist[v]:
                print("Negative cycle detected")
                return
            
                
    # After the algorithm is over we simply print out an informal
    # breakdown of what the dist array represents.
    
    for i in range(len(dist)):
        print("The minimum distance from", src, "to", i, "is", dist[i])


def main():
    
    # The vertices and edges array are declared
    # as global variables and then used throughout
    # the file without the need to pass them
    # as parameters.
    global vertices
    global edges
    
    # A graph of n vertices
    vertices = [0, 1, 2, 3, 4]
    
    # A 2D array in which the nth index contains the outgoing edges from the 
    # nth numbered vertex. Each outgoing edge contains two values, the 0th
    # value being the target vertex and the 1st index being weight of the edge.
    edges = [[[1, -1], [2, 4]], [[2, 3], [3, 2], [4, 2]], [], [[1, 1], [2, 5]], [[3, -3]]]

    # The Bellman Ford algorithm works with the vertices and the edges
    # array without needing to pass them, because the vertices and
    # edges array are declared as global variables.
    bellman_ford(0)
    
    # The Bellman-Ford algorithm prints the right answer with
    # respect to the given source index!
    
    # The algorithm DOES NOT change anything about the underlying
    # vertices and edges array but simply makes a new array and
    # fills it with the correct distances.
    
    return

if __name__ == '__main__':
    
    main()
    