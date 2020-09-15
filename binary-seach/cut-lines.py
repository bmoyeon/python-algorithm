#랜선 자르기

k, n = map(int, input().split())
l = []
largest = 0
for i in range(k):
    tmp = int(input())
    l.append(tmp)
    largest = max(largest, tmp)

def line_count(x):
    count = 0
    for i in l:
        count += i // x
    return count

lt = 1
rt = largest
result = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if line_count(mid) >= n:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)
