#역수열

n = int(input())
l = list(map(int, input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if l[i]== 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            l[i] -= 1
for i in seq:
    print(i, end= ' ')
