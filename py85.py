#프로그래머스 타겟넘버 level 2
from itertools import product
numbers = list(map(int,input().split()))
target = int(input())

answer = 0
def dfs(arr,target,value):
    global answer
    if 0 == len(arr):
        if value == target:     
            answer += 1 
        return
    dfs(arr[1:],target,value+arr[0])
    dfs(arr[1:],target,value-arr[0])

dfs(numbers,target,0)
print(answer)

#다른풀이 product 중복 순열 사용 
arr2 = [(x,-x)for x in numbers]
answer2 = [sum(x)for x in product(*arr2)]
print(answer2.count(target))