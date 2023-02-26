#프로그래머스 타겟넘버 level 2
from itertools import product
numbers = list(map(int,input().split()))
target = int(input())

answer = 0
def dfs(arr,target,cnt,value):
    global answer
    if cnt == len(arr):
        if value == target:     
            answer += 1 
        return
    dfs(arr,target,cnt+1,value+arr[cnt])
    dfs(arr,target,cnt+1,value-arr[cnt])

dfs(numbers,target,0,0)
print(answer)

#다른풀이 product 중복 순열 사용 
arr2 = [(x,-x)for x in numbers]
answer2 = [sum(x)for x in product(*arr2)]
print(answer2.count(target))