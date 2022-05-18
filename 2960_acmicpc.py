import sys
input = sys.stdin.readline

N,K = map(int, input().split())


def Prime_func(N,K):
    Prime = []
    cnt = 0
    isPrime = [True for _ in range(N+1)]
    for i in range(2,N+1): 
        if(isPrime[i]): Prime.append(i)
        for j in range(i,N+1,i):
            if(not isPrime[j]) : continue
            isPrime[j] = False            
            cnt+=1
            if(cnt==K) : return j



print(Prime_func(N,K))