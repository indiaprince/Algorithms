import sys
input = sys.stdin.readline

N = int(input())

values = list(map(int, input().split()))
ops = list(map(int , input().split()))

mn =1000000001
mx = -1000000001
def dfs(plus, minus, mul, div, values, idx, total,N):
    global mn,mx
    if(plus==0 and minus==0 and mul==0 and div==0): 
        mx = max(mx,total)
        mn = min(mn,total)
        return

    if(plus>0):
        dfs(plus-1,minus,mul,div,values,idx+1,total+values[idx+1],N)
    if(minus>0):
        dfs(plus,minus-1,mul,div,values,idx+1,total-values[idx+1],N)
    if(mul>0):
        dfs(plus,minus,mul-1,div,values,idx+1,total*values[idx+1],N)
    if(div>0):
        if(total>0):
            dfs(plus,minus,mul,div-1,values,idx+1,total//values[idx+1],N)
        else:
            tmp = -total
            tmp = tmp//values[idx+1]
            dfs(plus,minus,mul,div-1,values,idx+1,-tmp,N)
total, idx = values[0], 0 
dfs(ops[0], ops[1], ops[2], ops[3], values,idx,total,N)
print(mx)
print(mn)