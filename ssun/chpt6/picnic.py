
test_case = int(input())
pair = []

def contact_pair(index, has_mate):
	global count
	if check_countable():
		count += 1
	elif has_mate[index]:
		contact_pair(index+1, has_mate)
	else:
		for num in pair[index]:
			if not has_mate[num]:
				has_mate[num] = True
				has_mate[index] = True
				contact_pair(index + 1,has_mate)
				has_mate[num] = False
				has_mate[index] = False

				
def check_countable():
	for boolean in has_mate:
		if not boolean:
			return False
	return True

while test_case > 0:
	global count
	count = 0
	student_num, pair_num = input().split(' ')
	raw_pair = input().split(' ')

	has_mate = [False for x in range(int(student_num))]
	pair = [[] for x in range(int(student_num))]

	for i in range(0, int(pair_num)):
		first = int(raw_pair[i*2])
		last = int(raw_pair[(i*2)+1])

		pair[first].append(last)
		pair[last].append(first)


	contact_pair(0, has_mate)
	print(count)

	test_case -= 1

