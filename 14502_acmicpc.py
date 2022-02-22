import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int, input().split())
ls = [[] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    ls[i]=tmp
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    if(ls[y][x]==1 or ls[y][x]==3): return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(0<=nx<M and 0<=ny<N):
            if(ls[ny][nx]==0):
                ls[ny][nx]=4
                dfs(nx,ny)

# 벽 3개 세우기
for i in range(N*M):
    if(ls[i//M][i%M]==1 or ls[i//M][i%M]==2): continue 
    for j in range(i,N*M):
        if(ls[j//M][j%M]==1 or ls[j//M][j%M]==2): continue
        for k in range(j,N*M):
            if(ls[k//M][k%M]==1 or ls[k//M][k%M]==2): continue
            if(i==j or j==k or k==i): continue

            ls[i//M][i%M]=3
            ls[j//M][j%M]=3
            ls[k//M][k%M]=3
            # DFS 
            for x in range(M):
                for y in range(N):
                    if(ls[y][x]==2): dfs(x,y)
            # counting max
            tmp = 0                    
            for x in range(M):
                for y in range(N):           
                    if(ls[y][x]==0): tmp+=1
            cnt = max(cnt,tmp)

            # recover
            for x in range(M):          
                for y in range(N):
                    if(ls[y][x]==4): ls[y][x]=0
        
            ls[i//M][i%M]=0
            ls[j//M][j%M]=0
            ls[k//M][k%M]=0

print(cnt)
