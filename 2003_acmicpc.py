import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ls = list(map(int, input().split()))
cnt =0
partial_sum=0
s = e = 0

while(1):
    #print(f"s : {s}, e : {e} {partial_sum}")
    if(partial_sum>=M): 
        partial_sum-=ls[s]
        s+=1
    elif(e==N): break
    else:
        partial_sum+=ls[e]
        e+=1
    if(partial_sum == M): cnt+=1

print(cnt)

'''
while(1):
    #print(f"s : {s}, e : {e} {partial_sum}")
    if(s>=e and e==N): break
    if(partial_sum>=M): 
        partial_sum-=ls[s]
        s+=1
    elif(partial_sum<M):
        if(e!=N):
            partial_sum+=ls[e]
            e+=1
        else: break
    if(partial_sum == M): 
        cnt+=1

print(cnt)'''