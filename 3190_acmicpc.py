import sys
from collections import deque
input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
m = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())
for _ in range(M): 
    r,c = map(int ,input().split())
    m[r-1][c-1] = 1  # apple

K = int(input())


direction_info = []
for i in range(K):
    X,C = map(str, input().split())
    direction_info.append((int(X), C))

direction_info.reverse()
init_r,init_c = 0,0
snake = deque([(init_r,init_c)])
Time = 0 
direction = 0 
while(True):
    Time+=1
    head_r, head_c = snake.pop()
    new_head_r = head_r + dy[direction%4]
    new_head_c = head_c + dx[direction%4]
    if(0>new_head_r or new_head_r >=N or 0>new_head_c or new_head_c >=N): break
    if((new_head_r,new_head_c) in snake): break
    if(m[new_head_r][new_head_c]==1) : 
        snake.append((head_r,head_c))
        snake.append((new_head_r,new_head_c))
        m[new_head_r][new_head_c] = 0 # delete apple
    else:
        snake.append((head_r,head_c))
        snake.append((new_head_r,new_head_c))
        snake.popleft()
    
    if(direction_info != []):
        x,c = direction_info.pop()
        if(x==Time):
            if(c=='D'): direction+=1
            elif(c=='L') : direction-=1
        else : 
            direction_info.append((x,c))
    

print(Time)