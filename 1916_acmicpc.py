import sys
import heapq

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
INF = (10**10)+1
dst = [INF] * (N+1)
M = int(input())

def dijkstra(start):
    q = []
    dst[start] = 0
    heapq.heappush(q, (0,start))
    while(q):
        dist, curr = heapq.heappop(q)
        if(dist> dst[curr]) : continue
        for destination, weight in graph[curr]:
            cost = weight + dist
            if(cost < dst[destination]) : 
                dst[destination] = cost
                heapq.heappush(q,(cost, destination))


for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

start, end = map(int, input().split())


dijkstra(start)
print(dst[end])