def make_pair(num, is_paired):
	global friends
	if num == len(is_paired):
		return 1
	elif is_paired[num]:
		return make_pair(num+1, is_paired)
	else:
		res = 0
		for i in friends[num]:
			if not is_paired[i]:
				is_paired[i] = True
				is_paired[num] = True
				res += make_pair(num+1, is_paired)
				is_paired[i] = False
				is_paired[num] = False
		return res

def main():
	global friends

	test_case = int(input())

	while test_case > 0:
		num_student, num_pair = map(int, input().split(' '))
		pairs = [int(x) for x in input().split()]
		
		is_paired = [False for i in range(0, num_student)]
		friends = [[] for i in range(0, num_student)]

		for i in range(0, num_pair):
			first = pairs[i*2]
			second = pairs[(i*2)+1]
			friends[first].append(second)
			friends[second].append(first)

		print(make_pair(0, is_paired))

		test_case -= 1


if __name__ == '__main__':
	main()