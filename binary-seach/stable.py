#마구간 정하기

n, c = map(int, input().split())
l = []
for _ in range(n):
    tmp = int(input())
    l.append(tmp)
l.sort()

def horse_count(x):
    count = 1
    ep = l[0]
    for i in range(1, n):
        if l[i] - ep >= x:
            count += 1
            ep = l[i]
    return count

lt = 1
rt = l[-1]
result = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if horse_count(mid) >= c:
        result = mid
        lt = mid +1
    else:
        rt = mid - 1
print(result)
