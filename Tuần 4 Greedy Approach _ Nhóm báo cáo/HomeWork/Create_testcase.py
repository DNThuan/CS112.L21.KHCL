
# Knapsack Problem

class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt
 
    def __lt__(self, other):
        return self.cost < other.cost
 
# Greedy Approach
class KnapSack:

    @staticmethod
    def getMaxValue(wt, val, capacity):

        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
 
        iVal.sort(reverse=True)
        
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else: 
            #vì chúng ta không chia nhỏ các món hàng nên bỏ qua phần này
                '''
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction)
                break
                '''
        return totalValue
 
#Source: https://www.geeksforgeeks.org/fractional-knapsack-problem/


#Create_Testcase
import random
 
for t in range(20): #create_testcase
    name_of_file="Testcase/testcase_"+str(t)+".in"
    with open(name_of_file,"a+") as f_:
        values,weights=[],[]
        test_case=random.randint(1,10) #lenght per test case
        capacity=random.randint(20,50)
        for _ in range(test_case):
            value=random.randint(1,50)
            values.append(value)
            weights.append(int(2*value+2))
        maxValue = KnapSack.getMaxValue(weights, values, capacity)
        
        v=str(values).strip('[]').replace(",","")
        w=str(weights).strip('[]').replace(",","")
        i=v+"\n"+w+"\n"+str(capacity)+"\n"+str(maxValue)+"\n"
        f_.write(i)
            


