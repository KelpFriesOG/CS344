


def longest_path(source, dest, adj_list, llp_list):
    
    if source == dest:
        return 0
    if llp_list[source] == None:
        llp_list[source] = -99999
        for i in range(len(adj_list[source])):
            vertex = adj_list[source][i][0]
            length = adj_list[source][i][1]
            llp_list[source] = max(llp_list[source], length + longest_path(vertex, dest, adj_list, llp_list))

    return llp_list[source]

def main():
    
    weighted_adj_list = [ [[2, 5], [4, 3]], [[]], [[3, 10], [4, 6]], [], [], [[3, 5], [4, 4]] ]
    llp_list = [None, None, None, None, None, None]
    
    answer = longest_path(0, 4, weighted_adj_list, llp_list)
    
    print(answer)

    
    return

if __name__ == '__main__':
    main()