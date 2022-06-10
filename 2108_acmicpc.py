import sys
input = sys.stdin.readline

N = int(input())

ls = [0 for _ in range(8001)]
ls2 = []
for _ in range(N): 
    num = int(input())
    ls[num+4000]+=1
    ls2.append(num)
ls2.sort()
print(ls[:20])
freq_max = -4001
freq_val = -4001
freq_second = -4001
for i in range(8001):
    if(freq_max<=ls[i]) : 
        freq_max = ls[i]
        freq_val = i
cnt = 0 
print(freq_max,freq_val)
for i in range(8001):
    if(freq_val == i): break
    if(freq_max == ls[i]): 
        if(cnt==1): 
            freq_val = i
            break
        else:
            cnt+=1
            freq_val = i


print(int(round(sum(ls2)/N,0)))
print(ls2[N//2])
print(freq_val-4000)
print((ls2[N-1]) - (ls2[0]))