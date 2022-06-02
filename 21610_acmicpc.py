import sys
input = sys.stdin.readline

N,M = map(int, input().split())


m = [[] for _ in range(N)]
cloud = [[False for _ in range(N)] for _ in range(N)]
for i in range(N): m[i] = list(map(int, input().split()))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
bibaragi = [[N-1,1-1], [N-1,2-1], [N-1-1,1-1], [N-1-1,2-1]]
def dry(cloud):
    global m
    replace_bibaragi = []
    for i in range(N):
        for j in range(N):
            if(cloud[i][j]): continue  # visit 배열 만드는게 효율적
            if(m[i][j]>=2):  
                m[i][j]-=2
                replace_bibaragi.append([i,j])
    return replace_bibaragi
            
for _ in range(M):
    d, s = map(int, input().split())
    


    for i in range(len(bibaragi)):
        coord = bibaragi[i]
        coord[0] =  (coord[0] + s*dy[d-1])%N
        coord[1] =  (coord[1] + s*dx[d-1])%N
        m[coord[0]][coord[1]] +=1

        bibaragi[i] = coord
    cloud = [[False for _ in range(N)] for _ in range(N)]

    for bib in bibaragi: cloud[bib[0]][bib[1]] = True

    for i in range(len(bibaragi)):
        cnt = 0 
        for p in range(1,len(dx),2):
            copy_magic_r,copy_magic_c = bibaragi[i]

            diag_r,diag_c = copy_magic_r+dy[p],copy_magic_c+dx[p]

            if(0<=diag_r<N and 0<=diag_c<N):
                copy_magic = m[diag_r][diag_c]
                if(copy_magic>0): cnt+=1
        r,c = bibaragi[i]
        m[r][c] +=cnt
    bibaragi = dry(cloud)

res = 0
for mm in m : res+=sum(mm)
print(res) 