# 프로그래머스 2xN 타일링 level2 
n = int(input())
arr = [0] * n
arr[0] = 1
arr[1] = 2
for i in range(2,n):
    arr[i] = (arr[i-1] + arr[i-2])%1000000007
print(arr[n-1])