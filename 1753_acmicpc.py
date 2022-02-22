import sys
input = sys.stdin.readline
import heapq


V,E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
INF = 10**9
dst = [INF] * (V+1)

def findmindst(start):
    dst[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while(q):
        dist, curr = heapq.heappop(q)
        if(dst[curr] < dist): continue
        for v, w in graph[curr]:
            cost = dist + w
            if(cost<dst[v]) : 
                dst[v] = cost
                heapq.heappush(q, (cost,v))

for i in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
findmindst(start)


for dist in dst[1:]:
    if(dist==1000000000) : print("INF")
    else: print(dist)


