#뮤직비디오

n, m = map(int, input().split())
l = list(map(int, input().split()))
largest = max(l)

def dvd_count(x):
    count = 1
    total = 0
    for i in l:
        if total + i > x:
            count += 1
            total = i
        else:
            total += i
    return count

lt = 1
rt = sum(l)
result = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= largest and dvd_count(mid) <= m:
        result = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(result)
