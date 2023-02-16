#프로그래머스 과일 장수 
k, m = map(int,input().split())
score = list(map(int,input().split()))

score.sort(reverse=True)
answer = [min(score[i*m:(i+1)*m])*m for i in range(0,len(score)//m)]

print(sum(answer))