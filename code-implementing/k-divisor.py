#k번째 약수 구하기

def k_divisor(n, k):
    result = []
    for num in range(1, n+1):
        if n % num == 0:
            result.append(num)
    if k > len(result):
        return -1
    return result[k-1]

#solution
n, k = map(int, input().split())
count = 0
for num in range(1, n+1):
    if n % num == 0:
        count += 1
    if count == k:
        print(num)
        break
else:
    print(-1)
