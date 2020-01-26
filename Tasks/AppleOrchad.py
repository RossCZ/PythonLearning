# v sadu je v řadě "n" stromů každý s "m" jablky
# do sadu půjdou sběrači alice a bob
# alice zvládne posbírat jablka z "K" stromů v řadě
# bob zvládne posbírat jablka z "L" stromů v řadě
# kolik maximálně jablek zvládnou sběrači posbírat?

# returns sorted list of possible outcomes for a picker
# (start index, number of apples)
def get_sorted_lists(orchad_trees, number_of_trees):
    tree_count = len(orchad_trees)

    collector_list = []
    for i in range(0, tree_count - number_of_trees + 1):
        res = orchad_trees[i:i + number_of_trees]
        apples = sum(res)
        # print(res, ":", apples)
        collector_list.append((i, apples))

    collector_list = sorted(collector_list, key=lambda tup: tup[1])
    collector_list.reverse()
    # print(alice_list)
    # print(alice_list_sorted)
    return collector_list


def solution(orchad_trees, K, L):
    tree_count = len(orchad_trees)
    if K + L > tree_count:
        return -1

    # get possible outcomes for alice and bob
    alice_list = get_sorted_lists(orchad_trees, K)
    bob_list = get_sorted_lists(orchad_trees, L)
    print(alice_list)
    print(bob_list)

    # find max number w/o overlaps
    alice_items = len(alice_list)
    bob_items = len(bob_list)

    valid_combinations = []

    for i in range(0, alice_items):
        inx_a = alice_list[i][0]
        for j in range(0, bob_items):
            inx_b = bob_list[j][0]
            # not valid if trees overlaps
            if (inx_a > inx_b and inx_a - inx_b >= L) or (inx_b > inx_a and inx_b - inx_a >= K):
                total_apples = alice_list[i][1] + bob_list[j][1]
                valid_combinations.append((i, j, total_apples))
            # else:
                # print("invalid indexes:", inx_a, inx_b)

    valid_combinations = sorted(valid_combinations, key=lambda tup: tup[2])
    valid_combinations.reverse()
    print(valid_combinations)
    print(valid_combinations[0])
    return valid_combinations[0][2]


print(solution([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
print(solution([8, 1, 3, 3, 5, 4, 1, 9, 2, 7, 4, 5, 1, 2, 3, 8, 2], 4, 3))
