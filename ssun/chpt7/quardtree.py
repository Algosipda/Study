def quard_tree(image):
	if len(image) == 1:
		return image
	else:
		pointer = 1
		image_pices = []
		for i in range(0, 4):
			if not image[pointer] == 'x':
				image_pices.append(image[pointer])
				pointer += 1
			else:
				pice = quard_tree(image[pointer:])
				image_pices.append(pice)
				pointer += len(pice)
		return 'x' + image_pices[2] + image_pices[3] + image_pices[0] + image_pices[1]


def main():
	test_case = int(input())
	while test_case > 0:

		image = input()
		print(quard_tree(image))

		test_case -= 1

if __name__ == '__main__':
    main()
