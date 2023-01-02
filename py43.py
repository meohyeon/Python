#프로그래머스 땅따먹기 level 2
n = int(input())
land = [list(map(int,input().split()))for _ in range(n)]
for i in range(1,n):
    for j in range(4):
        land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
print(max(land[n-1]))