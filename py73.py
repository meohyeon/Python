#프로그래머스 행렬의 덧셈 
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# zip 함수 사용
answer = [[x+y for x,y in zip(a1,a2)]for a1,a2 in zip (arr1,arr2)]
print(answer)
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        arr1[i][j] += arr2[i][j]
print(arr1)
