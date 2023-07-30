def shimbel(vertices, adj_list):
    
    dist = [[[0 for i in range(len(vertices))] for j in range(len(vertices))] for 
            k in range(len(vertices))]
    
    # DO NOT INITIALIZE THIS LIST OR ANY OTHER USING STAR NOTATION:
    # i.e. dist = [None * 5] * 5
    
    # Because for 2D or n-d lists, the inner list's reference is simply copied
    # over x times. This means that making a change to the inner list,
    # affects all copies of the reference. Thus doing dist[0][0] = 1,
    # changes an entire column (the 0th value) of every copy of the inner
    # list!
    
    for u in range(len(vertices)):
        for v in range(len(vertices)):
            if u == v:
                dist[u][v][0] = 0
            else:
                dist[u][v][0] = float("Inf")
    
    for l in range(1, len(vertices) - 1):
        for u in range(len(vertices)):
            for v in range(len(vertices)):
                if u != v:
                    
                    dist[u][v][l] = dist[u][v][l-1]
                    for i in range(len(adj_list)):
                        for j in range(len(adj_list[i])):
                            x = i
                            weight = adj_list[i][j][1]
                            if j == v and dist[u][v][l] > dist[u][x][l-1] + weight:
                                dist[u][v][l] = dist[u][x][l-1] + weight
    
    
    
    return dist


def main():
    
    adj_list = [[[2, -2]], [[0, 4], [2, 3]], [[3, 2]], [[1, -1]]]
    vertices = [0, 1, 2, 3]
    
    print(shimbel(vertices, adj_list))
    
    dist = shimbel(vertices, adj_list)
    
    print(dist[0][3])
    
    return

if __name__ == '__main__':
    main()