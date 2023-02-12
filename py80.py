#프로그래머스 2016년
import datetime
a, b = map(int,input().split())

x = datetime.date(2016,a,b)
answer = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

print(answer[x.weekday()])