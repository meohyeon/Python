# 프로그래머스 가장큰 수 level 2
numbers = list(map(int,input().split()))
numbers = list(map(str,numbers))
# 원소의 범위가 1000 이하 이므로 3개를 이어붙혀 값 비교 
# ex) 3 -> 333 , 30 -> 303030 : 3 > 30
numbers.sort(key= lambda x:x*3,reverse=True)
# 모든원소가 0일경우 0000 이 아닌 0을 출력 해야함으로 정수로 바꿧다 다시 문자열로 출력
print(str(int(''.join(numbers))))