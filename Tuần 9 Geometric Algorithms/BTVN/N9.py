A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
#A->B->C

dic={0:"Clockwise",1:"CounterClockwise",2:"Colinear"}


def printResult(A,B,C):
    r=(B[0]-A[0])*(C[1]-A[1])-(B[1]-A[1])*(C[0]-A[0])
    if r<0:
        return 0
    elif r>0:
        return 1
    else:
        return 2
    

print(dic[printResult(A,B,C)])


