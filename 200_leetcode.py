import sys
sys.setrecursionlimit(10**6)
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

y_axis = len(grid)
x_axis = len(grid[0])

visit = [[False] * x_axis for _ in range(y_axis)]
cnt =0
def boundary(x,y):
    if(0<=x<x_axis and 0<=y<y_axis): return True
    return False

def dfs(x,y):
    if(grid[y][x]=='0'): return
    visit[y][x]= True
    for i in range(4):
        
        nx = x+dx[i]
        ny = y+dy[i]
        if(boundary(nx,ny)):
            grid[y][x]='0'
            dfs(nx,ny)


for y in range(y_axis):
    for x in range(x_axis):
        if(visit[y][x]==True or grid[y][x]=='0'): continue
        dfs(x,y)
        cnt+=1
print(cnt)