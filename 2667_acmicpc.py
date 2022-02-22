N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[False]*N for _ in range(N)]
def dfs(apart, i , j):
    global num
    if(apart[i][j]=='1') : num+=1
    else : return
    visit[i][j]=True
    for k in range(4):
        if(i+dx[k]<0 or i+dx[k]>len(apart)-1): continue
        if(j+dy[k]<0 or j+dy[k]>len(apart)-1): continue
        if(not visit[i+dx[k]][j+dy[k]]): 
            dfs(apart,i+dx[k],j+dy[k])



apart = [list(input()) for _ in range(N)]

ls = []
num = 0
count = 0
for i in range(N):
    for j in range(N):
        if(not visit[i][j] and apart[i][j]!='0'):
            count+=1
            dfs(apart,i,j)
            ls.append(num)
            num = 0
print(count)
ls.sort()
for i in range(count):
    print(ls[i])