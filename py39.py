#프로그래머스 H-index level 2
citations = list(map(int, input().split()))

citations.sort(reverse=True)
answer = 0
cnt = 0
for i in range(len(citations)):
    if i >= citations[i]:
        cnt = 1
        answer = i
        break
if cnt == 0:
    answer = len(citations)
print(answer)