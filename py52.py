# 프로그래머스 소수찾기 level 2
from itertools import permutations

numbers = input()
per = []
arr = [x for x in numbers]
answer = 0

for i in range(1,len(arr)+1):
    per+=(permutations(arr,i))

arr = [int(("").join(p)) for p in per] 
arr= set(arr)
num = [x for x in range(max(arr)+1)]
num[1]=0
for i in range(2,len(num)):
    if num[i] != 0:      
        for j in range(i+i,len(num),i):
            num[j] = 0

for i in arr:
    if num[i] != 0:
        answer += 1
print(answer)