import sys
from collections import deque
input = sys.stdin.readline
R,C,T = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

A = [[] for _ in range(R)]
for i in range(R): A[i] = list(map(int, input().split()))
air_puri = []
for i in range(R):
    for j in range(C):
        if(A[i][j]==-1): air_puri.append((i,j))



for _ in range(T):

    
    B = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if(A[i][j]>0) : 
                spread = 0
                for d in range(4):
                    nr = i+dy[d]
                    nc = j+dx[d]
                    sp =  int(A[i][j]/5)
                    if(0<=nr<R and 0<=nc<C and ((nr,nc) not in air_puri)):
                        B[nr][nc] += sp
                        spread+=1
                B[i][j] = B[i][j] + A[i][j] - (sp)*spread
    
    top_r,top_c = air_puri[0]
    bot_r,bot_c = air_puri[1]
    
    air_flow = []
    before = deque()
    for i in range(top_c+1,C-1): 
        air_flow.append((top_r,i))
        before.append(B[top_r][i])
    for i in range(top_r,0, -1) : 
        air_flow.append((i,C-1))
        before.append(B[i][C-1])
    for i in range(C-1, 0, -1) : 
        air_flow.append((0,i)) 
        before.append(B[0][i])
    for i in range(0,top_r+1): 
        air_flow.append((i,0))
        before.append(B[i][0])
    for i in range(0,top_c): 
        air_flow.append((top_c,i))
        before.append(B[top_c][i])

    before.appendleft(before.pop())
    for i in range(len(air_flow)):
        r,c = air_flow[i]
        if(r==top_r and c==top_c) : B[r][c] = 0
        else: B[r][c] = before.popleft()
    
    air_flow = []
    before = deque()
    for i in range(bot_c+1,C-1):        #->
        air_flow.append((bot_r,i))
        before.append(B[bot_r][i])
    for i in range(bot_r,R) :           #bot
        air_flow.append((i,C-1))
        before.append(B[i][C-1])
    for i in range(C-2, 0, -1) :        #left
        air_flow.append((R-1,i)) 
        before.append(B[R-1][i])

    for i in range(R-1, bot_r-1, -1):     #up
        air_flow.append((i,0))
        before.append(B[i][0])
    for i in range(0,bot_c):    
        air_flow.append((bot_c,i))
        before.append(B[bot_c][i])
    before.appendleft(before.pop())



    for i in range(len(air_flow)):
        r,c = air_flow[i]
        if(r==bot_r and c==bot_c) : B[r][c] = 0
        else: B[r][c] = before.popleft()



    for i in range(R):
        for j in range(C):
            A[i][j] = B[i][j]
total = 0
for i in range(R): total+=sum(A[i])
print(total)