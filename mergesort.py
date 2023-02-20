#합병정렬
arr = [6,5,3,1,8,7,2,4]


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    arr2 = []*len(arr)
    lf = 0
    rf = 0
    # 두 배열을 비교해서 작은값부터 arr2배열에 넣어준다 
    while lf < len(left) and rf < len(right):
        if left[lf] < right[rf]:
            arr2.append(left[lf])
            lf += 1
        else:
            arr2.append(right[rf])
            rf += 1
    # 혹시 배열에 남은값이 있음 더해준다 
    arr2 += left[lf:]
    arr2 += right[rf:]
    return arr2

print(mergesort(arr))