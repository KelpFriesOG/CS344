import datetime

def recursive_fib(X: int):
    if X > 2:
        return recursive_fib(X-1)+recursive_fib(X-2)
    else:
        return 1
    
def fast_fib(X: int, d: dict()):
    if(str(X) not in d):
        d[str(X)] = fast_fib(X-1, d) + fast_fib(X-2, d)
    return d[str(X)]

def iter_fib(X: int):
    F = [0] * X
    F[0] = 0
    F[1] = 1
    for i in range(2, X):
        F[i] = F[i-1] + F[i-2]
    return F[X-1]

def iter_fib2(X: int):
    prev = 1
    curr = 1
    
    for i in range(1, X):
        next = curr + prev
        prev = curr
        curr = next
    
    return curr
        
    
        


def main():

    # Testing recursive fib

    before = datetime.datetime.now()

    answer = recursive_fib(20)
    
    after = datetime.datetime.now()
    
    print("Recursive: ")
    
    print(answer)
    
    print("Time taken: " + str(after - before))
    
    # Testing fast fib
    
    d = {'1': 0, '2': 1}
    
    before = datetime.datetime.now()
    
    answer = fast_fib(500, d)
    
    after = datetime.datetime.now()
    
    print("Fast Fib: ")
    
    print(answer)
    
    print("Time taken: " + str(after - before))
    
    # Testing iter fib
    
    before = datetime.datetime.now()
    
    answer = iter_fib(500)
    
    after = datetime.datetime.now()
    
    print("Iterative Fib: ")
    
    print(answer)
    
    print("Time taken: " + str(after - before))
    
    # Testing iter fib 2
    
    before = datetime.datetime.now()
    
    answer = iter_fib2(500)
    
    after = datetime.datetime.now()
    
    print("Iterative Fib 2: ")
    
    print(answer)
    
    print("Time taken: " + str(after - before))
    
    
    
if __name__ == '__main__':
    main()
    