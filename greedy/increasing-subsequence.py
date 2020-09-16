#증가수열 만들기
n = int(input())
l = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
result = ''
tmp = []
while lt <= rt:
    if l[lt] > last:
        tmp.append((l[lt], 'L'))
    if l[rt] > last:
        tmp.append((l[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        result += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(result))
print(result)
