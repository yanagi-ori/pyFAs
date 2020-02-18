def generate_pairs(first_part, second_part):
    """ creating pairs of teams - matches """
    week = []
    for i in range(len(first_part)):
        week.append((first_part[i], second_part[i]))
    return week
