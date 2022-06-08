import sys
input = sys.stdin.readline


N, L, H = map(int, input().split())
m = [[] for _ in range(N)]
v = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N): m[i] = list(map(int, input().split()))
move = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(i,j,   m,v,   L,H, union):
    global Q
    if(v[i][j]!=0): return
    Q[union].append((i,j))
    v[i][j] = union
    for d in range(4):
        nx,ny = j+dx[d], i+dy[d]
        if(0<=nx<N and 0<=ny<N):
            if(L<=abs(m[i][j] - m[ny][nx])<=H):
                check(ny,nx, m,v,  L,H, union)

union = 1
while(True):
    union = 1
    v = [[0 for _ in range(N)] for _ in range(N)]
    Q=[[] for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            if(v[i][j] == 0):
                check(i,j,  m,v,   L,H, union)
                union+=1
    if((union-1)==N*N): break
    for i in range(1, len(Q)):
        if(len(Q[i])==0): break
        total_pop = 0
        for coord in Q[i]:
            y,x  = coord
            total_pop+=m[y][x]
        avg_pop = total_pop//len(Q[i])
        for coord in Q[i]:
            y,x  = coord
            m[y][x] = avg_pop
    move+=1
print(move)