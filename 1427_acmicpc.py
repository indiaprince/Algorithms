def q_sort(ls, low, high):
    if(low>high) : return
    pivot = ls[int((low+high)/2)]
    left = low
    right = high
    while(left<=right):
        while(ls[left]>pivot) : left=left+1
        while(ls[right]<pivot) : right=right -1
        if(left<=right):
            tmp = ls[left]
            ls[left] = ls[right]
            ls[right] = tmp
            left=left+1
            right = right -1
    q_sort(ls, low,right)
    q_sort(ls, left,high)
    
N = input()
ls= []
for i in range(len(N)):
    ls.append(N[i])
q_sort(ls, 0,len(ls)-1)
answer=""
for i in range(len(ls)):
    answer=answer + str(ls[i])
print(answer)
