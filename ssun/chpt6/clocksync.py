def sync_clock(clocks, index):
    global buttons
    res = 2147483547

    if index == len(buttons):
        if are_assigned(clocks):
            return 0
        else:
            return res
    else:
        temp = 0
        for i in range(0, 4):
            temp = i + sync_clock(clocks, index + 1)
            if res > temp:
                res = temp
            clocks = push_button(clocks, buttons[index])

        return res


def push_button(clocks, linked_clocks):
    for linked_clock in linked_clocks:
        clocks[linked_clock] = clocks[linked_clock] + 3
        if clocks[linked_clock] > 12:
            clocks[linked_clock] -= 12
    return clocks


def are_assigned(clocks):
    for i in range(0, len(clocks)):
        if not clocks[i] == 12:
            return False
    return True


def main():
    global buttons

    buttons = [[0, 1, 2], [3, 7, 9, 11], [4, 10, 14, 15], [0, 4, 5, 6, 7], [6, 7, 8, 10, 12], [
        0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15], [1, 2, 3, 4, 5], [3, 4, 5, 9, 13]]

    test_case = int(input())
    while test_case > 0:
        clocks = []

        for clock in input().split(' '):
            clocks.append(int(clock))

        print(sync_clock(clocks, 0))
        test_case -= 1


if __name__ == "__main__":
    main()
