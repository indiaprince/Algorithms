def solution(n, arr1, arr2):
    answer = []
    map1= [[] for i in range(n)]
    map2= [[] for i in range(n)]
    for i in range(n):
        t1 = ''
        t2= ''
        for j in range(n):
            if(arr1[i]%2==0): t1+='0'
            else : t1+='1'
            arr1[i]=arr1[i]//2
            if(arr2[i]%2==0): t2+='0'
            else : t2+='1'
            arr2[i]=arr2[i]//2            
        map1[i]=t1
        map2[i]=t2
    for i in range(n):
        tmp = ''
        for j in range(n):    
            if(map1[i][j]=='1' or map2[i][j]=='1'): tmp+='#'
            if(map1[i][j]=='0' and map2[i][j]=='0') :tmp+=' '
        tmp = tmp[::-1]
        answer.append(tmp)
    return answer
