
flag = False
N = int(input())
for i in range(N):
    total =0
    s= str(i)
    for j in range(len(s)):
        total+=int(s[j])
    total+=i
    if total == N:
        print(i)
        flag=True
        break
if flag==False:
    print(0)

    
    
