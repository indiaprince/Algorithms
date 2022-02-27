import sys
input = sys.stdin.readline
from collections import deque

def draw(graph,N):
    for i in range(N):
        print(graph[i])

dx = [0,1,0,-1]   #up, left, down, right
dy = [-1,0,1,0]
v= []

N,M = map(int, input().split())
r,c, d = map(int, input().split()) # r은 북쪽, c은 서쪽
graph = [[] for _ in range(N)]
for i in range(N): graph[i] = list(map(int, input().split()))

cnt =2
x = c
y = r
direction = d
while(1):
    graph[y][x]=cnt     # 1번
    if(graph[y+dy[(direction-1)%4]][x+dx[(direction-1)%4]]!=0 and graph[y+dy[(direction-2)%4]][x+dx[(direction-2)%4]]==1 and graph[y+dy[(direction-3)%4]][x+dx[(direction-3)%4]]!=0 and graph[y+dy[(direction-4)%4]][x+dx[(direction-4)%4]]!=0): 
        break
    if(graph[y+dy[(direction-1)%4]][x+dx[(direction-1)%4]]!=0 and graph[y+dy[(direction-2)%4]][x+dx[(direction-2)%4]]!=0 and graph[y+dy[(direction-3)%4]][x+dx[(direction-3)%4]]!=0 and graph[y+dy[(direction-4)%4]][x+dx[(direction-4)%4]]!=0):
        x = x+dx[(direction-2)%4]
        y = y+dy[(direction-2)%4] 
        continue
    if(graph[y+dy[(direction-1)%4]][x+dx[(direction-1)%4]]==0):  #청소하지 않은 칸 
        x= x+dx[(direction-1)%4]           # 전진, 회전
        y= y+dy[(direction-1)%4]           # 전지, 회전
        cnt+=1
        direction = (direction-1)%4
        continue
    else: 
        direction=(direction-1)%4
        continue
#draw(graph,N)
print(cnt-1)