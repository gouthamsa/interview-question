def supportA(voter):
    for index, value in enumerate(voter):
        if 'A' in voter:
            if value == 'A' and index == 0:
                if value == 'B' not in voter:
                    break
            elif index != len(voter) - 1:
                if value == '-' and voter[index +
                                          1] == 'A' and voter[index -
                                                              1] == 'B':
                    value = '-'
                else:
                    if value == 'A' and voter[index - 1] == '-':
                        voter[index - 1] = 'A'
    return voter


def supportB(voter):
    for index, value in enumerate(voter):
        if 'B' in voter:
            if value == 'B' and index == len(voter) - 1:
                if value == 'A' not in voter:
                    break
            elif index != 0:
                if value == '-' and voter[index -
                                          1] == 'B' and voter[index +
                                                              1] == 'A':
                    value = '-'
                else:
                    if value == 'B' and voter[index + 1] == '-':
                        voter[index + 1] = 'B'
    return voter


if __name__ == "__main__":
    voter = list(input("enter voter list"))
    supportA(voter)
    supportB(voter)
    print(voter)
