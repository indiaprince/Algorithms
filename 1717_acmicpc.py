import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())
disjoint_set = [i for i in range(N+1)]


def union(x,y):
    x_parent = find(x)
    y_parent = find(y)
    if(x_parent!=y_parent) : disjoint_set[x_parent] = y_parent

def find(x):
    if(x==disjoint_set[x]): return x
    disjoint_set[x] = find(disjoint_set[x])
    return disjoint_set[x]

def check(a,b):
    flag_a = find(a)
    flag_b = find(b)
    if(flag_a==flag_b):return True
    else : return False

for _ in range(M):
    num, a, b = map(int, sys.stdin.readline().split())
    if(num==0): union(a,b)
    elif(num==1): 
        if(check(a,b)): print('YES')
        else: print('NO')


