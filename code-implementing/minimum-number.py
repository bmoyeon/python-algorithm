#최솟값 구하기

l = [5, 3, 7, 9, 1, 5, 2, 6]

#float('inf') = inf: 양의 무한대
#float('-inf') = -inf: 음의 무한대

minimum_num = l[0]
for num in l:
    if num < minimum_num:
        minimum_num = num
print(minimum_num)
