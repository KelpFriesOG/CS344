def recursive_dfs(s, adj_list, marks):
    if(marks[s] == False):
        marks[s] = True
        for i in range(len(adj_list[s])):
            recursive_dfs(adj_list[s][i], adj_list, marks)
    
    
def iter_dfs(s, adj_list, marks):
    stack = []
    stack.append(s)
    
    while len(stack) != 0:
        v = stack.pop()
        if marks[v] == False:
            marks[v] = True
            for i in range(len(adj_list[v])):
                stack.append(adj_list[v][i])


def main():
    
    adj_list = [[1, 2], [0, 2], [0, 1], [4], [3]]
    marks = [False, False, False, False, False]
    
    # If you want to try either method, make
    # sure to comment out the other!
    
    recursive_dfs(2, adj_list, marks)
    # iter_dfs(2, adj_list, marks)
    
    print(marks)
    

if __name__ == '__main__':
    main()