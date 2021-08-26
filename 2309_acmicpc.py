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
            
