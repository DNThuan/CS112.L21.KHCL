

#code_submit_Gr6-------------------------------------------------------------------
def knapSack(W, wt, val, n):
 
    if n == 0 or W == 0:
        return 0
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
'''
n = int(input())
bag = int(input())
val = list(map(int,input().split()))
w = list(map(int,input().split()))

print(knapSack(bag,w,val,n))
'''
#end-------------------------------------------------------------------------
       
'''
#code_submit_Gr7----------------------------------------------------------
def knapSack(n, value, weight, W):
    remaining_weight = W
    bag_value = i = 0
    count = 0
    while (i<n):
        if(weight[i] <= remaining_weight):
            remaining_weight -= weight[i]
            bag_value += value[i]
            count += 1
        i += 1
    if sum(weight[1:count+1]) <= W and count < n:
        bag_value = sum(value[1:count+1])
    return bag_value

n = int(input())
bag = int(input())
val = list(map(int,input().split()))
w = list(map(int,input().split()))

print(knapSack(bag,w,val,n))
'''
#end-----------------------------------------------------------

'''
#code_submit_Gr11--------------------------------------------------
n = int(input())
value = list(map(int, input().strip().split()))[:n]
weight = list(map(int, input().strip().split()))[:n]
k = int(input())

remaining_weight = k
bag_value = 0

def divide(item):
    return item[0]/item[1]

for i in range(0,n):
    x[i]=(value[i], weight[i])
sorted_x = sorted(x, key= divide)

for i in range(0,n):
  value[i], weight[i] = sorted_x[i]
  if (weight[i] <= remaining_weight):
    remaining_weight -= weight[i]
    bag_value += value[i]

print(bag_value)
#end--------------------------------------------------------------------------------
'''

#Test
Score=0

for i in range(20): #20 test case
    name_of_testcase="Testcase/testcase_"+str(i)+".in"
    with open(name_of_testcase,'r') as f_read:
        s=f_read.read().split("\n")
        
        values=list(map(int,s[0].split()))
        weights=list(map(int,s[1].split()))
        maxWeigh=int(s[2])
        result=int(s[3])
        n=len(values)

        a=knapSack(maxWeigh,weights,values,n)      

        #check
        if a==result:
            Score+=1
        else:
            #check_erro
            print("test "+str(i)+": output:",a,"result:",result)
print("Score:",Score,"/20")

        




