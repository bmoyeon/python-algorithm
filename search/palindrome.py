#회문 문자열 검사

n = int(input())
for i in range(n):
    s = input()
    s = s.lower()
#    if s == s[::-1]:
#        print(f'#{i+1} YES')
#    else:
#        print(f'#{i+1} NO')
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1-j]:
            print(f'#{i+1} NO')
            break
    else:
        print(f'#{i+1} YES')

