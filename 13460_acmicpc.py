import sys
input = sys.stdin.readline
from collections import deque
rx = ry = bx = by = 0
hole_x = hole_y = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def draw(graph):
    for i in range(len(graph)):
        print(graph[i])

def init(graph,N,M):
    rx,ry,bx,by,hole_x,hole_y = 0,0,0,0,0,0
    for i in range(N):
        for j in range(M):
            if(graph[i][j]=='O'): hole_x, hole_y=j,i
            if(graph[i][j]=='R'): rx, ry=j,i
            if(graph[i][j]=='B'): bx, by=j,i
    return rx,ry,bx,by,hole_x,hole_y

def bfs(rx,ry,bx,by):
    q = deque()
    q.append((rx,ry,bx,by))
    visited = []
    visited.append((rx,ry,bx,by))
    count = 0
    while(q):
        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()
            if(count>10): return -1
            if(graph[ry][rx]=='O'): return count

            for i in range(4):
                nrx,nry, nbx,nby = rx, ry, bx,by
                b_count = 0
                r_count = 0


                while(True):
                    nrx,nry = nrx+dx[i], nry+dy[i]
                    if(graph[nry][nrx]=='#'): 
                        nrx -=dx[i] 
                        nry -=dy[i]
                        break
                    if(graph[nry][nrx]=='O'): 
                        break
                    r_count+=1


                while(True):
                    nbx,nby = nbx+dx[i], nby+dy[i]
                    if(graph[nby][nbx]=='#'): 
                        nbx -=dx[i]
                        nby -=dy[i]
                        break
                    if(graph[nby][nbx]=='O'): break
                    b_count+=1
                if(graph[nby][nbx]=='O') : continue




                if(nrx==nbx and nry==nby) : 
                    dst_r = abs(nrx-rx) + abs(nry-ry)   
                    dst_b = abs(nbx-bx) + abs(nby-by)
                    if(dst_r>dst_b):
                        nrx -=dx[i] 
                        nry -=dy[i]
                    else :
                        nbx -=dx[i]
                        nby -=dy[i]


                if((nrx,nry,nbx,nby) not in visited):                
                    visited.append((nrx,nry,nbx,nby))
                    q.append((nrx,nry,nbx,nby))

        count+=1
    return -1

N,M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i]  = list(input()[:-1])

#draw(graph)
rx,ry,bx,by,hole_x,hole_y = init(graph, N, M)

#print(f"hole {hole_x, hole_y}     R  {rx,ry}   B {bx,by}")


cnt = bfs(rx,ry,bx,by)

print(cnt)

