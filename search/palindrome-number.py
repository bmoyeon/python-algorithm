#5자리의 회문수의 개수 출력

board = [list(map(int, input().split())) for _ in range(7)]
count = 0
#5자리이기 때문에 3번만 돌면 된다.
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            count += 1
        #5자리이기 때문에 2번만 반복해서 비교하면 됨
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            count += 1
print(count)
