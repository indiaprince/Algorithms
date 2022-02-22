m = [  
       [0, 1, 0, 0, 1, 0, 0, 0, 1, 0 ],
       [1, 0 ,1 ,0 ,0, 0, 0, 0, 0, 0 ],
       [0, 1, 0, 1, 0, 0, 0, 0 ,0, 0 ],
       [0, 0, 1, 0, 0, 0, 0, 0 ,0 ,0 ],
       [1, 0, 0, 0, 0, 1, 0 ,1, 0, 0 ],
       [0, 0, 0, 0, 1, 0, 1, 0, 0, 0 ],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ]
      ]

m2 = [
    [1,4,8],
    [2],
    [3],
     [],
    [5,7],
    [6],
    [],
    [],
    [9],
    [10],
    []
]
N2 = len(m2)
V2 = []

def dfs_list(start):
    if(start in V2): return

    V2.append(start)
    print(start)
    for node in m2[start]:
        dfs_list(node)
dfs_list(0)
print(V2)


V3=[]
def dfs_list_while(start):
    stack = []
    stack.append(start)
    while(stack):
        node = stack.pop()
        if node not in V3:
            V3.append(node)
            stack.extend(m2[node])
    return

dfs_list_while(0)
print("V3-----")
print(V3)

M = len(m[0])
N = len(m)
V = [False]*N

def dfs(start):
    print(start)
    V[start] = True
    for i in range(N):
        if(m[start][i]==1 and V[i]==False):
            dfs(i)

dfs(0)