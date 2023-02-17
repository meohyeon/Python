#프로그래머스 옹알이(2)
babbling = list(input().split())
arr1 = ["aya","ye","woo","ma"]
answer = 0
for i in babbling:
    for j in arr1:
        if j*2 not in i:  # 연속된 발음 체크   
            i = i.replace(j," ")
    if i.strip() == "":
        answer += 1
print(answer)