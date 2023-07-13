
def subset_sum(X, i: int, T: int):
    if T == 0:
        return True
    elif T < 0 or i == 0:
        return False
    else:
        with_set = subset_sum(X, i-1, T-X[i])
        without_set = subset_sum(X, i-1, T)
        return with_set or without_set
        
    
def construct_subset(X, i: int, T: int):
    if T == 0:
        return []
    if T < 0 or len(X) == 0:
        return None
    Y = construct_subset(X, i - 1, T)
    if Y != None:
        return Y
    Y = construct_subset(X, i - 1, T - X[i])
    if Y != None:
        return Y.append(X[i])
    return None


def main():
    X = [3, 5, 1, 8, 11, 6, 9]
    target = 15
    print(subset_sum(X, len(X)-1, target))
    print(construct_subset(X, len(X)-1, target))

if __name__ == '__main__':
    main()