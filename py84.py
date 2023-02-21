arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
answer = [[0 for x in range(len(arr2[0]))]for _ in range(len(arr1))]
for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr1[0])):
            answer[i][j] += arr1[i][k]*arr2[k][j]
print(answer)

#zip 이용한 방법  zip(*arr2) ex) 열만 추출 
answer2 = [[sum(x*y for x,y in zip(arr1_row,arr2_col))for arr2_col in zip(*arr2)]for arr1_row in arr1]
print(answer2)