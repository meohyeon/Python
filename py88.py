order = list(map(int,input().split()))
answer = []
cnt = 0
for i in range(1,len(order)+1):
    answer.append(i)
    while answer and answer[-1] == order[cnt]:
        cnt += 1
        answer.pop()
print(cnt)