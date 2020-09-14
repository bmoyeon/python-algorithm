#봉우리의 개수 구하기

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.insert(0, [0]*n)
l.append([0]*n)
for i in l:
    i.insert(0, 0)
    i.append(0)

#top, right, bottom, left - l[i][j]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(l[i][j] > l[i+dx[k]][j+dy[k]] for k in range(4)):
            count += 1
print(count)
