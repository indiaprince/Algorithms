# 한 줄 읽고 정수 변환
#N = int(input())

# 한 줄 읽고 공백으로 문자 구분
#N = input().split()

# 한 줄 읽어서 정수 변환

#M, N = map(int, input().split())

# 입력 데이터 개수 모르면

#arr = list(map(int, input().split()))

count = 1
while(True):
    L, P, V = map(int, input().split())
    if(L==0 and P==0 and V==0): break
    days = V//P
    days = days*L
    if(V%P>L):
        lastdays = L
    else:
        lastdays = V%P
    days += lastdays
    print(f"Case {count}: {days}")
    count+=1
