# 프로그래머스 연속 부분 수열 합의 개수 level 2
elements = list(map(int, input().split()))
arr = set()
elen = len(elements)
# 원형 큐를 위해 단순이 리스트를 2개를 이어 붙힌다
elements = elements * 2
for i in range(elen):
    for j in range(1,elen+1):
        print(j+i)
        arr.add(sum(elements[i:j+i]))
    print(end='\n')
print(len(arr))