#k번째 큰 수 구하기

#solution
n, k = map(int, input().split())
l = list(map(int, input().split()))
result = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(l[i] + l[j] + l[m])
result = list(result)
result.sort(reverse=True)
print(result[k-1])
