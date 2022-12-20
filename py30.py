# 프로그래머스 점 찍기 level2 
# 중심이 0.0 반지름이 d인 원 의 x,y축과 1사분면에 찍히는 점 갯수 구하기
import math
k, d = map(int, input().split())

answer = 0
for i in range(0,d+1,k):
    # 현재 x좌표에 대한 원의 y좌표 구하기 
    y = int(math.sqrt(d**2-i**2))
    #y좌표 내부에 찍을수 있는 점 갯수 구해서 더한다 +1은 y=0 일때 찍히는 점갯수를 추가한 것 k는 점들간의 거리 
    answer += ((y//k)+1)

print(answer)