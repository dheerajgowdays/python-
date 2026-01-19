def fib(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo) 
    return memo[n]

def fun(n, m):
    count, idx = 0, 2 
    while True:
        value = fib(idx)  
        
        if value % m == 0: 
            count += 1
            if count == n:  
                return value  
        idx += 1  

n, m = 4, 3  
print(fun(n,m))