def cutting_fence(fence):
	if len(fence) == 1:
		return fence[0]
	else:
		res = 0
		for i in range(0, len(fence)):
			left = cutting_left(fence, i)
			right = cutting_right(fence, i)
			cal = (left+right+1)*fence[i]
			if res < cal:
				res = cal
		return res

def cutting_left(fence, iterator):
	ver = fence[iterator]
	hor = 0
	for i in range(iterator-1, 0):
		if ver > fence[i]:
			break
		else:
			hor += 1
	return hor

def cutting_right(fence, iterator):
	ver = fence[iterator]
	hor = 0
	for i in range(iterator+1, len(fence)):
		if ver > fence[i]:
			break
		else:
			hor += 1
	return hor

def main():
	test_case = int(input())
	while test_case > 0:
		fence_size = int(input())
		fence = [int(x) for x in input().split()]

		print(cutting_fence(fence))
		test_case -= 1

if __name__ == "__main__":
	main()