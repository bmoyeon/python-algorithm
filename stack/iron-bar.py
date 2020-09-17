#쇠막대기
l = input()
stack = []
total = 0
for i in range(len(l)):
    if l[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if l[i-1] == '(':
            total += len(stack)
        else:
            total += 1
print(total)
