#회의실 배정
#탐욕 알고리즘: 최적해를 구하는 근사적인 방법으로,
#여러 경우 중 하나를 선택해야 할 때 그 순간에 최적을 선택해 나가는 방식

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

#끝나는 시간을 기준으로 정렬 -> 더 많은 회의를 배정할 수 있으므로
#끝나는 시간이 같다면 차순으로 시작하는 시간을 기준으로 정렬
#a = lambda x: (x+1, x+2)
#a(1) -> (2, 3)
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
count = 0
for s, e in meeting:
    if s >= et:
        et = e
        count += 1
print(count)
