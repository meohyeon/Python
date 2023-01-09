k = 80
dungeons = [[80,20],[50,40],[30,10]]
vit = [0] * len(dungeons)
answer = 0
def dfs(k,dungeons,cnt,vit):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and vit[i] == 0:
            vit[i] = 1
            dfs(k-dungeons[i][1],dungeons,cnt+1,vit)
            vit[i] = 0

dfs(k,dungeons,0,vit)
print(answer)