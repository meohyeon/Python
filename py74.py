#프로그래머스 문자열 마음대로 정렬 
strings1 = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]
n1 = 1
n2 = 2
print(sorted(strings1,key=lambda x:(x[n1],x)))
print(sorted(strings2,key=lambda x:(x[n2],x)))