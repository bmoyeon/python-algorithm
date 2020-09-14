#다이아몬드 합 구하기

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
result = 0
s = e = n // 2

for i in range(n):
    for j in range(s, e+1):
        result += l[i][j]
    if i < n //2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(result)
