#프로그래머스 문자열 마음대로 정렬 
strings = ["sun", "bed", "car"]
n = 1
print(sorted(strings,key=lambda x:(x[n],x)))