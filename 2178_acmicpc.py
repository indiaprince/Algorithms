import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(r,c   ,m,   N,M):
    v = [[False for _ in range(M)] for _ in range(N)]
    move = 1
    v[0][0] = True
    q = deque([(0,0,move)])
    while(q):
        print(q)
        r,c,move = q.popleft()
        if(N-1==r and M-1==c): break

        for i in range(4):
            nr = r+ dy[i]
            nc = c+ dx[i]
            if(0<=nr<N and 0<=nc<M):
                if(m[nr][nc]=='1'):
                    if(not v[nr][nc]):
                        v[nr][nc] = True
                        q.append((nr,nc, move+1))
    return move

N,M = map(int, input().split())
m = [[] for _ in range(N)]
for i in range(N): m[i] = list(input()[:-1])


print(bfs(0,0,   m, N,M))
