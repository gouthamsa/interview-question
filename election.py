line = "-AB-----AB-"
def election(line):
    previous_influencer = None
    previous_neutral_index = 0
    previous_influencer_index = 0
    A_count = 0
    B_count = 0
    neutral_count = 0
    for i, voter in enumerate(line):
        if voter == '-':
            neutral_count += 1
        elif voter == 'A':
            A_count += 1
            if previous_influencer in (None, 'A'):
                A_count += neutral_count
            else:
                A_count += neutral_count // 2
                B_count += neutral_count // 2
            previous_influencer = 'A'
            neutral_count = 0
        else:
            B_count += 1
            if previous_influencer in ('B',):
                B_count += neutral_count
            elif previous_influencer in ('A',):
                A_count += neutral_count // 2
            previous_influencer = 'B'
            neutral_count = 0
    if neutral_count:
        if previous_influencer == 'B':
            B_count += neutral_count

    print (A_count)
    print (B_count)

    if A_count > B_count:
        print ("A won")
    elif B_count > A_count:
        print ("B won")
    else:
        print ("Coalition")



if __name__ == '__main__':
    election(line)
