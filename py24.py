# 프로그래머스 n개의 최소 공배수 level 2
from math import gcd
arr = list(map(int,input().split()))

answer = arr[0]
arr.remove(arr[0])

for i in arr:
    answer = answer * i // gcd(answer,i)

print(answer)