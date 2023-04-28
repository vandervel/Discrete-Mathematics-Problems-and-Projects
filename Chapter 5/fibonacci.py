""" a comparison of computation time needed for 2 different implementations generating Fibonacci numbers,
both recursive and iterative. """




def fibonacci_r(n):
    
    if n == 0: return 0
    if n == 1: return 1
    
    
    return fibonacci_r(n-1) + fibonacci_r(n-2)

def fibonacci_i(n):
    
    a, b = 0, 1
    ops = 0
    
    for i in range(0, n):
        a, b = b, a + b
        
    
    
    
    return a
    
    
start_time = time.time()

print(fibonacci_r(10))

end_time = time.time()
print(end_time - start_time)

start_time = time.time()
print(fibonacci_i(10)  )  
end_time = time.time()
print(end_time - start_time)
