
    
def fibonacci(N):
        if N<=1:
            return N
        else:
            
            return fibonacci(N-2)+fibonacci(N-1)
for N in range(1,31):        
    print(fibonacci(N))
