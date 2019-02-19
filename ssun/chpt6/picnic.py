
def count_pairing(student_num, is_paired, pair):

	if student_num == len(is_paired):
		return 1

	if is_paired[student_num]:
		return count_pairing(student_num+1, is_paired, pair)

	else:
		res = 0
		for student in pair[student_num]:
			if not is_paired[student]:
				is_paired[student] = True
				is_paired[student_num] = True
				res += count_pairing(student_num+1, is_paired, pair)
				is_paired[student] = False
				is_paired[student_num] = False

		return res



if __name__ == "__main__":
	test_case = int(input())

	while test_case > 0:
		num_student, num_pair = map(int, input().split(' '))
		pair = [[] for x in range(int(num_student))]
		
		inputed = [int(x) for x in input().split()]
		is_paired = [False for i in range(0, num_student)]

		for i in range(0, num_pair):
			pair[inputed[i*2]].append(inputed[(i*2)+1])
			pair[inputed[(i*2)+1]].append(inputed[i*2])

		print(count_pairing(0, is_paired, pair))

		test_case -= 1