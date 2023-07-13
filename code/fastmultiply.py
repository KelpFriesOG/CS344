import math

def split_multiply(x: int, y: int, n: int):
    if(n == 1):
        return x * y
    else:
        m = math.ceil(n / 2)
        ten_raised = math.pow(10, m)
        a = x // ten_raised
        b = x % ten_raised
        c = y // ten_raised
        d = y % ten_raised
        e = split_multiply(a, c, m)
        f = split_multiply(b, d, m)
        g = split_multiply(b, c, m)
        h = split_multiply(a, d, m)
        
        return (
        
        math.pow(10, 2 * m) * e + ten_raised * (g + h) + f 
        
        )

def fast_multiply(x: int, y: int, n: int):
    if(n == 1):
        return x * y
    else:
        m = math.ceil(n / 2)
        ten_raised = math.pow(10, m)
        a = x // ten_raised
        b = x % ten_raised
        c = y // ten_raised
        d = y % ten_raised
        e = fast_multiply(a, c, m)
        f = fast_multiply(b, d, m)
        g = fast_multiply(a - b, c - d, m)
        return ( 
            
        math.pow(10, 2 * m) * e + ten_raised * (e + f - g) + f
        
        )
    
    
    
    


def main():
    
    result = fast_multiply(25, 24, 2)
    print("The result : ", result)
    

if __name__ == '__main__':
    main()