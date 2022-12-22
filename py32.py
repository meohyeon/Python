# 프로그래머스 최대값과 최솟값 level2 
n = input()

arr = list(map(int, n.split()))
arr.sort()

answer = str(min(arr)) + " " + str(max(arr))

print(answer)