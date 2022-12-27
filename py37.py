#프로그래머스 멀리뛰기 level 2
n = int(input())
if n <= 3:
    print(n)
    
else:   
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 2      
    for i in range(3,n+1):
        arr[i] = (arr[i-1] + arr[i-2])%1234567
    print(arr[n])