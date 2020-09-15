#이분검색
#이분검색알고리즘: 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘

n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt + rt) // 2
    if l[mid] == m:
        print(mid + 1)
        break
    elif l[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
