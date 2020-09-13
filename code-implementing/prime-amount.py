#자연수 n이 주어졌을 때 1부터 n까지의 소수 갯수 구하기

n = int(input())
l = [0]*(n+1)

count = 0
for i in range(2, n+1):
    if l[i] == 0:
        count += 1
        for j in range(i, n+1, i):
            l[j] = 1
print(count)
