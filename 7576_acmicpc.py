import sys
sys.setrecursionlimit(10**9)

cnt = 0
t = []

def dfs(i,j):
    global cnt
    px = [-1,1,0,0]
    py = [0,0,-1,1]
    if(t[i][j]==-1) :return
    for d in range(4):
        nx = px[d]+j
        ny = py[d]+i
        if(0<=nx<W and 0<=ny<H):
            if(t[ny][nx]==0):
                t[ny][nx]=1
                cnt=cnt+1
                dfs(ny,nx)
                

W, H = map(int, input().split())
for i in range(H):
    tmp = list(map(int, input().split()))
    t.append(tmp)
for i in range(H):
    for j in range(W):
        if(t[i][j]==1):
            dfs(i,j)
print(cnt)