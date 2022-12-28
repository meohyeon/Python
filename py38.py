k = int(input())
tangerine = list(map(int, input().split()))
total = 0
arr = {}
answer = 0
for i in tangerine:
    if i not in arr:
        arr[i] = 1
    else:
        arr[i] += 1
        
arr = sorted(arr.items(), key = lambda x:-x[1])

for a, b in arr:
    for i in range(b):
        total += 1
        if total == k:
            break
    answer +=1
    if total == k:
        break
print(answer)