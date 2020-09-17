#가장 큰 수
#스택: 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 자료 구조
#나중에 들어간게 먼저 나온다. (Last In First Out)

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for i in num:
    while stack and m > 0 and stack[-1] < i:
        stack.pop()
        m -= 1
    stack.append(i)
if m != 0:
    stack = stack[:-m]
result = ''.join(map(str, stack))
print(result)
