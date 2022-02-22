from multiprocessing import cpu_count
import sys
input = sys.stdin.readline
from collections import deque

dx = [0,-1,0,1]   #up, left, down, right
dy = [-1,0,1,0]
v= []
flag = False
def blocked(x,y):
    if(graph[y+1][x]!=0 and graph[y-1][x]!=0 and graph[y][x+1]!=0 and graph[y][x-1]!=0): return True
    return False
                    

        

def draw(graph,N):
    for i in range(N):
        print(graph[i])


count = -1
def dfs(x, y, d):
    global count
    global flag
    if(flag) : return
    if (x,y) in v: return
    graph[y][x]=count
    count-=1
    v.append((x,y))
    if(blocked(x,y)):
        print(f"blocked {x}, {y}, {d}")
        nd = (d+2)%4
        nx = x+dx[nd]
        ny = y+dy[nd]
        if(graph[ny][nx]==1): flag=True
        return
    else:
        for i in range(1,5): 
                nd = (d+i)%4
                nx,ny = x+dx[nd], y+dy[nd]
                if(graph[ny][nx]==1): continue
                if (nx,ny) not in v: dfs(nx,ny,nd)


N,M = map(int, input().split())
r,c, d = map(int, input().split()) # r은 북쪽, c은 서쪽


graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

#draw(graph,N)

dfs(c, r, d)
#print()
#draw(graph,N)
print(len(v))
draw(graph,N)