# 프로그래머스 모음사전 level 2
word = input()
answer = 0
wordarr = ['A','E','I','O','U']

def dfs(string):
    global answer
    answer += 1
    if string == word:
        return True
    if len(string) == 5:
        return False
    for i in wordarr:
        if dfs(string+i):
            return True

for i in wordarr:
    if dfs(i):
        print(answer)
        break