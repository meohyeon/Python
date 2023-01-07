#프로그래머스 프린터 level 2
priorities = list(map(int,input().split()))
location = int(input())

index = [x for x in range(len(priorities))]
a = len(priorities)
i = 0
answer = 0

while i < a:
    if priorities[i] < max(priorities[i:]):
        index.append(index.pop(i))
        priorities.append(priorities.pop(i))
    else:
            i +=1  

answer = index.index(location)+1
print(answer)