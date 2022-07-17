import sys
input =  sys.stdin.readline

N = int(input())
alpha = [0 for _ in range(30)]
for _ in range(N):
    st = ord(input()[0]) - ord('a')
    alpha[st]+=1

res =[]
for i in range(len(alpha)):
    if(alpha[i]>=5): res.append(chr(i+ord('a')))

if(res==[]): print('PREDAJA')
else:
    res.sort()
    for ch in res: print(ch, end='')