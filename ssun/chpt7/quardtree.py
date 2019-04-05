def reverse_picture(picture):
    global index
    reversed_picture = []

    for i in range(0, 4):
        if picture[index] == 'x':
            index += 1
            reversed_picture.append(reverse_picture(picture))
        else:
            reversed_picture.append(picture[index])
            index += 1
    return 'x'+reversed_picture[2] + reversed_picture[3] + reversed_picture[0]+reversed_picture[1]


if __name__ == "__main__":
    test_case = int(input())

    while test_case > 0:
        global index
        index = 0
        picture = input()
        if picture[index] == 'x':
            index += 1
            print(reverse_picture(picture))
        else:
            print(picture)
        test_case -= 1
