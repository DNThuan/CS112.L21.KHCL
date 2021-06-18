def GetInput(n,value,weight):

    List = []
    for i in range(n):
        Temp = [int(value[i])]
        List.append(Temp)
        List[i].append(int(weight[i]))
    return List

def Max(a, k):
    S1 = 0
    Hold1 = 0
    for i in range(len(a)):
        if Hold1 + a[i][1] <= k:
            Hold1 = Hold1 + a[i][1]
            S1 = S1 + a[i][0]
    return S1

n = int(input())
a = GetInput(n)
a.sort(key=lambda x: x[0], reverse=True)
k = int(input())
print(Max(a, k))



