inpt=[]
total = 0

for i in range(9):
    inpt.append(int(input()))
    total+=inpt[i]
done = False
inpt = sorted(inpt)
for i in range(0, len(inpt)):
    for j in range(i+1,len(inpt)):
        if total-(inpt[i]+inpt[j])==100:
            inpt[i]=0
            inpt[j]=0
            for k in range(9):
                if(inpt[k]!=0): print(inpt[k])
            done = True
        if done==True: break
    if done==True: break
            
##
## 재시도
def dwarf(D,flag,total):
    for i in range(9):
        for j in range(i,9):
            if(total - D[i]-D[j]==100):
                flag[i] = False
                flag[j] = False
                return

D = []
flag = [True for x in range(9)]
done = False
total = 0


for i in range(9):
    tmp = int(input())
    D.append(tmp)
    total+=tmp
D.sort()

dwarf(D,flag,total)

for i in range(9):
    if(flag[i]) : print(D[i])
            
            
