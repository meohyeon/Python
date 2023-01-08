#프로그래머스 더 맵게 level 2
from heapq import heapify,heappush,heappop
scoville = list(map(int,input().split()))
K = int(input())

heapify(scoville)
count = 0

while scoville[0] < K and len(scoville) > 1:
    a, b = heappop(scoville), heappop(scoville)
    heappush(scoville,a+b*2)
    count += 1
if scoville[0] < K:
    count = -1

print(count)