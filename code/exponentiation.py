
def slow_exp(a, n : int):
    x = a
    for i in range(2, n+1):
        # Remember that last number isnt included.
        # Hence n+1
        x = x * a
    return x

def pingala_exp(a, n: int):
    if n == 1:
        return a
    else:
        x = pingala_exp(a, n // 2)
        
        if n % 2 == 0:
            return x * x
        else:
            return x * x * a
    

def main():
    
    print(slow_exp(2, 4))
    print(pingala_exp(3, 4))
    
    
if __name__ == '__main__':
    main()