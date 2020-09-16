#창고 정리

l = int(input())
store = list(map(int, input().split()))
m = int(input())
store.sort()

for _ in range(m):
    store[0] += 1
    store[-1] -= 1
    store.sort()
print(store[-1] - store[0])
