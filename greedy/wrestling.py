#씨름 선수

n = int(input())
player = []
for i in range(n):
    h, w = map(int, input().split())
    player.append((h, w))

#키 순으로 내림차순 정렬하여 첫번째 사람은 해당되므로 counting 하고
#그 다음 순부터는 윗 사람과의 몸무게 비교 중 가장 크면 counting 하면 된다.
player.sort(reverse=True)

largest = 0
count = 0
for h, w in player:
    if w > largest:
        largest = w
        count += 1
print(count)
