import sys
input = sys.stdin.readline

s = input()[:-1]
freq = [0 for _ in range(100)]
for i in range(len(s)):
    ch = s[i].lower()
    order = ord(ch) - ord('a')
    freq[order] +=1

mx_cnt = 0 
mx_char = ''
mx = max(freq)
for i in range(len(freq)):
    if(freq[i]==mx): 
        mx_cnt+=1
        mx_char = chr(i+ord('a'))

if(mx_cnt>=2) : print('?')
else: print(mx_char.upper())


