# Câu hỏi của nhóm 10: Khi dùng hướng tiếp cận tham lam, làm sao để xác định được cấu trúc con tối ưu cho bài toán?
import numpy as np

def knapSack(W, weight, value, n):
	count_value = 0
	ratio = (np.array(value)/np.array(weight))
	ratio = sorted(range(n), key=lambda k: ratio[k])
	for i in range(n-1,-1,-1):
		index = ratio[i]
		W += -weight[index]
		if W < 0:
			break
		count_value -= -value[index]
	return count_value