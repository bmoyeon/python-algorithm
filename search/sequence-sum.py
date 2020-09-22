#연속된 수열의 합이 입력받은 수가 되는 경우의 수 출력

n, m = map(int, input().split())
l = list(map(int, input().split()))

lt = 0
rt = 1
total = l[0]
count = 0
while True:
    if total < m:
        if rt < n:
            total += l[rt]
            rt += 1
        else:
            break
    elif total == m:
        count += 1
        total -= l[lt]
        lt += 1
    else:
        total -= l[lt]
        lt += 1
print(count)
