def supporters(voters):
    for index, value in enumerate(voters):
        if value == '-' and voters[index + 1] == 'A' and voters[index -
                                                                1] == 'B':
            voters[index] = '-'
        elif value == '-' and voters[index + 1] == 'A':
            voters[index] = 'A'
        elif value == '-' and voters[index - 1] == 'B':
            voters[index] = 'B'
        elif value == '-':
            pass
    return voters


def voters_count(voters):
    count_A_voters = 0
    count_B_voters = 0
    count_neutral_voters = 0
    for voter in voters:
        if voter == "A":
            count_A_voters += 1
        elif voter == "B":
            count_B_voters += 1
        elif voter == "-":
            count_neutral_voters += 1
    if count_A_voters > count_B_voters:
        return print('A voters wins')
    elif count_B_voters > count_neutral_voters:
        return print('B voters wins')
    elif count_neutral_voters > count_A_voters:
        return print('neutral voters wins')


if __name__ == "__main__":
    no_of_voters = int(input("enter total number of voter"))
    voters = list(input("enter voters list"))
    supporter_list = list(supporters(voters))
    print(supporter_list)
    count = voters_count(supporter_list)
