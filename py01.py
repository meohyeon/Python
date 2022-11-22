#프로그래머스: 코딩테스트 연습 > 정렬 > K번쨰수
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
anwer=[]



def Operator():
    for i in range(len(commands)):
        a=[]
        a=array[commands[i][0]-1:commands[i][1]]
        a.sort()
        anwer.append(a[commands[i][2]-1])
  


Operator()
print(anwer)

