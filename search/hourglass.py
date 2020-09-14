#모래시계 영역의 요소의 합 출력

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    r, t, c = map(int, input().split())
    if t == 0:
        for _ in range(c):
            l[r-1].append(l[r-1].pop(0))
    else:
        for _ in range(c):
            l[r-1].insert(0, l[r-1].pop())

s = 0
e = n
result = 0
for i in range(n):
    for j in range(s, e):
        result += l[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(result)
