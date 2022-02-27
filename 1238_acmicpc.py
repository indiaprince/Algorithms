import sys
input = sys.stdin.readline
import heapq

N, M, end = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 10**9
total = [0] * (N+1)


def dijkstra(start, end, dist):
    dist[start] = 0
    q= []
    heapq.heappush(q, (0,start))
    while(q):
        dst, node = heapq.heappop(q)
        for dest,weight in graph[node]:
            cost = dst+weight
            if(dist[dest]>cost):
                dist[dest] = cost
                heapq.heappush(q, (cost,dest))


for i in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

for i in range(1,N+1):
    dist_come = [INF] * (N+1)
    dist_back = [INF] * (N+1)
    dijkstra(i,end, dist_come)
    dijkstra(end,i, dist_back)
    total[i] = dist_come[end]+dist_back[i]

print(max(total[1:]))