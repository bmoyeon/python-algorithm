#입력된 구간의 카드 역배치

l = list(range(21))
#_로 해놓으면 변수 저장없이 10번 반복된다.
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        l[s+i], l[e-i] = l[e-i], l[s+i]
l.pop(0)
for i in l:
    print(i, end= ' ')
