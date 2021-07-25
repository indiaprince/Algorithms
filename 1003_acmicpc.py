def fib_mem(mem , n):
    for i in range(n+1):
        if i==0: 
            mem[i][0] = 1
            mem[i][1] = 0
        elif i ==1:
            mem[i][0] = 0
            mem[i][1] = 1
        else:
            mem[i][0] = mem[i-1][0] + mem[i-2][0]
            mem[i][1] = mem[i-1][1] + mem[i-2][1]
    return mem
    
ls = []
ls = [[0 for col in range(41)] for row in range(41)]


t = int(input())
for i in range(t):
    n = int(input())
    ls = fib_mem(ls,n)
    print(f"{ls[n][0]} {ls[n][1]}")
