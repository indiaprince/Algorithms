# 인접 리스트
# T = int(input())
# for _ in range(T):
#     W, H, N = map(int, input().split())

#     land = [[] for _ in range(W)]

#     print(land)
#     for _ in range(N):
#         x,y = map(int, input().split())
#         land[x].append(y)
#     print(land)    
    

# 인접 행렬

def dfs2(i, j):
    dx = [1, -1, 0 ,0]
    dy = [0, 0 ,-1, 1]
    land[j][i] = 0
    for d in range(4):
        nx = dx[d]+i
        ny = dy[d]+j
        if (nx< 0 or nx>len(land[0])-1 or ny <0 or ny>len(land)-1) : continue
        if (land[ny][nx]==1):
            dfs2(nx,ny)
    return 0


def dfs(i, j):
    dx = [1, -1, 0 ,0]
    dy = [0, 0 ,-1, 1]
    for d in range(4):
        nx = dx[d]+i
        ny = dy[d]+j
        if ( nx< 0 or nx>len(land[0])-1 or ny <0 or ny>len(land)-1) : continue
        if (land[ny][nx]==1 and visited[ny][nx]==0):
            visited[ny][nx] = 1
            dfs(nx,ny)
    return 

def makegraph(land):
        for i in range(len(land)):
            for j in range(len(land[0])):
                print(land[i][j] , end ="")
            print()
        print("------------------")
        
T = int(input())
for _ in range(T):
    W, H, N = map(int, input().split())

    land = [[0 for _ in range(W)] for _ in range(H)]
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for _ in range(N):
        x,y = map(int, input().split())
        land[y][x]=1
    count=0
    for i in range(W):
        for j in range(H):
            if(land[j][i]==1 and visited[j][i]==0):
                visited[j][i] = 1
                dfs2(i,j)
                count+=1
                makegraph(visited)
                print(count)
    print(count)

