import sys
input = sys.stdin.readline

def Prime_func(N):
    Prime = []
    start = N
    end = 2*N
    isPrime = [True for _ in range(end+1)]
    for i in range(2,end+1):
        if(not isPrime[i]): continue
        if(N<i):
            if(isPrime[i]) : Prime.append(i)
        
        for  j in range(i*i,end+1,i):
            isPrime[j] = False
    return Prime

while(True):
    N = int(input())
    if(N==0): break
    ls = Prime_func(N)
    print(len(ls))