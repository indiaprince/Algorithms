import sys
from collections import deque
input = sys.stdin.readline


# 한 칸에 물고기 한 마리
# 처음 아기 상어 크기는 2, 1초에 상하좌우 한 칸 이동

# 자기보다 큰 물고기 있는 칸은 못 지남
# 자기보다 크기 작으면 먹을 수 있음
# 크기가 같은 물고기는 먹을 수 없지만 칸을 지나갈 수 있다. 

# 이동 결정은 다음과 같이
# 물고기가 없으면 엄마 부름
# 먹을 수 있는 물고기 하나면 그거 먹으러 감
# 먹을 수 있는 물고기 두 마리 이상이면 거리가 가장 가까운 물고기 먹으러 간다.
    # 지나가는 칸의 최소가 가장 가까운 거리.
    # 가까운게 여러개면 가장 위, 그게 여러 개면 왼쪽 물고기 먹는다.
# 자기 크기와 같은 수의 물고기 먹으면 크기 +1
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def find_closest_fish_bfs(Shark_r,Shark_c,Shark_size, m,N):
    v = [[0 for _ in range(N)] for _ in range(N)]
    v[Shark_r][Shark_c] = True
    dist = 0
    q = deque([(Shark_r,Shark_c, dist)])
    closest_fish_r,closest_fish_c = -1,-1
    candidate = []
    while(q):
        curr=q.popleft()
        curr_r,curr_c, dist = curr
        if(0<m[curr_r][curr_c]<Shark_size):
            closest_fish_r,closest_fish_c = curr_r,curr_c
            candidate.append((closest_fish_r,closest_fish_c,dist))

        for d in range(4):
            nr = curr_r + dy[d]
            nc = curr_c + dx[d]
            if(0<=nr<N and 0<=nc<N):
                if(not v[nr][nc]):
                    if(m[nr][nc]==0 or m[nr][nc]<=Shark_size):
                        v[nr][nc] = True
                        q.append((nr,nc, dist+1))

    min_dist = 10000
    for candi in candidate:
        r,c,d = candi
        if(d<min_dist): 
            min_dist = d
            closest_fish_r = r
            closest_fish_c = c
        if(d==min_dist):
            if(r<closest_fish_r):
                closest_fish_r = r
                closest_fish_c = c
            elif(r==closest_fish_r):
                if(c<closest_fish_c):
                    closest_fish_r = r
                    closest_fish_c = c
    return closest_fish_r,closest_fish_c,min_dist


Shark_r,Shark_c,Shark_size = 0, 0, 2
left_fish = 0
N = int(input())
m = [[] for _ in range(N)]
for i in range(N): m[i] = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if(m[i][j]!=0):
            if(m[i][j]==9): 
                Shark_r,Shark_c = i,j 
                m[i][j] = 0
            else: left_fish+=1

Time = 0
eaten = 0
while(True):

    if(left_fish==0) : break
    fish_r,fish_c,dist = find_closest_fish_bfs(Shark_r,Shark_c,Shark_size, m,N)
    if(fish_r==-1 and fish_c==-1) : break
    Time+=dist
    m[fish_r][fish_c] = 0
    Shark_r,Shark_c = fish_r,fish_c
    left_fish-=1
    eaten+=1
    if(eaten==Shark_size):
        eaten=0
        Shark_size+=1
print(Time)






