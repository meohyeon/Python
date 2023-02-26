#프로그래머스 타겟넘버 level 2
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