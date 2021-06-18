def main():
	n = int(input())
	value = [int(x) for x in input().split()]
	weight = [int(x) for x in input().split()]
	w = int(input())
	ratio = [(value[i]/weight[i], i) for i in range(n)]
	ratio.sort()
	ans = 0
	for _, index  in ratio:
		if weight[index] <= w:
			w -= weight[index]
			ans += value[index]

	print(ans)
