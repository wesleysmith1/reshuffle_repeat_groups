import random

def check_rematching(previous, current):
    """Does the previous list, have any of the same groups as current list."""
    for group in current:
        if group in previous:
            return True
    return False


def generate_groups(rounds, participant_count):
    """
        Generate group matrix like the following:
        [
            [(3, 8), (9, 6), (7, 4), (5, 2), (1, 10)],
            [(3, 2), (5, 6), (1, 10), (9, 4), (7, 8)]
        ]
    """
    ids = [i+1 for i in range(participant_count)]
    odd = ids[0:len(ids):2]
    even = ids[1:len(ids):2]

    groups = []
    # generate all groups
    for i in range(rounds):
        random.shuffle(odd)
        random.shuffle(even)
        groups.append(list(zip(odd, even)))

    return groups

def random_group(participant_count):
    """
        Create list of groups like the following:
        [(3, 8), (9, 6), (7, 4), (5, 2), (1, 10)]
    """
    ids = [i+1 for i in range(participant_count)]
    odd = ids[0:len(ids):2]
    even = ids[1:len(ids):2]
    random.shuffle(odd)
    random.shuffle(even)
    return list(zip(odd, even))

def no_repeat_pairs(group_matrix, participant_count):
    """Ensure no repeat paris from list of groups to the next in group_matrix"""
    for i in range(len(group_matrix)):
        if i == 0:
            continue

    while check_rematching(group_matrix[i-1], group_matrix[i]):
        # reshuffle current
        group_matrix[i] = random_group(participant_count)

    return group_matrix


def main():
    """Demonstration"""
    gmatrix = generate_groups(10,10)

    print("Group matrix:")

    for g in gmatrix:
        print(g)

    print("Checking group matrix for repeat pairs...")

    no_repeat_pairs(gmatrix, 10)

    for g in gmatrix:
        print(g)

if __name__ == "__main__":
    main()
